"""
第 03 章：运算符与流程控制
知识点：算术/比较/逻辑/位运算符、三元表达式、if/elif/else、match/case（Python 3.10+）
"""

# ============================================================
# 1. 算术运算符
# ============================================================

print("=== 算术运算符 ===")

a, b = 17, 5
print(f"a={a}, b={b}")
print(f"  a + b  = {a + b}")    # 加
print(f"  a - b  = {a - b}")    # 减
print(f"  a * b  = {a * b}")    # 乘
print(f"  a / b  = {a / b}")    # 除（始终返回 float）
print(f"  a // b = {a // b}")   # 整除
print(f"  a % b  = {a % b}")    # 取余
print(f"  a ** b = {a ** b}")   # 幂次

# 增量赋值
x = 10
x += 3;  print(f"x += 3 -> {x}")
x -= 2;  print(f"x -= 2 -> {x}")
x *= 2;  print(f"x *= 2 -> {x}")
x //= 3; print(f"x //= 3 -> {x}")

# ============================================================
# 2. 比较运算符
# ============================================================

print("\n=== 比较运算符 ===")

print(f"5 == 5   : {5 == 5}")
print(f"5 != 3   : {5 != 3}")
print(f"5 > 3    : {5 > 3}")
print(f"5 < 3    : {5 < 3}")
print(f"5 >= 5   : {5 >= 5}")
print(f"5 <= 4   : {5 <= 4}")

# 链式比较（Python 特性）
age = 25
print(f"18 <= {age} <= 60: {18 <= age <= 60}")

# is / is not（身份比较）
a_list = [1, 2]
b_list = [1, 2]
c_list = a_list
print(f"a_list == b_list: {a_list == b_list}")    # True（值相等）
print(f"a_list is b_list: {a_list is b_list}")    # False（不同对象）
print(f"a_list is c_list: {a_list is c_list}")    # True（同一对象）

# in / not in（成员检查）
fruits = ["apple", "banana", "cherry"]
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'mango' not in fruits: {'mango' not in fruits}")

# ============================================================
# 3. 逻辑运算符
# ============================================================

print("\n=== 逻辑运算符 ===")

# 短路求值
print(f"True and False: {True and False}")
print(f"True or False:  {True or False}")
print(f"not True:       {not True}")

# 短路求值实用技巧
name = ""
display = name or "匿名用户"   # name 为空时取默认值
print(f"name or '匿名用户': {display}")

value = None
safe = value or 0              # 空值保护
print(f"None or 0: {safe}")

# and 短路
def risky():
    print("  risky() 被调用")
    return True

flag = False
result = flag and risky()      # flag 为 False，risky() 不会被调用
print(f"False and risky(): {result}（risky 未执行）")

# ============================================================
# 4. 位运算符
# ============================================================

print("\n=== 位运算符 ===")

p, q = 0b1010, 0b1100          # 10 和 12
print(f"p = {p:04b} ({p})")
print(f"q = {q:04b} ({q})")
print(f"p & q  = {p & q:04b} ({p & q})")    # 按位与
print(f"p | q  = {p | q:04b} ({p | q})")    # 按位或
print(f"p ^ q  = {p ^ q:04b} ({p ^ q})")    # 按位异或
print(f"~p     = {~p}")                       # 按位取反
print(f"p << 1 = {p << 1:04b} ({p << 1})")  # 左移
print(f"p >> 1 = {p >> 1:04b} ({p >> 1})")  # 右移

# ============================================================
# 5. 三元表达式（条件表达式）
# ============================================================

print("\n=== 三元表达式 ===")

score = 75
grade = "及格" if score >= 60 else "不及格"
print(f"score={score}, grade={grade}")

# 嵌套三元（可读性较差，不推荐超过两层）
level = "优" if score >= 90 else ("良" if score >= 75 else "中")
print(f"level={level}")

# ============================================================
# 6. if / elif / else
# ============================================================

print("\n=== if / elif / else ===")

def classify_score(score: int) -> str:
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 70:
        return "中等"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

for s in [95, 85, 73, 62, 50]:
    print(f"  score={s:3d} -> {classify_score(s)}")

# ============================================================
# 7. match / case（Python 3.10+）
# ============================================================

print("\n=== match / case ===")

# 基本值匹配
def day_type(day: str) -> str:
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "工作日"
        case "Saturday" | "Sunday":
            return "周末"
        case _:
            return "未知"

for d in ["Monday", "Saturday", "Holiday"]:
    print(f"  {d} -> {day_type(d)}")

# 带守卫（guard）的 match
print()

def classify_number(n: int) -> str:
    match n:
        case 0:
            return "零"
        case n if n > 0 and n % 2 == 0:
            return "正偶数"
        case n if n > 0:
            return "正奇数"
        case _:
            return "负数"

for num in [0, 4, 7, -3]:
    print(f"  {num:3d} -> {classify_number(num)}")

# 序列模式匹配
print()

def describe_list(lst: list) -> str:
    match lst:
        case []:
            return "空列表"
        case [x]:
            return f"单元素列表: {x}"
        case [first, *rest]:
            return f"首元素={first}, 其余={rest}"

for lst in [[], [42], [1, 2, 3]]:
    print(f"  {lst} -> {describe_list(lst)}")

# 字典/对象结构匹配
print()

def handle_event(event: dict) -> str:
    match event:
        case {"type": "click", "x": x, "y": y}:
            return f"点击坐标 ({x}, {y})"
        case {"type": "keydown", "key": key}:
            return f"按键: {key}"
        case {"type": t}:
            return f"未知事件类型: {t}"
        case _:
            return "无效事件"

events = [
    {"type": "click", "x": 100, "y": 200},
    {"type": "keydown", "key": "Enter"},
    {"type": "scroll"},
]
for e in events:
    print(f"  {e} -> {handle_event(e)}")
