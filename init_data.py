"""
初始化关卡和题目数据
包含从基础到高级的 Python 学习内容，侧重软件测试
"""

import json

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
        )
    ]
    
    for q in questions_level5:
        db.session.add(q)
    
    # 第六关：列表和字典操作
    level6 = Level(
        title="第六关：列表和字典高级操作",
        description="深入学习列表和字典的操作方法，为处理测试数据做准备",
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
        )
    ]
    
    for q in questions_level21:
        db.session.add(q)
    
    db.session.commit()
    print("数据库初始化完成！已添加 21 个关卡和多个题目。")
