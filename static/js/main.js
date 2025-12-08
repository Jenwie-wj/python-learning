// 全局变量
let currentLevelId = null;
let currentQuestionId = null;
let currentUsername = 'guest';
let codeTextarea = null; // Code editor textarea
let currentQuestionData = null; // Store current question data including answer
let isAnswerVisible = false; // Track answer visibility
let currentLevelQuestions = []; // Store all questions in current level
let currentQuestionIndex = -1; // Track current question index in level

// 代码编辑器配置
const CODE_INDENT_SIZE = 4; // 缩进空格数

// 页面加载时初始化
document.addEventListener('DOMContentLoaded', function() {
    loadUsername();
    loadLevels();
    loadProgress();
});

// 加载用户名
function loadUsername() {
    const savedUsername = localStorage.getItem('username') || 'guest';
    currentUsername = savedUsername;
    document.getElementById('username-display').textContent = `学习者: ${currentUsername}`;
    
    // 设置到服务器
    fetch('/set_username', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: currentUsername })
    });
}

// 更改用户名
function changeUsername() {
    const newUsername = prompt('请输入您的用户名：', currentUsername);
    if (newUsername && newUsername.trim()) {
        currentUsername = newUsername.trim();
        localStorage.setItem('username', currentUsername);
        document.getElementById('username-display').textContent = `学习者: ${currentUsername}`;
        
        // 更新到服务器
        fetch('/set_username', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username: currentUsername })
        }).then(() => {
            // 重新加载数据
            loadProgress();
            if (document.getElementById('wrong-questions-tab').classList.contains('active')) {
                loadWrongQuestions();
            }
        });
    }
}

// 切换标签页
function showTab(tabName, event) {
    // 隐藏所有标签页内容
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // 移除所有按钮的激活状态
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // 显示选中的标签页
    document.getElementById(tabName + '-tab').classList.add('active');
    
    // 激活对应的按钮
    if (event && event.target) {
        event.target.classList.add('active');
    }
    
    // 加载对应的数据
    if (tabName === 'wrong-questions') {
        loadWrongQuestions();
    } else if (tabName === 'progress') {
        loadProgress();
    }
}

// 加载关卡列表
function loadLevels() {
    fetch('/levels')
        .then(response => response.json())
        .then(levels => {
            const container = document.getElementById('levels-container');
            container.innerHTML = '';
            
            levels.forEach(level => {
                const card = document.createElement('div');
                card.className = 'level-card';
                card.onclick = () => openLevel(level.id);
                
                card.innerHTML = `
                    <span class="question-count">${level.question_count} 题</span>
                    <h3>${level.title}</h3>
                    <p>${level.description}</p>
                    <span class="level-category category-${level.category}">${level.category}</span>
                `;
                
                container.appendChild(card);
            });
        })
        .catch(error => {
            console.error('加载关卡失败:', error);
            document.getElementById('levels-container').innerHTML = '<p class="hint">加载失败，请刷新页面重试</p>';
        });
}

// 打开关卡
function openLevel(levelId) {
    currentLevelId = levelId;
    
    fetch(`/level/${levelId}`)
        .then(response => response.json())
        .then(level => {
            // Store all questions in current level
            currentLevelQuestions = level.questions;
            
            document.getElementById('level-title').textContent = level.title;
            document.getElementById('level-description').textContent = level.description;
            
            const questionsList = document.getElementById('questions-list');
            questionsList.innerHTML = '';
            
            level.questions.forEach((question, index) => {
                const questionItem = document.createElement('div');
                questionItem.className = 'question-item';
                
                // 标记最后访问的题目
                if (level.last_question_id && question.id === level.last_question_id) {
                    questionItem.classList.add('last-attempted');
                }
                
                questionItem.onclick = () => openQuestion(question.id);
                
                const typeNames = {
                    'choice': '选择题',
                    'fill': '填空题',
                    'code': '编程题'
                };
                
                // 添加最后访问的提示
                const lastAttemptedBadge = (level.last_question_id && question.id === level.last_question_id) 
                    ? '<span class="last-attempted-badge">📍 上次做到这里</span>' 
                    : '';
                
                questionItem.innerHTML = `
                    <span>
                        <strong>${index + 1}.</strong> ${question.title}
                        ${lastAttemptedBadge}
                    </span>
                    <span class="question-type-badge type-${question.type}">
                        ${typeNames[question.type]}
                    </span>
                `;
                
                questionsList.appendChild(questionItem);
            });
            
            document.getElementById('level-modal').style.display = 'block';
            
            // 如果有最后访问的题目，自动打开它
            // 延迟一小段时间，让用户看到关卡列表
            if (level.last_question_id) {
                setTimeout(() => {
                    // 只在关卡模态框仍然打开时才自动打开题目
                    if (document.getElementById('level-modal').style.display === 'block') {
                        openQuestion(level.last_question_id);
                    }
                }, 1500);
            }
        })
        .catch(error => {
            console.error('加载关卡详情失败:', error);
            alert('加载失败，请重试');
        });
}

// 关闭关卡模态框
function closeLevelModal() {
    document.getElementById('level-modal').style.display = 'none';
}

// 打开题目
function openQuestion(questionId) {
    currentQuestionId = questionId;
    isAnswerVisible = false; // Reset answer visibility
    
    // Find the index of current question in the level
    currentQuestionIndex = currentLevelQuestions.findIndex(q => q.id === questionId);
    
    // 更新用户在关卡中的位置
    fetch('/update_question_position', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question_id: questionId })
    }).catch(error => {
        console.error('更新题目位置失败:', error);
    });
    
    // 确保关闭关卡模态框（当从错题本打开题目时）
    closeLevelModal();
    
    fetch(`/question/${questionId}`)
        .then(response => response.json())
        .then(question => {
            currentQuestionData = question; // Store question data
            
            document.getElementById('question-title').textContent = question.title;
            document.getElementById('question-content').innerHTML = `<p>${question.content}</p>`;
            
            const optionsArea = document.getElementById('question-options');
            const answerArea = document.getElementById('answer-input-area');
            const codeEditorContainer = document.getElementById('code-editor-container');
            const codeOutput = document.getElementById('code-output');
            const answerDisplayArea = document.getElementById('answer-area');
            
            optionsArea.innerHTML = '';
            answerArea.innerHTML = '';
            codeEditorContainer.style.display = 'none';
            codeOutput.style.display = 'none';
            document.getElementById('result-area').style.display = 'none';
            answerDisplayArea.style.display = 'none';
            document.getElementById('answer-toggle-text').textContent = '显示答案';
            
            codeTextarea = null;
            
            if (question.type === 'choice') {
                // 选择题
                question.options.forEach((option, index) => {
                    const optionDiv = document.createElement('div');
                    optionDiv.className = 'option';
                    optionDiv.textContent = option;
                    optionDiv.onclick = function() {
                        // 移除其他选项的选中状态
                        document.querySelectorAll('.option').forEach(opt => {
                            opt.classList.remove('selected');
                        });
                        // 选中当前选项
                        this.classList.add('selected');
                    };
                    optionsArea.appendChild(optionDiv);
                });
            } else if (question.type === 'fill') {
                // 填空题 - 使用代码编辑器样式的 textarea
                answerArea.innerHTML = '<textarea id="fill-answer" class="code-editor-textarea" placeholder="# 在这里输入您的答案\n" rows="5" spellcheck="false"></textarea>';
                
                // 保存引用
                codeTextarea = document.getElementById('fill-answer');
                
                // 支持 Tab 键缩进
                codeTextarea.addEventListener('keydown', function(e) {
                    if (e.key === 'Tab') {
                        e.preventDefault();
                        const start = this.selectionStart;
                        const end = this.selectionEnd;
                        
                        // 插入配置的缩进空格
                        const indent = ' '.repeat(CODE_INDENT_SIZE);
                        this.value = this.value.substring(0, start) + indent + this.value.substring(end);
                        
                        // 将光标移到插入的空格后
                        this.selectionStart = this.selectionEnd = start + CODE_INDENT_SIZE;
                    }
                });
            } else if (question.type === 'code') {
                // 编程题 - 使用增强的 textarea
                answerArea.innerHTML = '<textarea id="code-answer" class="code-editor-textarea" placeholder="# 在这里编写您的 Python 代码\n" rows="15" spellcheck="false"></textarea>';
                codeEditorContainer.style.display = 'block';
                
                // 保存引用
                codeTextarea = document.getElementById('code-answer');
                
                // 支持 Tab 键缩进
                codeTextarea.addEventListener('keydown', function(e) {
                    if (e.key === 'Tab') {
                        e.preventDefault();
                        const start = this.selectionStart;
                        const end = this.selectionEnd;
                        
                        // 插入配置的缩进空格
                        const indent = ' '.repeat(CODE_INDENT_SIZE);
                        this.value = this.value.substring(0, start) + indent + this.value.substring(end);
                        
                        // 将光标移到插入的空格后
                        this.selectionStart = this.selectionEnd = start + CODE_INDENT_SIZE;
                    }
                });
            }
            
            document.getElementById('question-modal').style.display = 'block';
        })
        .catch(error => {
            console.error('加载题目失败:', error);
            alert('加载失败，请重试');
        });
}

// 关闭题目模态框
function closeQuestionModal() {
    document.getElementById('question-modal').style.display = 'none';
}

// 提交答案
function submitAnswer() {
    let answer = '';
    
    // 根据题目类型获取答案
    const selectedOption = document.querySelector('.option.selected');
    if (selectedOption) {
        // 选择题 - 获取选项的第一个字符（A, B, C, D）
        answer = selectedOption.textContent.trim().charAt(0);
    } else if (codeTextarea) {
        // 从 textarea 获取代码（包括填空题和编程题）
        answer = codeTextarea.value.trim();
    }
    
    if (!answer) {
        alert('请先选择或填写答案！');
        return;
    }
    
    // 提交到服务器
    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            question_id: currentQuestionId,
            answer: answer
        })
    })
    .then(response => response.json())
    .then(result => {
        const resultArea = document.getElementById('result-area');
        resultArea.style.display = 'block';
        
        // Check if there's a next question
        const hasNextQuestion = currentLevelQuestions && 
                               currentLevelQuestions.length > 0 &&
                               currentQuestionIndex >= 0 && 
                               currentQuestionIndex < currentLevelQuestions.length - 1;
        
        // Create next question button HTML if there's a next question
        const nextQuestionBtn = hasNextQuestion 
            ? '<button class="btn btn-primary" onclick="goToNextQuestion()" style="margin-top: 15px;">下一题 →</button>'
            : '<p class="hint" style="margin-top: 15px;">🎉 恭喜！你已完成本关卡所有题目</p>';
        
        if (result.correct) {
            resultArea.className = 'result correct';
            resultArea.innerHTML = `
                <h3>✅ 回答正确！</h3>
                <p>${result.explanation || '继续加油！'}</p>
                ${nextQuestionBtn}
            `;
        } else {
            resultArea.className = 'result wrong';
            resultArea.innerHTML = `
                <h3>❌ 回答错误</h3>
                <p><strong>正确答案：</strong>${result.answer}</p>
                <p>${result.explanation || ''}</p>
                <p class="hint">题目已添加到错题本，可以稍后复习</p>
                ${nextQuestionBtn}
            `;
        }
        
        // 更新进度
        loadProgress();
    })
    .catch(error => {
        console.error('提交答案失败:', error);
        alert('提交失败，请重试');
    });
}

// 切换答案显示
function toggleAnswer() {
    if (!currentQuestionData) {
        alert('请先加载题目！');
        return;
    }
    
    const answerArea = document.getElementById('answer-area');
    const toggleText = document.getElementById('answer-toggle-text');
    
    isAnswerVisible = !isAnswerVisible;
    
    if (isAnswerVisible) {
        // 显示答案
        const answerContent = document.getElementById('answer-content');
        const answer = currentQuestionData.answer || '暂无答案';
        
        // 对于代码类型的题目，使用语法高亮
        if (currentQuestionData.type === 'code' || currentQuestionData.type === 'fill') {
            answerContent.innerHTML = `<pre><code class="language-python">${escapeHtml(answer)}</code></pre>`;
            // 应用语法高亮
            if (typeof hljs !== 'undefined') {
                hljs.highlightElement(answerContent.querySelector('code'));
            }
        } else {
            answerContent.textContent = answer;
        }
        
        document.getElementById('answer-explanation').textContent = currentQuestionData.explanation || '暂无解析';
        answerArea.style.display = 'block';
        toggleText.textContent = '隐藏答案';
    } else {
        // 隐藏答案
        answerArea.style.display = 'none';
        toggleText.textContent = '显示答案';
    }
}

// HTML 转义函数
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// 加载学习进度
function loadProgress() {
    fetch('/progress')
        .then(response => response.json())
        .then(progress => {
            const percentage = progress.percentage || 0;
            document.getElementById('overall-progress').style.width = percentage + '%';
            document.getElementById('progress-text').textContent = `已完成 ${percentage}%`;
            
            // 更新统计页面
            document.getElementById('total-questions').textContent = progress.total;
            document.getElementById('completed-questions').textContent = progress.completed;
            document.getElementById('completion-rate').textContent = percentage + '%';
        })
        .catch(error => {
            console.error('加载进度失败:', error);
        });
}

// 加载错题本
function loadWrongQuestions() {
    fetch('/wrong_questions')
        .then(response => response.json())
        .then(wrongQuestions => {
            const container = document.getElementById('wrong-questions-list');
            
            if (wrongQuestions.length === 0) {
                container.innerHTML = '<p class="hint">太棒了！你还没有错题。继续保持！</p>';
                return;
            }
            
            container.innerHTML = '';
            
            wrongQuestions.forEach(wq => {
                const card = document.createElement('div');
                card.className = 'wrong-question-card';
                card.onclick = () => openQuestion(wq.question_id);
                
                card.innerHTML = `
                    <h4>${wq.question}</h4>
                    <p>
                        <small>错误次数：</small>
                        <span class="wrong-count">错了 ${wq.wrong_count} 次</span>
                    </p>
                    <p><small>添加日期：${wq.added_date}</small></p>
                    ${wq.notes ? `<p class="hint">${wq.notes}</p>` : ''}
                `;
                
                container.appendChild(card);
            });
        })
        .catch(error => {
            console.error('加载错题本失败:', error);
            document.getElementById('wrong-questions-list').innerHTML = '<p class="hint">加载失败，请刷新页面重试</p>';
        });
}

// 点击模态框外部关闭
window.onclick = function(event) {
    const levelModal = document.getElementById('level-modal');
    const questionModal = document.getElementById('question-modal');
    
    if (event.target === levelModal) {
        levelModal.style.display = 'none';
    }
    if (event.target === questionModal) {
        questionModal.style.display = 'none';
    }
}

// 运行代码
function runCode() {
    if (!codeTextarea) {
        alert('请先打开编程题！');
        return;
    }
    
    const code = codeTextarea.value.trim();
    if (!code) {
        alert('请先输入代码！');
        return;
    }
    
    // 显示输出区域
    const outputDiv = document.getElementById('code-output');
    const outputContent = document.getElementById('output-content');
    outputDiv.style.display = 'block';
    outputContent.textContent = '正在运行...';
    outputContent.style.color = '#f8f8f8';
    
    // 发送代码到服务器执行
    fetch('/run_code', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            outputContent.textContent = result.output || '(无输出)';
            outputContent.style.color = '#f8f8f8';
        } else {
            outputContent.textContent = `错误:\n${result.error}`;
            outputContent.style.color = '#ff6b6b';
        }
    })
    .catch(error => {
        outputContent.textContent = `运行失败: ${error.message}`;
        outputContent.style.color = '#ff6b6b';
    });
}

// 跳转到下一题
function goToNextQuestion() {
    if (currentLevelQuestions && 
        currentLevelQuestions.length > 0 &&
        currentQuestionIndex >= 0 && 
        currentQuestionIndex < currentLevelQuestions.length - 1) {
        const nextQuestion = currentLevelQuestions[currentQuestionIndex + 1];
        openQuestion(nextQuestion.id);
    }
}
