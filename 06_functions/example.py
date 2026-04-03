"""
第 06 章：函数
知识点：函数定义与调用、默认参数、仅关键字参数、*args/**kwargs、
        lambda、类型注解、递归（斐波那契）、闭包
"""

# ============================================================
# 1. 基本函数定义与调用
# ============================================================

print("=== 基本函数 ===")

def greet(name: str) -> str:
    """向指定姓名的人打招呼，返回问候字符串。"""
    return f"你好，{name}！"

print(greet("Alice"))
print(greet("Bob"))

# 查看函数文档字符串
print(greet.__doc__)

# ============================================================
# 2. 默认参数
# ============================================================

print("\n=== 默认参数 ===")

def make_coffee(size: str = "中杯", sugar: int = 1, milk: bool = True) -> str:
    milk_str = "加奶" if milk else "不加奶"
    return f"{size}咖啡，{sugar}块糖，{milk_str}"

print(make_coffee())                          # 全部使用默认值
print(make_coffee("大杯"))                    # 只指定 size
print(make_coffee("小杯", 0, False))          # 全部指定（位置参数）
print(make_coffee(sugar=2, size="大杯"))      # 关键字参数，顺序可变

# 注意：默认参数应使用不可变对象
# 错误示例：def bad_append(item, lst=[]) 会共享同一个列表
def safe_append(item, lst: list | None = None) -> list:
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(safe_append(1))
print(safe_append(2))   # 正确：每次都是新列表

# ============================================================
# 3. 仅关键字参数（keyword-only）
# ============================================================

print("\n=== 仅关键字参数 ===")

# * 之后的参数必须用关键字传递
def send_email(to: str, subject: str, *, cc: str = "", bcc: str = "") -> None:
    print(f"  发送邮件 -> to={to}, subject={subject}, cc={cc}, bcc={bcc}")

send_email("alice@example.com", "Hello", cc="boss@example.com")
# send_email("alice@example.com", "Hello", "boss@example.com")  # TypeError

# / 之前的参数只能位置传递（Python 3.8+）
def pos_only(x: int, y: int, /, z: int = 0) -> int:
    return x + y + z

print(f"pos_only(1, 2, z=3) = {pos_only(1, 2, z=3)}")

# ============================================================
# 4. *args 和 **kwargs
# ============================================================

print("\n=== *args / **kwargs ===")

# *args：接收任意数量的位置参数，打包为元组
def sum_all(*args: int) -> int:
    return sum(args)

print(f"sum_all(1,2,3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1..10) = {sum_all(*range(1, 11))}")

# **kwargs：接收任意数量的关键字参数，打包为字典
def print_info(**kwargs: str) -> None:
    for key, val in kwargs.items():
        print(f"  {key}: {val}")

print_info(name="Alice", age="20", city="Beijing")

# 混合使用
def mixed(first: int, *args: int, sep: str = ",", **kwargs) -> None:
    print(f"  first={first}, args={args}, sep={sep!r}, kwargs={kwargs}")

mixed(1, 2, 3, sep="-", extra="test")

# ============================================================
# 5. lambda 表达式
# ============================================================

print("\n=== lambda ===")

# 基本形式：lambda 参数: 表达式
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

# 排序 key
students = [("Alice", 85), ("Bob", 92), ("Carol", 78)]
students.sort(key=lambda s: s[1], reverse=True)
print(f"按分数排序: {students}")

# 与 map/filter/sorted 配合
nums = [1, -2, 3, -4, 5, -6]
positives = list(filter(lambda x: x > 0, nums))
doubled = list(map(lambda x: x * 2, nums))
print(f"正数: {positives}")
print(f"翻倍: {doubled}")

# ============================================================
# 6. 类型注解
# ============================================================

print("\n=== 类型注解 ===")

# Python 3.10+ 可用 X | Y 联合类型
def describe(value: int | float | str) -> str:
    if isinstance(value, str):
        return f"字符串，长度 {len(value)}"
    return f"数值，平方 {value ** 2}"

print(describe(5))
print(describe(3.14))
print(describe("hello"))

# 容器类型注解
def top_n(items: list[int], n: int = 3) -> list[int]:
    return sorted(items, reverse=True)[:n]

print(f"top_3: {top_n([3,1,4,1,5,9,2,6])}")

# ============================================================
# 7. 递归
# ============================================================

print("\n=== 递归 ===")

# 斐波那契数列（带备忘录）
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    """返回第 n 个斐波那契数（0 索引）。"""
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

fib_seq = [fib(i) for i in range(10)]
print(f"斐波那契前10项: {fib_seq}")

# 阶乘
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"10! = {factorial(10)}")

# ============================================================
# 8. 闭包
# ============================================================

print("\n=== 闭包 ===")

def make_counter(start: int = 0):
    """工厂函数：返回一个计数器闭包。"""
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

c1 = make_counter()
c2 = make_counter(10)

print(f"c1: {c1()}, {c1()}, {c1()}")   # 1, 2, 3
print(f"c2: {c2()}, {c2()}, {c2()}")   # 11, 12, 13（各自独立）

# 闭包捕获变量
def make_multiplier(factor: int):
    return lambda x: x * factor

double = make_multiplier(2)
triple = make_multiplier(3)
print(f"double(5)={double(5)}, triple(5)={triple(5)}")
