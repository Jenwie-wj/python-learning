"""
初始化关卡和题目数据
包含从基础到高级的 Python 学习内容，侧重软件测试
"""

import json

# 数据库版本信息 - 当添加新题目或关卡时，请更新这些数字
EXPECTED_LEVEL_COUNT = 21
EXPECTED_QUESTION_COUNT = 118

def initialize_levels_and_questions(db, Level, Question):
    """初始化关卡和题目"""
    
    # 第一关：Python 基础 - 变量和数据类型
    level1 = Level(
        title="第一关：变量和数据类型",
        description="学习 Python 的基本变量和数据类型，为后续测试编程打下基础",
        order=1,
        category="基础"
    )
    db.session.add(level1)
    db.session.commit()
    
    questions_level1 = [
        Question(
            level_id=level1.id,
            question_type="choice",
            title="选择题：下列哪个是 Python 的正确变量名？",
            content="在 Python 中，变量名有一定的命名规则。请选择正确的变量名：",
            options=json.dumps(["A. 1test", "B. test_1", "C. test-1", "D. test 1"]),
            answer="B",
            explanation="Python 变量名必须以字母或下划线开头，不能以数字开头，不能包含特殊字符（除了下划线），不能包含空格。",
            order=1
        ),
        Question(
            level_id=level1.id,
            question_type="fill",
            title="填空题：数据类型判断",
            content="在 Python 中，可以使用 ______ 函数来获取变量的数据类型。",
            options=None,
            answer="type",
            explanation="type() 函数用于返回对象的类型。例如：type(10) 返回 <class 'int'>",
            order=2
        ),
        Question(
            level_id=level1.id,
            question_type="code",
            title="编程题：创建变量",
            content="请创建一个字符串变量 name，值为 'Python测试工程师'，并打印它的类型和值。",
            options=None,
            answer="name = 'Python测试工程师'\nprint(type(name))\nprint(name)",
            explanation="使用引号创建字符串，type() 查看类型，print() 打印结果。",
            order=3
        ),
        Question(
            level_id=level1.id,
            question_type="choice",
            title="选择题：整数和浮点数",
            content="在 Python 中，以下哪个表达式的结果是浮点数类型？",
            options=json.dumps(["A. 10 + 5", "B. 10 / 2", "C. 10 // 2", "D. 10 % 2"]),
            answer="B",
            explanation="在 Python 3 中，使用 / 运算符进行除法运算总是返回浮点数，即使结果是整数。// 是整数除法，% 是取余运算。",
            order=4
        ),
        Question(
            level_id=level1.id,
            question_type="fill",
            title="填空题：类型转换",
            content="将字符串 '123' 转换为整数，应该使用 ______ 函数。",
            options=None,
            answer="int",
            explanation="int() 函数可以将字符串或浮点数转换为整数类型。例如：int('123') 返回 123",
            order=5
        ),
        Question(
            level_id=level1.id,
            question_type="code",
            title="编程题：布尔类型",
            content="创建两个布尔变量 is_passed（值为 True）和 is_failed（值为 False），并打印它们。",
            options=None,
            answer="is_passed = True\nis_failed = False\nprint(is_passed)\nprint(is_failed)",
            explanation="布尔类型只有 True 和 False 两个值，注意首字母大写。",
            order=6
        ),
        Question(
            level_id=level1.id,
            question_type="choice",
            title="选择题：运算符优先级",
            content="在 Python 中，以下表达式的结果是什么？2 + 3 * 4",
            options=json.dumps(["A. 20", "B. 14", "C. 12", "D. 24"]),
            answer="B",
            explanation="乘法运算符的优先级高于加法运算符，所以先计算 3 * 4 = 12，然后 2 + 12 = 14。",
            order=7
        ),
        Question(
            level_id=level1.id,
            question_type="fill",
            title="填空题：注释的作用",
            content="在 Python 中，使用 ______ 符号可以添加单行注释。",
            options=None,
            answer="#",
            explanation="# 符号用于添加单行注释，Python 解释器会忽略 # 后面的内容。多行注释可以使用三引号 '''...''' 或 \"\"\"...\"\"\"。",
            order=8
        )
    ]
    
    for q in questions_level1:
        db.session.add(q)
    
    # 第二关：控制流程
    level2 = Level(
        title="第二关：条件判断与循环",
        description="掌握 if-else 条件判断和 for、while 循环，这是编写测试逻辑的基础",
        order=2,
        category="基础"
    )
    db.session.add(level2)
    db.session.commit()
    
    questions_level2 = [
        Question(
            level_id=level2.id,
            question_type="choice",
            title="选择题：条件判断",
            content="以下哪个关键字用于在 Python 中表示'否则'的条件？",
            options=json.dumps(["A. elif", "B. else", "C. otherwise", "D. then"]),
            answer="B",
            explanation="在 Python 中，else 用于表示所有条件都不满足时执行的代码块。",
            order=1
        ),
        Question(
            level_id=level2.id,
            question_type="code",
            title="编程题：判断测试结果",
            content="编写一个函数 check_test_result(score)，如果分数大于等于60返回'通过'，否则返回'失败'。",
            options=None,
            answer="def check_test_result(score):\n    if score >= 60:\n        return '通过'\n    else:\n        return '失败'",
            explanation="使用 if-else 语句进行条件判断，这在测试中经常用于判断测试用例是否通过。",
            order=2
        ),
        Question(
            level_id=level2.id,
            question_type="code",
            title="编程题：循环遍历测试数据",
            content="使用 for 循环遍历列表 [1, 2, 3, 4, 5]，打印每个数字的平方。",
            options=None,
            answer="numbers = [1, 2, 3, 4, 5]\nfor num in numbers:\n    print(num ** 2)",
            explanation="for 循环用于遍历序列，在测试中常用于批量处理测试数据。",
            order=3
        ),
        Question(
            level_id=level2.id,
            question_type="fill",
            title="填空题：elif 的使用",
            content="在多个条件判断中，if 和 else 之间使用 ______ 关键字添加更多条件。",
            options=None,
            answer="elif",
            explanation="elif 是 else if 的缩写，用于添加多个条件分支。",
            order=4
        ),
        Question(
            level_id=level2.id,
            question_type="choice",
            title="选择题：while 循环",
            content="以下关于 while 循环的说法，哪个是正确的？",
            options=json.dumps(["A. while 循环会执行固定次数", "B. while 循环在条件为 True 时持续执行", "C. while 循环不能使用 break", "D. while 循环必须有 else"]),
            answer="B",
            explanation="while 循环会在条件为 True 时持续执行，直到条件变为 False 或遇到 break 语句。",
            order=5
        ),
        Question(
            level_id=level2.id,
            question_type="code",
            title="编程题：range 函数",
            content="使用 for 循环和 range() 函数打印 1 到 10 的所有偶数。",
            options=None,
            answer="for i in range(2, 11, 2):\n    print(i)",
            explanation="range(start, stop, step) 可以生成指定范围和步长的数字序列。range(2, 11, 2) 会生成 2, 4, 6, 8, 10。",
            order=6
        ),
        Question(
            level_id=level2.id,
            question_type="choice",
            title="选择题：逻辑运算符",
            content="表达式 True and False or True 的结果是什么？",
            options=json.dumps(["A. True", "B. False", "C. 报错", "D. None"]),
            answer="A",
            explanation="逻辑运算符的优先级：not > and > or。先计算 True and False = False，再计算 False or True = True。",
            order=7
        ),
        Question(
            level_id=level2.id,
            question_type="code",
            title="编程题：多条件判断",
            content="编写判断：如果分数大于等于90输出'优秀'，大于等于80输出'良好'，大于等于60输出'及格'，否则输出'不及格'。变量名为 score。",
            options=None,
            answer="if score >= 90:\n    print('优秀')\nelif score >= 80:\n    print('良好')\nelif score >= 60:\n    print('及格')\nelse:\n    print('不及格')",
            explanation="使用多个 elif 可以处理多种情况，在测试中常用于根据不同条件执行不同的验证逻辑。",
            order=8
        )
    ]
    
    for q in questions_level2:
        db.session.add(q)
    
    # 第三关：函数和模块
    level3 = Level(
        title="第三关：函数和模块",
        description="学习如何定义和使用函数，以及导入模块，为编写测试工具做准备",
        order=3,
        category="基础"
    )
    db.session.add(level3)
    db.session.commit()
    
    questions_level3 = [
        Question(
            level_id=level3.id,
            question_type="choice",
            title="选择题：函数定义",
            content="在 Python 中，定义函数使用哪个关键字？",
            options=json.dumps(["A. function", "B. def", "C. func", "D. define"]),
            answer="B",
            explanation="Python 使用 def 关键字定义函数。",
            order=1
        ),
        Question(
            level_id=level3.id,
            question_type="fill",
            title="填空题：导入模块",
            content="如果要导入 Python 的随机数模块，应该使用 ______ random",
            options=None,
            answer="import",
            explanation="使用 import 关键字导入模块，例如：import random",
            order=2
        ),
        Question(
            level_id=level3.id,
            question_type="code",
            title="编程题：创建数据生成函数",
            content="创建一个函数 generate_test_user(name, age)，返回一个包含用户信息的字典。",
            options=None,
            answer="def generate_test_user(name, age):\n    return {'name': name, 'age': age}",
            explanation="函数可以返回字典，这在测试中常用于生成测试数据。",
            order=3
        ),
        Question(
            level_id=level3.id,
            question_type="choice",
            title="选择题：函数返回值",
            content="如果函数没有 return 语句，它会返回什么？",
            options=json.dumps(["A. 0", "B. None", "C. False", "D. 空字符串"]),
            answer="B",
            explanation="没有 return 语句的函数会默认返回 None。",
            order=4
        ),
        Question(
            level_id=level3.id,
            question_type="fill",
            title="填空题：函数参数",
            content="在函数定义中，设置参数默认值可以创建 ______ 参数。",
            options=None,
            answer="可选|默认",
            explanation="带有默认值的参数是可选参数，调用时可以不传该参数。",
            order=5
        ),
        Question(
            level_id=level3.id,
            question_type="code",
            title="编程题：带默认参数的函数",
            content="创建一个函数 run_test(test_name, retry=3)，打印测试名称和重试次数。",
            options=None,
            answer="def run_test(test_name, retry=3):\n    print(f'测试: {test_name}, 重试次数: {retry}')",
            explanation="使用默认参数可以让函数更灵活，调用时可以选择性地提供参数值。",
            order=6
        ),
        Question(
            level_id=level3.id,
            question_type="choice",
            title="选择题：Lambda 函数",
            content="以下哪个是正确的 lambda 函数定义？",
            options=json.dumps(["A. lambda x: x * 2", "B. def lambda x: x * 2", "C. lambda(x): x * 2", "D. x => x * 2"]),
            answer="A",
            explanation="lambda 函数的语法是：lambda 参数: 表达式。它是一种匿名函数，常用于简单的一次性函数。",
            order=7
        ),
        Question(
            level_id=level3.id,
            question_type="code",
            title="编程题：使用 Lambda 函数",
            content="使用 lambda 函数和 map() 将列表 [1, 2, 3, 4] 中的每个数字乘以 2，并转换为列表输出。",
            options=None,
            answer="numbers = [1, 2, 3, 4]\nresult = list(map(lambda x: x * 2, numbers))\nprint(result)",
            explanation="lambda 函数经常与 map()、filter() 等高阶函数配合使用，可以使代码更简洁。",
            order=8
        )
    ]
    
    for q in questions_level3:
        db.session.add(q)
    
    # 第四关：文件操作
    level4 = Level(
        title="第四关：文件读写操作",
        description="学习文件的读写操作，为数据迁移和测试数据管理打下基础",
        order=4,
        category="工具"
    )
    db.session.add(level4)
    db.session.commit()
    
    questions_level4 = [
        Question(
            level_id=level4.id,
            question_type="choice",
            title="选择题：文件打开模式",
            content="以下哪个模式用于以追加方式打开文件？",
            options=json.dumps(["A. 'r'", "B. 'w'", "C. 'a'", "D. 'x'"]),
            answer="C",
            explanation="'a' 模式用于追加内容到文件末尾，'r' 是读取，'w' 是写入（覆盖），'x' 是创建新文件。",
            order=1
        ),
        Question(
            level_id=level4.id,
            question_type="code",
            title="编程题：写入测试日志",
            content="编写代码将字符串 'Test passed' 写入到 test_log.txt 文件中。",
            options=None,
            answer="with open('test_log.txt', 'w') as f:\n    f.write('Test passed')",
            explanation="使用 with 语句可以自动关闭文件，这是文件操作的最佳实践。",
            order=2
        ),
        Question(
            level_id=level4.id,
            question_type="code",
            title="编程题：读取配置文件",
            content="编写代码读取 config.txt 文件的所有内容并打印。",
            options=None,
            answer="with open('config.txt', 'r') as f:\n    content = f.read()\n    print(content)",
            explanation="使用 read() 方法读取文件全部内容，在测试中常用于读取配置文件。",
            order=3
        ),
        Question(
            level_id=level4.id,
            question_type="fill",
            title="填空题：文件读取方法",
            content="要逐行读取文件内容，可以使用 ______ 方法。",
            options=None,
            answer="readlines|readline",
            explanation="readlines() 读取所有行返回列表，readline() 每次读取一行。",
            order=4
        ),
        Question(
            level_id=level4.id,
            question_type="choice",
            title="选择题：with 语句的作用",
            content="使用 with 语句打开文件的主要好处是什么？",
            options=json.dumps(["A. 文件读取更快", "B. 自动关闭文件", "C. 支持更多文件格式", "D. 可以同时打开多个文件"]),
            answer="B",
            explanation="with 语句会在代码块结束后自动关闭文件，即使发生异常也能确保文件被关闭。",
            order=5
        )
    ]
    
    for q in questions_level4:
        db.session.add(q)
    
    # 第五关：异常处理
    level5 = Level(
        title="第五关：异常处理",
        description="学习如何处理程序异常，让测试代码更加健壮",
        order=5,
        category="基础"
    )
    db.session.add(level5)
    db.session.commit()
    
    questions_level5 = [
        Question(
            level_id=level5.id,
            question_type="choice",
            title="选择题：异常捕获",
            content="在 Python 中，捕获异常使用哪个关键字组合？",
            options=json.dumps(["A. try-catch", "B. try-except", "C. catch-throw", "D. error-handle"]),
            answer="B",
            explanation="Python 使用 try-except 来捕获和处理异常。",
            order=1
        ),
        Question(
            level_id=level5.id,
            question_type="code",
            title="编程题：安全的类型转换",
            content="编写一个函数 safe_int_convert(value)，尝试将参数转换为整数，如果失败返回 None。",
            options=None,
            answer="def safe_int_convert(value):\n    try:\n        return int(value)\n    except ValueError:\n        return None",
            explanation="使用 try-except 捕获 ValueError，使类型转换更加安全，这在处理测试数据时很重要。",
            order=2
        ),
        Question(
            level_id=level5.id,
            question_type="fill",
            title="填空题：finally 块",
            content="在 try-except 结构中，无论是否发生异常都会执行的代码块使用 ______ 关键字。",
            options=None,
            answer="finally",
            explanation="finally 块中的代码无论是否发生异常都会执行，常用于清理资源。",
            order=3
        ),
        Question(
            level_id=level5.id,
            question_type="choice",
            title="选择题：自定义异常",
            content="要抛出一个异常，使用哪个关键字？",
            options=json.dumps(["A. throw", "B. raise", "C. error", "D. except"]),
            answer="B",
            explanation="Python 使用 raise 关键字抛出异常。",
            order=4
        ),
        Question(
            level_id=level5.id,
            question_type="code",
            title="编程题：完整的异常处理",
            content="编写代码尝试打开并读取文件 'data.txt'，如果文件不存在则打印 '文件未找到'。",
            options=None,
            answer="try:\n    with open('data.txt', 'r') as f:\n        content = f.read()\n        print(content)\nexcept FileNotFoundError:\n    print('文件未找到')",
            explanation="FileNotFoundError 是文件不存在时抛出的异常，在测试中经常需要处理文件操作的异常。",
            order=5
        )
    ]
    
    for q in questions_level5:
        db.session.add(q)
    
    # 第六关：列表和字典操作
    level6 = Level(
        title="第六关：列表、字典、元组和集合",
        description="深入学习 Python 的数据结构：列表、字典、元组和集合，为处理测试数据做准备",
        order=6,
        category="基础"
    )
    db.session.add(level6)
    db.session.commit()
    
    questions_level6 = [
        Question(
            level_id=level6.id,
            question_type="choice",
            title="选择题：列表方法",
            content="下列哪个方法可以在列表末尾添加元素？",
            options=json.dumps(["A. add()", "B. append()", "C. insert()", "D. push()"]),
            answer="B",
            explanation="append() 方法在列表末尾添加元素，insert() 在指定位置插入。",
            order=1
        ),
        Question(
            level_id=level6.id,
            question_type="code",
            title="编程题：批量生成测试数据",
            content="使用列表推导式生成包含 1 到 10 的所有偶数的列表。",
            options=None,
            answer="even_numbers = [x for x in range(1, 11) if x % 2 == 0]",
            explanation="列表推导式是生成列表的简洁方式，在批量生成测试数据时非常有用。",
            order=2
        ),
        Question(
            level_id=level6.id,
            question_type="code",
            title="编程题：合并测试数据",
            content="有两个字典 dict1 = {'a': 1} 和 dict2 = {'b': 2}，将它们合并成一个字典。",
            options=None,
            answer="dict1 = {'a': 1}\ndict2 = {'b': 2}\nmerged = {**dict1, **dict2}",
            explanation="使用字典解包操作符 ** 可以方便地合并字典，这在合并测试配置时很有用。",
            order=3
        ),
        Question(
            level_id=level6.id,
            question_type="fill",
            title="填空题：字典方法",
            content="获取字典所有键的列表，可以使用字典的 ______ 方法。",
            options=None,
            answer="keys",
            explanation="dict.keys() 返回字典所有键的视图对象，可以转换为列表使用。",
            order=4
        ),
        Question(
            level_id=level6.id,
            question_type="choice",
            title="选择题：列表切片",
            content="对于列表 nums = [1, 2, 3, 4, 5]，nums[1:4] 的结果是什么？",
            options=json.dumps(["A. [1, 2, 3]", "B. [2, 3, 4]", "C. [2, 3, 4, 5]", "D. [1, 2, 3, 4]"]),
            answer="B",
            explanation="切片 [start:end] 包含 start 但不包含 end，所以 [1:4] 返回索引 1、2、3 的元素。",
            order=5
        ),
        Question(
            level_id=level6.id,
            question_type="choice",
            title="选择题：元组的特性",
            content="元组（tuple）和列表（list）的主要区别是什么？",
            options=json.dumps(["A. 元组不能包含数字", "B. 元组是不可变的", "C. 元组只能有一个元素", "D. 元组不能被遍历"]),
            answer="B",
            explanation="元组是不可变的序列类型，一旦创建就不能修改。这在需要确保数据不被改变时很有用，比如作为字典的键。",
            order=6
        ),
        Question(
            level_id=level6.id,
            question_type="code",
            title="编程题：使用元组返回多个值",
            content="创建一个函数 get_test_stats()，返回一个元组，包含三个值：测试总数10、通过数8、失败数2。",
            options=None,
            answer="def get_test_stats():\n    return (10, 8, 2)",
            explanation="函数可以使用元组返回多个值，调用时可以解包：total, passed, failed = get_test_stats()",
            order=7
        ),
        Question(
            level_id=level6.id,
            question_type="choice",
            title="选择题：集合的特性",
            content="集合（set）的主要特点是什么？",
            options=json.dumps(["A. 元素有序且可重复", "B. 元素无序且不可重复", "C. 只能包含数字", "D. 可以包含列表"]),
            answer="B",
            explanation="集合（set）是无序的且不包含重复元素的数据结构，常用于去重和集合运算。",
            order=8
        ),
        Question(
            level_id=level6.id,
            question_type="code",
            title="编程题：使用集合去重",
            content="有一个包含重复元素的列表 test_ids = [1, 2, 2, 3, 3, 4]，使用集合去除重复元素并转回列表。",
            options=None,
            answer="test_ids = [1, 2, 2, 3, 3, 4]\nunique_ids = list(set(test_ids))",
            explanation="使用 set() 可以快速去除列表中的重复元素，这在处理测试数据时很实用。",
            order=9
        )
    ]
    
    for q in questions_level6:
        db.session.add(q)
    
    # 第七关：字符串处理
    level7 = Level(
        title="第七关：字符串处理技巧",
        description="掌握字符串的各种处理方法，用于测试数据的格式化和验证",
        order=7,
        category="工具"
    )
    db.session.add(level7)
    db.session.commit()
    
    questions_level7 = [
        Question(
            level_id=level7.id,
            question_type="fill",
            title="填空题：字符串格式化",
            content="在 Python 3.6+ 中，使用 ______ 字符串可以方便地进行格式化，例如 f'Hello {name}'",
            options=None,
            answer="f|f-string|f字符串",
            explanation="f-string 是 Python 3.6+ 引入的字符串格式化方式，语法简洁易读。",
            order=1
        ),
        Question(
            level_id=level7.id,
            question_type="code",
            title="编程题：验证邮箱格式",
            content="编写函数 is_valid_email(email)，简单检查邮箱是否包含 @ 符号，返回 True 或 False。",
            options=None,
            answer="def is_valid_email(email):\n    return '@' in email",
            explanation="这是一个简单的邮箱验证，实际测试中可能需要更复杂的正则表达式验证。",
            order=2
        ),
        Question(
            level_id=level7.id,
            question_type="choice",
            title="选择题：字符串方法",
            content="下列哪个方法可以将字符串转换为大写？",
            options=json.dumps(["A. toUpper()", "B. upper()", "C. uppercase()", "D. Upper()"]),
            answer="B",
            explanation="Python 字符串的 upper() 方法将所有字符转换为大写，lower() 转换为小写。",
            order=3
        ),
        Question(
            level_id=level7.id,
            question_type="fill",
            title="填空题：字符串分割",
            content="将字符串按照指定分隔符分割成列表，使用 ______ 方法。",
            options=None,
            answer="split",
            explanation="split() 方法根据分隔符将字符串分割成列表，在解析测试数据时非常有用。",
            order=4
        ),
        Question(
            level_id=level7.id,
            question_type="code",
            title="编程题：字符串连接",
            content="使用 join() 方法将列表 ['Python', '测试', '工程师'] 连接成一个字符串，用空格分隔。",
            options=None,
            answer="words = ['Python', '测试', '工程师']\nresult = ' '.join(words)\nprint(result)",
            explanation="join() 方法用于将列表中的字符串连接成一个字符串，参数是分隔符。",
            order=5
        )
    ]
    
    for q in questions_level7:
        db.session.add(q)
    
    # 第八关：CSV 数据处理
    level8 = Level(
        title="第八关：CSV 文件处理",
        description="学习读写 CSV 文件，这是测试数据管理的常用技能",
        order=8,
        category="工具"
    )
    db.session.add(level8)
    db.session.commit()
    
    questions_level8 = [
        Question(
            level_id=level8.id,
            question_type="choice",
            title="选择题：CSV 模块",
            content="Python 中处理 CSV 文件最常用的内置模块是？",
            options=json.dumps(["A. csv", "B. excel", "C. file", "D. data"]),
            answer="A",
            explanation="csv 是 Python 的内置模块，专门用于处理 CSV 文件。",
            order=1
        ),
        Question(
            level_id=level8.id,
            question_type="code",
            title="编程题：导出测试数据到 CSV",
            content="使用 csv 模块将列表 [['姓名', '年龄'], ['张三', 25], ['李四', 30]] 写入 users.csv 文件。",
            options=None,
            answer="import csv\ndata = [['姓名', '年龄'], ['张三', 25], ['李四', 30]]\nwith open('users.csv', 'w', newline='', encoding='utf-8') as f:\n    writer = csv.writer(f)\n    writer.writerows(data)",
            explanation="csv.writer 可以方便地将数据写入 CSV 文件，在测试中常用于导出测试报告。",
            order=2
        ),
        Question(
            level_id=level8.id,
            question_type="fill",
            title="填空题：CSV 读取",
            content="使用 csv 模块读取文件时，创建阅读器使用 csv.______ 函数。",
            options=None,
            answer="reader",
            explanation="csv.reader() 创建一个读取器对象，用于逐行读取 CSV 文件。",
            order=3
        ),
        Question(
            level_id=level8.id,
            question_type="choice",
            title="选择题：CSV 字典",
            content="如果要以字典形式读取 CSV 文件（第一行作为键），应使用什么？",
            options=json.dumps(["A. csv.reader", "B. csv.DictReader", "C. csv.dict", "D. csv.map"]),
            answer="B",
            explanation="csv.DictReader 将每行数据转换为字典，第一行作为字典的键，便于按列名访问数据。",
            order=4
        ),
        Question(
            level_id=level8.id,
            question_type="code",
            title="编程题：读取 CSV 文件",
            content="使用 csv 模块读取 CSV 文件 'data.csv' 并打印每一行。",
            options=None,
            answer="import csv\nwith open('data.csv', 'r', encoding='utf-8') as f:\n    reader = csv.reader(f)\n    for row in reader:\n        print(row)",
            explanation="csv.reader 创建读取器对象，可以逐行读取 CSV 文件内容。",
            order=5
        )
    ]
    
    for q in questions_level8:
        db.session.add(q)
    
    # 第九关：JSON 数据处理
    level9 = Level(
        title="第九关：JSON 数据处理",
        description="学习处理 JSON 格式数据，这是 API 测试的基础",
        order=9,
        category="测试"
    )
    db.session.add(level9)
    db.session.commit()
    
    questions_level9 = [
        Question(
            level_id=level9.id,
            question_type="fill",
            title="填空题：JSON 转换",
            content="将 Python 字典转换为 JSON 字符串使用 json.______ 方法",
            options=None,
            answer="dumps",
            explanation="json.dumps() 将 Python 对象转换为 JSON 字符串，json.loads() 则相反。",
            order=1
        ),
        Question(
            level_id=level9.id,
            question_type="code",
            title="编程题：解析 API 响应",
            content="编写代码将 JSON 字符串 '{\"status\": \"success\", \"code\": 200}' 转换为 Python 字典并打印 status 的值。",
            options=None,
            answer="import json\njson_str = '{\"status\": \"success\", \"code\": 200}'\ndata = json.loads(json_str)\nprint(data['status'])",
            explanation="在 API 测试中，经常需要解析 JSON 响应来验证测试结果。",
            order=2
        ),
        Question(
            level_id=level9.id,
            question_type="choice",
            title="选择题：JSON 数据类型",
            content="JSON 格式不支持以下哪种 Python 数据类型？",
            options=json.dumps(["A. 字典", "B. 列表", "C. 元组", "D. 字符串"]),
            answer="C",
            explanation="JSON 不支持元组，Python 的元组会被转换为 JSON 数组（对应 Python 列表）。",
            order=3
        ),
        Question(
            level_id=level9.id,
            question_type="code",
            title="编程题：美化 JSON 输出",
            content="将字典 {'name': 'Test', 'age': 20} 转换为格式化的 JSON 字符串（缩进为2个空格）。",
            options=None,
            answer="import json\ndata = {'name': 'Test', 'age': 20}\njson_str = json.dumps(data, indent=2, ensure_ascii=False)\nprint(json_str)",
            explanation="indent 参数用于格式化输出，ensure_ascii=False 确保中文正常显示。",
            order=4
        ),
        Question(
            level_id=level9.id,
            question_type="choice",
            title="选择题：JSON 文件操作",
            content="将 Python 对象保存到 JSON 文件中，应该使用哪个方法？",
            options=json.dumps(["A. json.dump()", "B. json.write()", "C. json.save()", "D. json.export()"]),
            answer="A",
            explanation="json.dump() 将对象序列化为 JSON 并写入文件，json.dumps() 则返回 JSON 字符串。",
            order=5
        )
    ]
    
    for q in questions_level9:
        db.session.add(q)
    
    # 第十关：正则表达式
    level10 = Level(
        title="第十关：正则表达式基础",
        description="学习正则表达式，用于测试数据的模式匹配和验证",
        order=10,
        category="工具"
    )
    db.session.add(level10)
    db.session.commit()
    
    questions_level10 = [
        Question(
            level_id=level10.id,
            question_type="choice",
            title="选择题：正则表达式模块",
            content="Python 中使用正则表达式需要导入哪个模块？",
            options=json.dumps(["A. regex", "B. re", "C. regexp", "D. pattern"]),
            answer="B",
            explanation="re 是 Python 的正则表达式模块。",
            order=1
        ),
        Question(
            level_id=level10.id,
            question_type="code",
            title="编程题：验证手机号",
            content="使用正则表达式验证字符串是否为 11 位数字的手机号。使用 re.match 方法。",
            options=None,
            answer="import re\ndef is_valid_phone(phone):\n    pattern = r'^\\d{11}$'\n    return bool(re.match(pattern, phone))",
            explanation="\\d{11} 表示匹配 11 个数字，^ 和 $ 表示字符串的开始和结束。",
            order=2
        ),
        Question(
            level_id=level10.id,
            question_type="fill",
            title="填空题：正则匹配",
            content="在正则表达式中，匹配任意单个字符使用 ______ 符号。",
            options=None,
            answer=".",
            explanation=". 在正则表达式中匹配除换行符外的任意单个字符。",
            order=3
        ),
        Question(
            level_id=level10.id,
            question_type="choice",
            title="选择题：正则查找",
            content="re.findall() 方法的作用是？",
            options=json.dumps(["A. 查找第一个匹配项", "B. 查找所有匹配项", "C. 替换匹配项", "D. 分割字符串"]),
            answer="B",
            explanation="re.findall() 返回所有匹配项的列表，re.search() 返回第一个匹配。",
            order=4
        ),
        Question(
            level_id=level10.id,
            question_type="code",
            title="编程题：提取邮箱",
            content="使用正则表达式从字符串 'Contact us at test@example.com or info@test.com' 中提取所有邮箱地址。",
            options=None,
            answer="import re\ntext = 'Contact us at test@example.com or info@test.com'\npattern = r'\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b'\nemails = re.findall(pattern, text)\nprint(emails)",
            explanation="使用正则表达式可以方便地从文本中提取符合模式的内容，在测试中常用于数据验证。",
            order=5
        )
    ]
    
    for q in questions_level10:
        db.session.add(q)
    
    # 第十一关：数据库操作
    level11 = Level(
        title="第十一关：SQLite 数据库操作",
        description="学习使用 SQLite 数据库，为测试数据迁移做准备",
        order=11,
        category="工具"
    )
    db.session.add(level11)
    db.session.commit()
    
    questions_level11 = [
        Question(
            level_id=level11.id,
            question_type="choice",
            title="选择题：数据库操作",
            content="Python 连接 SQLite 数据库使用哪个内置模块？",
            options=json.dumps(["A. sqlite", "B. sqlite3", "C. database", "D. db"]),
            answer="B",
            explanation="sqlite3 是 Python 的内置模块，用于操作 SQLite 数据库。",
            order=1
        ),
        Question(
            level_id=level11.id,
            question_type="code",
            title="编程题：查询数据库",
            content="使用 sqlite3 连接数据库 test.db，执行 SQL 查询 'SELECT * FROM users'，获取所有结果。",
            options=None,
            answer="import sqlite3\nconn = sqlite3.connect('test.db')\ncursor = conn.cursor()\ncursor.execute('SELECT * FROM users')\nresults = cursor.fetchall()\nconn.close()",
            explanation="这是数据库操作的基本流程：连接、执行、获取结果、关闭连接。",
            order=2
        ),
        Question(
            level_id=level11.id,
            question_type="fill",
            title="填空题：数据库提交",
            content="在执行 INSERT、UPDATE 等修改数据的操作后，需要调用连接对象的 ______ 方法保存更改。",
            options=None,
            answer="commit",
            explanation="commit() 方法将事务提交到数据库，使更改永久生效。",
            order=3
        ),
        Question(
            level_id=level11.id,
            question_type="choice",
            title="选择题：SQL 注入防护",
            content="为了防止 SQL 注入，应该使用什么方式传递参数？",
            options=json.dumps(["A. 字符串拼接", "B. 参数化查询", "C. format 方法", "D. % 格式化"]),
            answer="B",
            explanation="参数化查询（使用 ? 占位符）可以有效防止 SQL 注入攻击，是最安全的方式。",
            order=4
        ),
        Question(
            level_id=level11.id,
            question_type="code",
            title="编程题：插入数据",
            content="使用参数化查询向 users 表插入一条记录，姓名为 '测试用户'，年龄为 25。",
            options=None,
            answer="import sqlite3\nconn = sqlite3.connect('test.db')\ncursor = conn.cursor()\ncursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('测试用户', 25))\nconn.commit()\nconn.close()",
            explanation="参数化查询使用 ? 占位符，值通过元组传递，这是安全的数据库操作方式。",
            order=5
        )
    ]
    
    for q in questions_level11:
        db.session.add(q)
    
    # 第十二关：unittest 测试框架基础
    level12 = Level(
        title="第十二关：unittest 测试框架入门",
        description="开始学习 Python 的单元测试框架 unittest",
        order=12,
        category="测试"
    )
    db.session.add(level12)
    db.session.commit()
    
    questions_level12 = [
        Question(
            level_id=level12.id,
            question_type="fill",
            title="填空题：测试类继承",
            content="在 unittest 中，测试类需要继承 unittest.______ 类",
            options=None,
            answer="TestCase",
            explanation="unittest.TestCase 是所有测试用例的基类。",
            order=1
        ),
        Question(
            level_id=level12.id,
            question_type="code",
            title="编程题：编写第一个测试用例",
            content="创建一个测试类 TestMath，编写一个测试方法 test_add，验证 1 + 1 = 2。",
            options=None,
            answer="import unittest\n\nclass TestMath(unittest.TestCase):\n    def test_add(self):\n        self.assertEqual(1 + 1, 2)",
            explanation="测试方法以 test_ 开头，使用 assertEqual 断言相等。",
            order=2
        ),
        Question(
            level_id=level12.id,
            question_type="choice",
            title="选择题：运行测试",
            content="如何运行 unittest 测试？",
            options=json.dumps(["A. python test.py", "B. unittest.main()", "C. python -m unittest test.py", "D. 以上都可以"]),
            answer="D",
            explanation="可以直接运行脚本(包含unittest.main())，也可以使用python -m unittest命令。",
            order=3
        ),
        Question(
            level_id=level12.id,
            question_type="fill",
            title="填空题：测试方法命名",
            content="unittest 中的测试方法必须以 ______ 开头才能被识别和执行。",
            options=None,
            answer="test_|test",
            explanation="只有以test_开头的方法才会被unittest识别为测试方法并执行。",
            order=4
        ),
        Question(
            level_id=level12.id,
            question_type="choice",
            title="选择题：断言方法",
            content="unittest 中用于断言两个值相等的方法是？",
            options=json.dumps(["A. assertEquals()", "B. assertEqual()", "C. assertSame()", "D. assertEquals()"]),
            answer="B",
            explanation="assertEqual() 是 unittest 中用于断言两个值相等的标准方法。",
            order=5
        )
    ]
    
    for q in questions_level12:
        db.session.add(q)
    
    # 第十三关：断言方法
    level13 = Level(
        title="第十三关：unittest 断言方法",
        description="学习各种断言方法，用于验证测试结果",
        order=13,
        category="测试"
    )
    db.session.add(level13)
    db.session.commit()
    
    questions_level13 = [
        Question(
            level_id=level13.id,
            question_type="choice",
            title="选择题：断言方法",
            content="验证某个值为 True 应该使用哪个断言方法？",
            options=json.dumps(["A. assertEqual", "B. assertTrue", "C. assertIs", "D. assertIn"]),
            answer="B",
            explanation="assertTrue() 用于验证表达式为 True。",
            order=1
        ),
        Question(
            level_id=level13.id,
            question_type="code",
            title="编程题：多种断言",
            content="编写测试方法验证：列表 [1, 2, 3] 包含元素 2，使用 assertIn 方法。",
            options=None,
            answer="def test_list_contains(self):\n    my_list = [1, 2, 3]\n    self.assertIn(2, my_list)",
            explanation="assertIn 用于验证元素是否在容器中。",
            order=2
        ),
        Question(
            level_id=level13.id,
            question_type="fill",
            title="填空题：断言相等",
            content="验证两个值相等，应该使用 ______ 断言方法。",
            options=None,
            answer="assertEqual",
            explanation="assertEqual(a, b) 验证 a 和 b 相等。",
            order=3
        ),
        Question(
            level_id=level13.id,
            question_type="choice",
            title="选择题：断言异常",
            content="测试代码是否抛出异常，应该使用什么？",
            options=json.dumps(["A. assertRaises", "B. assertError", "C. assertException", "D. assertThrow"]),
            answer="A",
            explanation="assertRaises 用于验证代码是否抛出预期的异常。",
            order=4
        ),
        Question(
            level_id=level13.id,
            question_type="code",
            title="编程题：断言不等",
            content="编写测试方法验证 5 不等于 3，使用 assertNotEqual 方法。",
            options=None,
            answer="def test_not_equal(self):\n    self.assertNotEqual(5, 3)",
            explanation="assertNotEqual() 用于验证两个值不相等。",
            order=5
        )
    ]
    
    for q in questions_level13:
        db.session.add(q)
    
    # 第十四关：测试夹具
    level14 = Level(
        title="第十四关：测试夹具 setUp 和 tearDown",
        description="学习测试前的准备和测试后的清理工作",
        order=14,
        category="测试"
    )
    db.session.add(level14)
    db.session.commit()
    
    questions_level14 = [
        Question(
            level_id=level14.id,
            question_type="choice",
            title="选择题：测试夹具",
            content="在每个测试方法执行前自动运行的方法是？",
            options=json.dumps(["A. __init__", "B. setUp", "C. before", "D. prepare"]),
            answer="B",
            explanation="setUp() 在每个测试方法前执行，tearDown() 在每个测试方法后执行。",
            order=1
        ),
        Question(
            level_id=level14.id,
            question_type="code",
            title="编程题：使用测试夹具",
            content="创建测试类，在 setUp 中初始化一个空列表 self.data，在测试方法中添加元素并验证。",
            options=None,
            answer="class TestList(unittest.TestCase):\n    def setUp(self):\n        self.data = []\n    \n    def test_append(self):\n        self.data.append(1)\n        self.assertEqual(len(self.data), 1)",
            explanation="setUp 用于准备测试数据，避免在每个测试方法中重复代码。",
            order=2
        ),
        Question(
            level_id=level14.id,
            question_type="fill",
            title="填空题：清理方法",
            content="在每个测试方法执行后自动运行的清理方法是 ______。",
            options=None,
            answer="tearDown",
            explanation="tearDown() 用于清理测试后的资源，如关闭文件、断开数据库连接等。",
            order=3
        ),
        Question(
            level_id=level14.id,
            question_type="choice",
            title="选择题：类级别夹具",
            content="只在测试类开始时执行一次的方法是？",
            options=json.dumps(["A. setUp", "B. setUpClass", "C. classSetUp", "D. initClass"]),
            answer="B",
            explanation="setUpClass() 是类方法，在整个测试类开始时执行一次，tearDownClass() 在结束时执行一次。",
            order=4
        ),
        Question(
            level_id=level14.id,
            question_type="code",
            title="编程题：tearDown 清理",
            content="编写 tearDown 方法，关闭一个文件句柄 self.file（假设已在 setUp 中打开）。",
            options=None,
            answer="def tearDown(self):\n    if hasattr(self, 'file') and self.file:\n        self.file.close()",
            explanation="tearDown 用于清理测试后的资源，确保测试环境干净。",
            order=5
        )
    ]
    
    for q in questions_level14:
        db.session.add(q)
    
    # 第十五关：数据驱动测试
    level15 = Level(
        title="第十五关：参数化测试和数据驱动",
        description="学习如何用不同的数据运行同一个测试",
        order=15,
        category="测试"
    )
    db.session.add(level15)
    db.session.commit()
    
    questions_level15 = [
        Question(
            level_id=level15.id,
            question_type="code",
            title="编程题：批量测试",
            content="编写测试方法，使用循环测试多组数据：[(2, 3, 5), (1, 1, 2), (0, 0, 0)]，验证前两个数之和等于第三个数。",
            options=None,
            answer="def test_addition_multiple(self):\n    test_data = [(2, 3, 5), (1, 1, 2), (0, 0, 0)]\n    for a, b, expected in test_data:\n        with self.subTest(a=a, b=b):\n            self.assertEqual(a + b, expected)",
            explanation="使用 subTest 可以在一个测试方法中测试多组数据，失败时能显示具体是哪组数据。",
            order=1
        ),
        Question(
            level_id=level15.id,
            question_type="choice",
            title="选择题：数据驱动",
            content="数据驱动测试的主要优势是什么？",
            options=json.dumps(["A. 代码更短", "B. 用相同逻辑测试多组数据", "C. 运行更快", "D. 不需要断言"]),
            answer="B",
            explanation="数据驱动测试允许使用相同的测试逻辑测试多组不同的输入数据，提高测试覆盖率。",
            order=2
        ),
        Question(
            level_id=level15.id,
            question_type="fill",
            title="填空题：subTest",
            content="在一个测试方法中测试多组数据时，使用 ______ 可以在某组数据失败时继续测试其他数据。",
            options=None,
            answer="subTest",
            explanation="self.subTest() 创建子测试，即使某组数据失败也会继续执行其他组的测试。",
            order=3
        ),
        Question(
            level_id=level15.id,
            question_type="choice",
            title="选择题：参数化库",
            content="在 unittest 中实现参数化测试，除了 subTest，还可以使用哪个第三方库？",
            options=json.dumps(["A. parameterized", "B. pytest-parametrize", "C. params", "D. testdata"]),
            answer="A",
            explanation="parameterized 是一个流行的第三方库，可以为 unittest 提供参数化测试功能。",
            order=4
        ),
        Question(
            level_id=level15.id,
            question_type="code",
            title="编程题：从文件读取测试数据",
            content="编写代码从 CSV 文件读取测试数据并进行测试（示例框架）。",
            options=None,
            answer="import csv\nimport unittest\n\nclass TestWithCSV(unittest.TestCase):\n    def test_from_csv(self):\n        with open('test_data.csv', 'r') as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                with self.subTest(row=row):\n                    # 执行测试逻辑\n                    pass",
            explanation="数据驱动测试可以从外部文件（如CSV）读取测试数据，使测试更灵活。",
            order=5
        )
    ]
    
    for q in questions_level15:
        db.session.add(q)
    
    # 第十六关：Mock 和补丁
    level16 = Level(
        title="第十六关：Mock 对象和打补丁",
        description="学习使用 Mock 对象模拟外部依赖，隔离测试环境",
        order=16,
        category="测试"
    )
    db.session.add(level16)
    db.session.commit()
    
    questions_level16 = [
        Question(
            level_id=level16.id,
            question_type="choice",
            title="选择题：Mock 库",
            content="Python 3.3+ 中，Mock 功能在哪个模块中？",
            options=json.dumps(["A. mock", "B. unittest.mock", "C. test.mock", "D. mocklib"]),
            answer="B",
            explanation="从 Python 3.3 开始，Mock 功能集成到 unittest.mock 模块中。",
            order=1
        ),
        Question(
            level_id=level16.id,
            question_type="code",
            title="编程题：使用 Mock",
            content="使用 unittest.mock.Mock 创建一个模拟对象，设置其 get_name 方法返回 'Test User'。",
            options=None,
            answer="from unittest.mock import Mock\n\nmock_obj = Mock()\nmock_obj.get_name.return_value = 'Test User'",
            explanation="Mock 对象可以模拟任何对象的行为，return_value 设置返回值。",
            order=2
        ),
        Question(
            level_id=level16.id,
            question_type="fill",
            title="填空题：patch 装饰器",
            content="要临时替换模块中的函数或类，使用 ______ 装饰器。",
            options=None,
            answer="patch",
            explanation="@patch 装饰器可以临时替换对象，测试结束后自动恢复。",
            order=3
        ),
        Question(
            level_id=level16.id,
            question_type="choice",
            title="选择题：Mock 的作用",
            content="使用 Mock 对象的主要目的是什么？",
            options=json.dumps(["A. 加快测试速度", "B. 隔离外部依赖", "C. 减少代码量", "D. 美化代码"]),
            answer="B",
            explanation="Mock 主要用于隔离外部依赖（如数据库、API等），让测试更可控和可靠。",
            order=4
        ),
        Question(
            level_id=level16.id,
            question_type="code",
            title="编程题：patch 上下文管理器",
            content="使用 patch 作为上下文管理器，模拟 random.randint 返回固定值 5。",
            options=None,
            answer="from unittest.mock import patch\n\nwith patch('random.randint', return_value=5):\n    import random\n    result = random.randint(1, 10)\n    print(result)  # 输出 5",
            explanation="patch 可以作为装饰器或上下文管理器使用，临时替换函数或方法的行为。",
            order=5
        )
    ]
    
    for q in questions_level16:
        db.session.add(q)
    
    # 第十七关：HTTP 请求测试
    level17 = Level(
        title="第十七关：HTTP 请求和 API 测试",
        description="学习使用 requests 库进行 API 测试",
        order=17,
        category="测试"
    )
    db.session.add(level17)
    db.session.commit()
    
    questions_level17 = [
        Question(
            level_id=level17.id,
            question_type="fill",
            title="填空题：HTTP 请求库",
            content="Python 中最常用的 HTTP 请求库是 ______",
            options=None,
            answer="requests",
            explanation="requests 是 Python 最流行的 HTTP 请求库，语法简洁易用。",
            order=1
        ),
        Question(
            level_id=level17.id,
            question_type="code",
            title="编程题：GET 请求测试",
            content="使用 requests 发送 GET 请求到 'https://api.example.com/users'，验证响应状态码是 200。",
            options=None,
            answer="import requests\n\nresponse = requests.get('https://api.example.com/users')\nassert response.status_code == 200",
            explanation="这是 API 测试的基本模式：发送请求、验证响应。",
            order=2
        ),
        Question(
            level_id=level17.id,
            question_type="choice",
            title="选择题：HTTP 方法",
            content="以下哪个不是常见的 HTTP 请求方法？",
            options=json.dumps(["A. GET", "B. POST", "C. FETCH", "D. DELETE"]),
            answer="C",
            explanation="常见的 HTTP 方法有 GET、POST、PUT、DELETE、PATCH 等，没有 FETCH 方法。",
            order=3
        ),
        Question(
            level_id=level17.id,
            question_type="code",
            title="编程题：POST 请求",
            content="使用 requests 发送 POST 请求，提交 JSON 数据 {'name': 'Test', 'age': 25}。",
            options=None,
            answer="import requests\n\ndata = {'name': 'Test', 'age': 25}\nresponse = requests.post('https://api.example.com/users', json=data)",
            explanation="json 参数会自动将字典转换为 JSON 格式并设置正确的 Content-Type。",
            order=4
        ),
        Question(
            level_id=level17.id,
            question_type="fill",
            title="填空题：HTTP 响应",
            content="使用 requests 发送请求后，通过 response.______ 属性获取 JSON 格式的响应数据。",
            options=None,
            answer="json()",
            explanation="response.json() 方法将响应体解析为 JSON 对象（Python 字典或列表）。",
            order=5
        )
    ]
    
    for q in questions_level17:
        db.session.add(q)
    
    # 第十八关：测试报告生成
    level18 = Level(
        title="第十八关：生成测试报告",
        description="学习如何生成和导出测试报告",
        order=18,
        category="测试"
    )
    db.session.add(level18)
    db.session.commit()
    
    questions_level18 = [
        Question(
            level_id=level18.id,
            question_type="choice",
            title="选择题：测试运行器",
            content="unittest 中使用哪个类来运行测试？",
            options=json.dumps(["A. TestRunner", "B. TestExecutor", "C. TextTestRunner", "D. TestManager"]),
            answer="C",
            explanation="unittest.TextTestRunner 是默认的测试运行器，可以生成文本格式的测试报告。",
            order=1
        ),
        Question(
            level_id=level18.id,
            question_type="code",
            title="编程题：运行测试套件",
            content="创建测试套件并使用 TextTestRunner 运行。",
            options=None,
            answer="import unittest\n\nsuite = unittest.TestLoader().loadTestsFromTestCase(TestMath)\nrunner = unittest.TextTestRunner(verbosity=2)\nrunner.run(suite)",
            explanation="TestLoader 加载测试用例，TextTestRunner 执行测试并输出结果。",
            order=2
        ),
        Question(
            level_id=level18.id,
            question_type="fill",
            title="填空题：测试详细度",
            content="TextTestRunner 的 ______ 参数控制输出的详细程度，值越大越详细。",
            options=None,
            answer="verbosity",
            explanation="verbosity=0 只输出结果，verbosity=1 输出点，verbosity=2 输出详细信息。",
            order=3
        ),
        Question(
            level_id=level18.id,
            question_type="choice",
            title="选择题：HTML 报告",
            content="要生成 HTML 格式的测试报告，通常使用哪个第三方库？",
            options=json.dumps(["A. unittest-html", "B. HTMLTestRunner", "C. pytest-html", "D. 以上都可以"]),
            answer="D",
            explanation="HTMLTestRunner、pytest-html 等都可以生成 HTML 格式的测试报告。",
            order=4
        ),
        Question(
            level_id=level18.id,
            question_type="code",
            title="编程题：自定义测试结果",
            content="创建一个继承自 unittest.TestResult 的自定义结果类，重写 addSuccess 方法打印成功消息。",
            options=None,
            answer="import unittest\n\nclass CustomResult(unittest.TestResult):\n    def addSuccess(self, test):\n        super().addSuccess(test)\n        print(f'测试成功: {test}')",
            explanation="可以通过继承 TestResult 来自定义测试结果的处理方式。",
            order=5
        )
    ]
    
    for q in questions_level18:
        db.session.add(q)
    
    # 第十九关：实战 - 数据迁移工具
    level19 = Level(
        title="第十九关：实战项目 - 数据迁移工具",
        description="综合运用所学知识，编写一个 CSV 到数据库的数据迁移工具",
        order=19,
        category="项目"
    )
    db.session.add(level19)
    db.session.commit()
    
    questions_level19 = [
        Question(
            level_id=level19.id,
            question_type="code",
            title="项目题：CSV 数据迁移",
            content="编写函数 migrate_csv_to_db(csv_file, db_file, table_name)，将 CSV 文件数据导入 SQLite 数据库。",
            options=None,
            answer="import csv\nimport sqlite3\n\ndef migrate_csv_to_db(csv_file, db_file, table_name):\n    conn = sqlite3.connect(db_file)\n    cursor = conn.cursor()\n    \n    with open(csv_file, 'r', encoding='utf-8') as f:\n        reader = csv.DictReader(f)\n        for row in reader:\n            columns = ', '.join(row.keys())\n            placeholders = ', '.join(['?'] * len(row))\n            sql = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'\n            cursor.execute(sql, list(row.values()))\n    \n    conn.commit()\n    conn.close()",
            explanation="这个工具结合了 CSV 读取和数据库操作，是实际工作中常见的数据迁移场景。",
            order=1
        ),
        Question(
            level_id=level19.id,
            question_type="choice",
            title="选择题：数据迁移注意事项",
            content="在数据迁移过程中，最需要注意的是什么？",
            options=json.dumps(["A. 速度", "B. 数据完整性", "C. 代码简洁", "D. 界面美观"]),
            answer="B",
            explanation="数据迁移最重要的是确保数据完整性，不能丢失或损坏数据。",
            order=2
        ),
        Question(
            level_id=level19.id,
            question_type="fill",
            title="填空题：批量插入",
            content="在 SQLite 中，批量插入多条数据使用 executemany 方法比多次调用 execute 更 ______。",
            options=None,
            answer="高效|快",
            explanation="executemany 可以一次性插入多条数据，减少数据库操作次数，提高效率。",
            order=3
        ),
        Question(
            level_id=level19.id,
            question_type="choice",
            title="选择题：数据验证",
            content="数据迁移前应该做什么？",
            options=json.dumps(["A. 直接开始迁移", "B. 验证源数据格式", "C. 删除目标数据", "D. 不需要准备"]),
            answer="B",
            explanation="迁移前应验证源数据的格式和完整性，确保迁移过程顺利。",
            order=4
        ),
        Question(
            level_id=level19.id,
            question_type="code",
            title="编程题：数据迁移错误处理",
            content="为数据迁移添加错误处理，记录失败的行。",
            options=None,
            answer="import csv\nimport sqlite3\n\nfailed_rows = []\nwith open('data.csv', 'r') as f:\n    reader = csv.DictReader(f)\n    for row in reader:\n        try:\n            # 插入数据逻辑\n            pass\n        except Exception as e:\n            failed_rows.append({'row': row, 'error': str(e)})\nprint(f'失败记录数: {len(failed_rows)}')",
            explanation="在数据迁移中，应该记录失败的记录以便后续处理。",
            order=5
        )
    ]
    
    for q in questions_level19:
        db.session.add(q)
    
    # 第二十关：实战 - 测试数据生成器
    level20 = Level(
        title="第二十关：实战项目 - 测试数据生成器",
        description="编写一个灵活的测试数据生成工具",
        order=20,
        category="项目"
    )
    db.session.add(level20)
    db.session.commit()
    
    questions_level20 = [
        Question(
            level_id=level20.id,
            question_type="code",
            title="项目题：批量生成用户数据",
            content="编写类 TestDataGenerator，包含方法 generate_users(count)，生成指定数量的随机用户数据（包含姓名、年龄、邮箱）。",
            options=None,
            answer="import random\nimport string\n\nclass TestDataGenerator:\n    def generate_users(self, count):\n        users = []\n        for i in range(count):\n            name = f'User{i+1}'\n            age = random.randint(18, 60)\n            email = f'user{i+1}@test.com'\n            users.append({'name': name, 'age': age, 'email': email})\n        return users",
            explanation="测试数据生成器可以快速创建大量测试数据，提高测试效率。",
            order=1
        ),
        Question(
            level_id=level20.id,
            question_type="choice",
            title="选择题：随机数据生成",
            content="生成随机数据时，以下哪个不是好的实践？",
            options=json.dumps(["A. 使用 random 模块", "B. 设置随机种子以便重现", "C. 每次生成完全相同的数据", "D. 生成符合实际规则的数据"]),
            answer="C",
            explanation="测试数据应该有一定的随机性和多样性，完全相同的数据可能无法覆盖所有场景。",
            order=2
        ),
        Question(
            level_id=level20.id,
            question_type="fill",
            title="填空题：Faker 库",
            content="Python 中有一个专门用于生成假数据的第三方库叫 ______。",
            options=None,
            answer="Faker|faker",
            explanation="Faker 库可以生成各种类型的假数据，如姓名、地址、电话号码等，非常适合测试使用。",
            order=3
        ),
        Question(
            level_id=level20.id,
            question_type="code",
            title="编程题：生成随机密码",
            content="编写函数 generate_password(length=8)，生成指定长度的随机密码（包含字母和数字）。",
            options=None,
            answer="import random\nimport string\n\ndef generate_password(length=8):\n    chars = string.ascii_letters + string.digits\n    return ''.join(random.choice(chars) for _ in range(length))",
            explanation="使用 random 和 string 模块可以生成各种随机测试数据。",
            order=4
        ),
        Question(
            level_id=level20.id,
            question_type="choice",
            title="选择题：数据生成策略",
            content="在生成测试数据时，哪种策略最好？",
            options=json.dumps(["A. 只生成正常数据", "B. 只生成边界数据", "C. 混合正常、边界和异常数据", "D. 随意生成"]),
            answer="C",
            explanation="好的测试数据应该包含正常、边界和异常情况，以充分测试系统的健壮性。",
            order=5
        )
    ]
    
    for q in questions_level20:
        db.session.add(q)
    
    # 第二十一关：最终项目 - 测试框架搭建
    level21 = Level(
        title="第二十一关：终极挑战 - 搭建自己的测试框架",
        description="整合所有知识，搭建一个完整的自动化测试框架 Demo",
        order=21,
        category="项目"
    )
    db.session.add(level21)
    db.session.commit()
    
    questions_level21 = [
        Question(
            level_id=level21.id,
            question_type="code",
            title="终极项目：测试框架 Demo",
            content="""创建一个简单的测试框架，包含以下功能：
1. BaseTest 基类，包含 setUp 和 tearDown
2. 测试用例管理
3. 测试报告生成
4. 日志记录

请实现 BaseTest 类的基本结构。""",
            options=None,
            answer="""import unittest
import logging
from datetime import datetime

class BaseTest(unittest.TestCase):
    \"\"\"测试基类\"\"\"
    
    @classmethod
    def setUpClass(cls):
        # 配置日志
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename=f'test_log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
        )
        cls.logger = logging.getLogger(__name__)
        cls.logger.info('测试开始')
    
    def setUp(self):
        self.logger.info(f'开始测试: {self._testMethodName}')
    
    def tearDown(self):
        self.logger.info(f'结束测试: {self._testMethodName}')
    
    @classmethod
    def tearDownClass(cls):
        cls.logger.info('所有测试完成')""",
            explanation="""这个测试框架基类提供了：
- 日志记录功能
- 测试前后的准备和清理
- 可以被其他测试类继承
这是一个真实测试框架的基础结构。""",
            order=1
        ),
        Question(
            level_id=level21.id,
            question_type="code",
            title="终极项目：完整测试套件",
            content="基于 BaseTest，创建一个测试类 APITest，包含至少两个测试方法，演示完整的测试流程。",
            options=None,
            answer="""class APITest(BaseTest):
    \"\"\"API 测试示例\"\"\"
    
    def setUp(self):
        super().setUp()
        self.base_url = 'https://api.example.com'
        self.headers = {'Content-Type': 'application/json'}
    
    def test_get_user(self):
        \"\"\"测试获取用户信息\"\"\"
        # 模拟测试
        user_id = 1
        self.logger.info(f'测试获取用户 {user_id}')
        # response = requests.get(f'{self.base_url}/users/{user_id}')
        # self.assertEqual(response.status_code, 200)
        self.assertTrue(True)  # 示例
    
    def test_create_user(self):
        \"\"\"测试创建用户\"\"\"
        self.logger.info('测试创建用户')
        # data = {'name': 'Test User', 'email': 'test@example.com'}
        # response = requests.post(f'{self.base_url}/users', json=data)
        # self.assertEqual(response.status_code, 201)
        self.assertTrue(True)  # 示例""",
            explanation="""恭喜完成最终挑战！你已经学会了：
1. 搭建测试框架的基本结构
2. 使用继承组织测试代码
3. 集成日志记录
4. 编写实际的测试用例

这些知识可以帮助你在实际工作中搭建自己的自动化测试框架！""",
            order=2
        ),
        Question(
            level_id=level21.id,
            question_type="choice",
            title="选择题：测试框架设计",
            content="设计测试框架时，以下哪个不是好的实践？",
            options=json.dumps(["A. 提供清晰的日志", "B. 可扩展性强", "C. 硬编码所有配置", "D. 模块化设计"]),
            answer="C",
            explanation="配置应该灵活可配置，而不是硬编码，这样才能适应不同的测试环境。",
            order=3
        ),
        Question(
            level_id=level21.id,
            question_type="fill",
            title="填空题：测试框架组成",
            content="一个完整的测试框架通常包括：测试用例管理、测试执行、测试报告和 ______。",
            options=None,
            answer="日志记录|配置管理|数据管理",
            explanation="除了这些核心功能，还需要日志记录、配置管理、测试数据管理等支撑功能。",
            order=4
        ),
        Question(
            level_id=level21.id,
            question_type="choice",
            title="选择题：框架最佳实践",
            content="测试框架应该具备哪个特性？",
            options=json.dumps(["A. 易于使用", "B. 可维护性强", "C. 支持扩展", "D. 以上都是"]),
            answer="D",
            explanation="优秀的测试框架应该易于使用、可维护性强、支持扩展，满足各种测试需求。",
            order=5
        )
    ]
    
    for q in questions_level21:
        db.session.add(q)
    
    db.session.commit()
    print("数据库初始化完成！已添加 21 个关卡和多个题目。")
