"""
Python 学习闯关平台 - 主应用文件
一个以闯关形式学习 Python 的全中文网站，特别针对软件测试方向
"""

from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'python-learning-secret-key-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///python_learning.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 数据库模型
class User(db.Model):
    """用户模型"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    progress = db.relationship('UserProgress', backref='user', lazy=True)
    wrong_questions = db.relationship('WrongQuestion', backref='user', lazy=True)

class Level(db.Model):
    """关卡模型"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    order = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # 基础、测试、工具、项目
    questions = db.relationship('Question', backref='level', lazy=True)

class Question(db.Model):
    """题目模型"""
    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(db.Integer, db.ForeignKey('level.id'), nullable=False)
    question_type = db.Column(db.String(20), nullable=False)  # choice, fill, code
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    options = db.Column(db.Text)  # JSON 格式的选项
    answer = db.Column(db.Text, nullable=False)
    explanation = db.Column(db.Text)
    order = db.Column(db.Integer, nullable=False)

class UserProgress(db.Model):
    """用户进度模型"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    attempts = db.Column(db.Integer, default=0)
    last_attempt = db.Column(db.DateTime)

class WrongQuestion(db.Model):
    """错题本模型"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    wrong_count = db.Column(db.Integer, default=1)
    added_date = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)

# 路由
@app.route('/')
def index():
    """首页"""
    return render_template('index.html')

@app.route('/levels')
def get_levels():
    """获取所有关卡"""
    levels = Level.query.order_by(Level.order).all()
    return jsonify([{
        'id': level.id,
        'title': level.title,
        'description': level.description,
        'order': level.order,
        'category': level.category,
        'question_count': len(level.questions)
    } for level in levels])

@app.route('/level/<int:level_id>')
def get_level(level_id):
    """获取关卡详情"""
    level = Level.query.get_or_404(level_id)
    questions = Question.query.filter_by(level_id=level_id).order_by(Question.order).all()
    
    return jsonify({
        'id': level.id,
        'title': level.title,
        'description': level.description,
        'questions': [{
            'id': q.id,
            'type': q.question_type,
            'title': q.title,
            'content': q.content,
            'options': json.loads(q.options) if q.options else None,
            'order': q.order
        } for q in questions]
    })

@app.route('/question/<int:question_id>')
def get_question(question_id):
    """获取题目详情"""
    question = Question.query.get_or_404(question_id)
    
    return jsonify({
        'id': question.id,
        'type': question.question_type,
        'title': question.title,
        'content': question.content,
        'options': json.loads(question.options) if question.options else None
    })

@app.route('/submit', methods=['POST'])
def submit_answer():
    """提交答案"""
    data = request.json
    question_id = data.get('question_id')
    user_answer = data.get('answer')
    username = session.get('username', 'guest')
    
    question = Question.query.get_or_404(question_id)
    
    # 检查答案
    correct = False
    if question.question_type == 'choice':
        correct = user_answer.strip() == question.answer.strip()
    elif question.question_type == 'fill':
        # 填空题支持多个可能的答案
        possible_answers = [ans.strip() for ans in question.answer.split('|')]
        correct = user_answer.strip() in possible_answers
    elif question.question_type == 'code':
        # 代码题需要执行并检查结果
        try:
            # 这里简化处理，实际应该在沙箱环境中执行
            exec_globals = {}
            exec(user_answer, exec_globals)
            # 根据题目要求检查结果
            correct = True  # 简化处理
        except Exception as e:
            correct = False
    
    # 获取或创建用户
    user = User.query.filter_by(username=username).first()
    if not user:
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
    
    # 更新用户进度
    progress = UserProgress.query.filter_by(user_id=user.id, question_id=question_id).first()
    if not progress:
        progress = UserProgress(user_id=user.id, question_id=question_id, attempts=0)
        db.session.add(progress)
    
    progress.attempts = (progress.attempts or 0) + 1
    progress.last_attempt = datetime.utcnow()
    if correct:
        progress.completed = True
    
    # 如果答错，添加到错题本
    if not correct:
        wrong = WrongQuestion.query.filter_by(user_id=user.id, question_id=question_id).first()
        if not wrong:
            wrong = WrongQuestion(user_id=user.id, question_id=question_id)
            db.session.add(wrong)
        else:
            wrong.wrong_count += 1
    
    db.session.commit()
    
    return jsonify({
        'correct': correct,
        'explanation': question.explanation,
        'answer': question.answer if not correct else None
    })

@app.route('/wrong_questions')
def get_wrong_questions():
    """获取错题本"""
    username = session.get('username', 'guest')
    user = User.query.filter_by(username=username).first()
    
    if not user:
        return jsonify([])
    
    wrong_questions = WrongQuestion.query.filter_by(user_id=user.id).all()
    
    return jsonify([{
        'id': wq.id,
        'question_id': wq.question_id,
        'question': Question.query.get(wq.question_id).title,
        'wrong_count': wq.wrong_count,
        'notes': wq.notes,
        'added_date': wq.added_date.strftime('%Y-%m-%d')
    } for wq in wrong_questions])

@app.route('/progress')
def get_progress():
    """获取学习进度"""
    username = session.get('username', 'guest')
    user = User.query.filter_by(username=username).first()
    
    if not user:
        return jsonify({'total': 0, 'completed': 0, 'percentage': 0})
    
    total_questions = Question.query.count()
    completed = UserProgress.query.filter_by(user_id=user.id, completed=True).count()
    
    return jsonify({
        'total': total_questions,
        'completed': completed,
        'percentage': round((completed / total_questions * 100) if total_questions > 0 else 0, 2)
    })

@app.route('/set_username', methods=['POST'])
def set_username():
    """设置用户名"""
    data = request.json
    username = data.get('username', 'guest')
    session['username'] = username
    return jsonify({'success': True})

def init_db():
    """初始化数据库"""
    with app.app_context():
        db.create_all()
        
        # 如果数据库为空，添加初始关卡和题目
        if Level.query.count() == 0:
            from init_data import initialize_levels_and_questions
            initialize_levels_and_questions(db, Level, Question)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
