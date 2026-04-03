"""
第 11 章：高级特性
知识点：函数装饰器（计时/日志）、生成器/yield、生成器表达式、
        迭代器协议（__iter__/__next__）、contextlib.contextmanager、
        类型联合 X | Y（Python 3.10+）
"""

import time
import functools
import contextlib
from collections.abc import Iterator, Generator

# ============================================================
# 1. 函数装饰器
# ============================================================

print("=== 函数装饰器 ===")

# --- 计时装饰器 ---
def timer(func):
    """测量函数执行时间的装饰器。"""
    @functools.wraps(func)    # 保留原函数的 __name__ / __doc__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  [{func.__name__}] 耗时 {elapsed:.6f}s")
        return result
    return wrapper

# --- 日志装饰器 ---
def log_call(func):
    """记录函数调用参数和返回值的装饰器。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"  调用 {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"  返回 {result!r}")
        return result
    return wrapper

@timer
@log_call
def slow_sum(n: int) -> int:
    """计算 1+2+...+n。"""
    return sum(range(n + 1))

slow_sum(1000)

# --- 带参数的装饰器（装饰器工厂）---
def retry(max_times: int = 3, exceptions: tuple = (Exception,)):
    """自动重试装饰器，捕获指定异常后重试最多 max_times 次。"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_times + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_times:
                        raise
                    print(f"  第{attempt}次失败({type(e).__name__})，重试...")
        return wrapper
    return decorator

import random
random.seed(10)

@retry(max_times=3, exceptions=(ValueError,))
def unstable_api(x: int) -> str:
    if random.random() < 0.6:
        raise ValueError("随机失败")
    return f"成功：{x}"

print()
try:
    result = unstable_api(42)
    print(f"  最终结果: {result}")
except ValueError:
    print("  三次都失败了")

# ============================================================
# 2. 生成器（generator）
# ============================================================

print("\n=== 生成器 ===")

# --- 生成器函数（yield）---
def fibonacci() -> Generator[int, None, None]:
    """无限斐波那契数列生成器。"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(f"斐波那契前10项: {first_10}")

# --- 带 yield from 的生成器 ---
def chain(*iterables):
    """将多个可迭代对象串联。"""
    for it in iterables:
        yield from it

print(f"yield from: {list(chain([1,2], 'ab', (3,4)))}")

# --- 生成器与协程（send）---
def accumulator() -> Generator[float, float, str]:
    """接收值并持续累加，返回汇总。"""
    total = 0.0
    while True:
        value = yield total     # yield 既发送当前值，又接收下一个值
        if value is None:
            return f"最终总计: {total}"
        total += value

acc = accumulator()
next(acc)             # 启动生成器
print(f"发送 10: {acc.send(10)}")
print(f"发送 20: {acc.send(20)}")
print(f"发送 5:  {acc.send(5)}")

# --- 生成器表达式 ---
print("\n生成器表达式（节省内存）:")
# 与列表推导式语法相同，用 () 代替 []
gen_exp = (x**2 for x in range(1, 6))
print(f"生成器对象: {gen_exp}")
print(f"求和（消耗生成器）: {sum(gen_exp)}")

# 内存对比
import sys
list_comp = [x**2 for x in range(10000)]
gen_comp  = (x**2 for x in range(10000))
print(f"列表推导式大小: {sys.getsizeof(list_comp):>10} bytes")
print(f"生成器表达式大小: {sys.getsizeof(gen_comp):>8} bytes")

# ============================================================
# 3. 迭代器协议
# ============================================================

print("\n=== 迭代器协议 ===")

class CountDown:
    """从 start 倒数到 0 的迭代器。"""

    def __init__(self, start: int) -> None:
        self.start = start
        self.current = start

    def __iter__(self) -> "CountDown":
        # 重置并返回 self（迭代器本身）
        self.current = self.start
        return self

    def __next__(self) -> int:
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


countdown = CountDown(5)
print("CountDown(5):", list(countdown))
print("for 循环:", end=" ")
for n in CountDown(3):
    print(n, end=" ")
print()

# 与 iter() / next() 内置函数的关系
it = iter([10, 20, 30])
print(f"next(it): {next(it)}, {next(it)}, {next(it)}")
try:
    next(it)
except StopIteration:
    print("StopIteration 被抛出")

# ============================================================
# 4. contextlib.contextmanager
# ============================================================

print("\n=== 上下文管理器 ===")

# --- 用类实现 ---
class ManagedResource:
    def __init__(self, name: str) -> None:
        self.name = name

    def __enter__(self):
        print(f"  [进入] 获取资源: {self.name}")
        return self   # with ... as x 中的 x

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"  [退出] 释放资源: {self.name}")
        if exc_type:
            print(f"  [退出] 捕获到异常: {exc_type.__name__}: {exc_val}")
        return False  # False = 不抑制异常；True = 吞掉异常

with ManagedResource("数据库连接") as res:
    print(f"  使用资源: {res.name}")

# --- 用 contextlib.contextmanager 装饰器实现（更简洁）---
@contextlib.contextmanager
def timer_ctx(label: str):
    """计时上下文管理器。"""
    start = time.perf_counter()
    print(f"  [{label}] 开始")
    try:
        yield       # with 块中的代码在这里执行
    finally:
        elapsed = time.perf_counter() - start
        print(f"  [{label}] 结束，耗时 {elapsed:.6f}s")

with timer_ctx("计算任务"):
    total = sum(range(1_000_000))
print(f"  sum(range(1_000_000)) = {total}")

# ============================================================
# 5. 类型联合 X | Y（Python 3.10+）
# ============================================================

print("\n=== 类型联合 X | Y ===")

# 函数参数和返回值的联合类型注解
def process(value: int | float | str | None) -> str:
    match value:
        case None:
            return "空值"
        case int() | float():
            return f"数值: {value}"
        case str():
            return f"字符串: {value!r}"

for v in [42, 3.14, "hello", None]:
    print(f"  process({v!r}) = {process(v)}")

# X | None 等价于 Optional[X]
def find_user(user_id: int) -> dict | None:
    db = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    return db.get(user_id)

for uid in [1, 99]:
    user = find_user(uid)
    print(f"  find_user({uid}) = {user}")

# 用于 isinstance 检查（Python 3.10+）
values = [42, "hello", 3.14, True]
for v in values:
    if isinstance(v, int | float):
        print(f"  {v!r} 是数值类型")
    elif isinstance(v, str):
        print(f"  {v!r} 是字符串")
