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

// 自动打开最后访问题目的延迟时间（毫秒）
const AUTO_RESUME_DELAY_MS = 1500;

// 自动跳转下一题的延迟时间（毫秒）
const AUTO_ADVANCE_DELAY_MS = 1500;

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
            const container = document.getElementById('levels-view');
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
            document.getElementById('levels-view').innerHTML = '<p class="hint">加载失败，请刷新页面重试</p>';
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
            
            // Switch to level detail view
            document.getElementById('levels-view').style.display = 'none';
            document.getElementById('level-detail-view').style.display = 'block';
            
            // 如果有最后访问的题目，自动打开它，否则打开第一题
            const questionToOpen = level.last_question_id || 
                                   (level.questions.length > 0 && level.questions[0] && level.questions[0].id ? 
                                    level.questions[0].id : null);
            if (questionToOpen) {
                // Small delay to let the UI settle
                setTimeout(() => {
                    openQuestion(questionToOpen);
                }, 100);
            }
        })
        .catch(error => {
            console.error('加载关卡详情失败:', error);
            alert('加载失败，请重试');
        });
}

// 返回关卡列表
function backToLevels() {
    document.getElementById('level-detail-view').style.display = 'none';
    document.getElementById('levels-view').style.display = 'block';
    currentLevelId = null;
    currentQuestionId = null;
    currentLevelQuestions = [];
    currentQuestionIndex = -1;
}

// 关闭关卡模态框
function closeLevelModal() {
    // No longer used - keeping for compatibility
}

// 打开题目
function openQuestion(questionId) {
    currentQuestionId = questionId;
    isAnswerVisible = false; // Reset answer visibility
    
    // Find the index of current question in the level
    currentQuestionIndex = currentLevelQuestions.findIndex(q => q.id === questionId);
    
    // Update active state in question list
    document.querySelectorAll('.question-item').forEach(item => {
        item.classList.remove('active');
    });
    if (currentQuestionIndex >= 0) {
        const questionItems = document.querySelectorAll('.question-item');
        if (questionItems.length > currentQuestionIndex) {
            questionItems[currentQuestionIndex].classList.add('active');
        }
    }
    
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
    
    fetch(`/question/${questionId}`)
        .then(response => response.json())
        .then(question => {
            currentQuestionData = question; // Store question data
            
            // Build question detail HTML
            let questionHTML = `
                <h2>${question.title}</h2>
                <div class="question-content">
                    <p>${question.content}</p>
                </div>
            `;
            
            // Add question-specific interface based on type
            if (question.type === 'choice') {
                questionHTML += '<div id="question-options" class="question-options">';
                question.options.forEach((option, index) => {
                    questionHTML += `
                        <div class="option" onclick="selectOption(this)">
                            ${option}
                        </div>
                    `;
                });
                questionHTML += '</div>';
            } else if (question.type === 'fill') {
                questionHTML += `
                    <div class="answer-input-area">
                        <textarea id="fill-answer" class="code-editor-textarea" placeholder="# 在这里输入您的答案\n" rows="5" spellcheck="false"></textarea>
                    </div>
                `;
            } else if (question.type === 'code') {
                questionHTML += `
                    <div class="answer-input-area">
                        <textarea id="code-answer" class="code-editor-textarea" placeholder="# 在这里编写您的 Python 代码\n" rows="15" spellcheck="false"></textarea>
                    </div>
                    <div class="code-editor-toolbar">
                        <button class="btn btn-run" onclick="runCode()">▶ 运行代码</button>
                        <span class="security-warning">⚠️ 代码将在服务器端运行，请勿执行恶意代码</span>
                    </div>
                    <div id="code-output" class="code-output" style="display: none;">
                        <div class="output-header">输出结果：</div>
                        <pre id="output-content"></pre>
                    </div>
                `;
            }
            
            // Add button group
            questionHTML += `
                <div class="button-group">
                    <button class="btn btn-secondary" onclick="toggleAnswer()">
                        <span id="answer-toggle-text">显示答案</span>
                    </button>
                    <button class="btn btn-primary" onclick="submitAnswer()">提交答案</button>
                </div>
                <div id="answer-area" class="answer-area" style="display: none;">
                    <h3>📝 参考答案</h3>
                    <div id="answer-content"></div>
                    <h3>💡 解析</h3>
                    <div id="answer-explanation"></div>
                </div>
                <div id="result-area" style="display: none;"></div>
            `;
            
            // Update the question detail area
            document.getElementById('question-detail-content').innerHTML = questionHTML;
            
            // Setup code editor if needed
            codeTextarea = null;
            if (question.type === 'fill' || question.type === 'code') {
                const textareaId = question.type === 'fill' ? 'fill-answer' : 'code-answer';
                codeTextarea = document.getElementById(textareaId);
                
                if (codeTextarea) {
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
            }
        })
        .catch(error => {
            console.error('加载题目失败:', error);
            alert('加载失败，请重试');
        });
}

// 选择选项
function selectOption(element) {
    // 移除其他选项的选中状态
    document.querySelectorAll('.option').forEach(opt => {
        opt.classList.remove('selected');
    });
    // 选中当前选项
    element.classList.add('selected');
}

// 关闭题目模态框
function closeQuestionModal() {
    // No longer used - keeping for compatibility
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
        
        if (result.correct) {
            resultArea.className = 'result correct';
            resultArea.innerHTML = `
                <h3>✅ 回答正确！</h3>
                <p>${result.explanation || '继续加油！'}</p>
            `;
            
            // Auto-advance to next question after a short delay
            if (hasNextQuestion) {
                resultArea.innerHTML += '<p class="hint">正在跳转到下一题...</p>';
                setTimeout(() => {
                    goToNextQuestion();
                }, AUTO_ADVANCE_DELAY_MS);
            } else {
                resultArea.innerHTML += '<p class="hint">🎉 恭喜！你已完成本关卡所有题目</p>';
            }
        } else {
            // Create manual next question button for wrong answers
            const nextQuestionBtn = hasNextQuestion 
                ? '<button class="btn btn-primary" onclick="goToNextQuestion()" style="margin-top: 15px;">下一题 →</button>'
                : '<p class="hint" style="margin-top: 15px;">🎉 恭喜！你已完成本关卡所有题目</p>';
            
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
                card.onclick = () => openQuestionFromWrongBook(wq.question_id);
                
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

// 从错题本打开题目 - 需要先加载关卡信息
function openQuestionFromWrongBook(questionId) {
    // First get the question to find its level
    fetch(`/question/${questionId}`)
        .then(response => response.json())
        .then(question => {
            // Get level info from question
            fetch(`/level/${question.level_id}`)
                .then(response => response.json())
                .then(level => {
                    // Switch to levels tab - select the specific levels tab button
                    const levelsTabBtn = document.querySelector('.tab-btn');
                    if (levelsTabBtn) {
                        showTab('levels', { target: levelsTabBtn });
                    }
                    
                    // Open the level
                    openLevel(level.id);
                    
                    // After a short delay, open the specific question
                    setTimeout(() => {
                        openQuestion(questionId);
                    }, 200);
                });
        })
        .catch(error => {
            console.error('从错题本打开题目失败:', error);
            alert('加载失败，请重试');
        });
}

// 点击模态框外部关闭 - no longer used but keeping for compatibility
window.onclick = function(event) {
    // Modals have been removed - this is kept for backward compatibility
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
