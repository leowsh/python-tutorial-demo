"""
第 11 章：练习题
请先独立完成，再查看下方答案注释。
"""

# ============================================================
# 练习 1：缓存装饰器
# 要求：实现 @cache(maxsize) 装饰器，对函数结果进行缓存（LRU 策略）
#   - 使用 OrderedDict 记录（key=参数元组, value=结果）
#   - 超出 maxsize 时删除最旧的条目
#   - 每次调用打印 "[CACHE HIT]" 或 "[CACHE MISS]"
# 演示：将其应用到计算斐波那契的递归函数，观察命中情况
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# import functools
# from collections import OrderedDict
#
# def cache(maxsize: int = 128):
#     def decorator(func):
#         _cache: OrderedDict = OrderedDict()
#
#         @functools.wraps(func)
#         def wrapper(*args):
#             if args in _cache:
#                 print(f"  [CACHE HIT]  {func.__name__}{args}")
#                 _cache.move_to_end(args)   # 移到最末（最近使用）
#                 return _cache[args]
#             result = func(*args)
#             print(f"  [CACHE MISS] {func.__name__}{args} = {result}")
#             _cache[args] = result
#             if len(_cache) > maxsize:
#                 _cache.popitem(last=False)  # 删除最旧的
#             return result
#
#         wrapper.cache_info = lambda: f"size={len(_cache)}/{maxsize}"
#         return wrapper
#     return decorator
#
# @cache(maxsize=5)
# def fib(n: int) -> int:
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
# for i in [5, 6, 5]:
#     print(f"fib({i}) = {fib(i)}")
# print("缓存信息:", fib.cache_info())

# ============================================================
# 练习 2：无限范围生成器 + 管道
# 要求：
#   (a) 实现生成器 integers(start=0)：从 start 开始无限生成整数
#   (b) 实现生成器 take(n, iterable)：取前 n 个元素
#   (c) 实现生成器 where(pred, iterable)：过滤满足条件的元素
#   (d) 用管道组合：取 integers() 中前 10 个能被 3 整除的自然数
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# from collections.abc import Iterator
#
# def integers(start: int = 0) -> Iterator[int]:
#     n = start
#     while True:
#         yield n
#         n += 1
#
# def take(n: int, iterable) -> Iterator:
#     count = 0
#     for item in iterable:
#         if count >= n:
#             break
#         yield item
#         count += 1
#
# def where(pred, iterable) -> Iterator:
#     for item in iterable:
#         if pred(item):
#             yield item
#
# # 管道组合
# divisible_by_3 = take(10, where(lambda x: x % 3 == 0, integers(1)))
# print("前10个能被3整除的自然数:", list(divisible_by_3))

# ============================================================
# 练习 3：事务上下文管理器
# 要求：实现 @contextmanager transaction(name) 模拟数据库事务
#   - 进入 with 块时打印 "BEGIN TRANSACTION: <name>"
#   - 正常退出时打印 "COMMIT: <name>"
#   - 发生异常时打印 "ROLLBACK: <name>: <错误信息>"，并吞掉异常
# 演示：
#   with transaction("添加用户"): 执行成功的操作
#   with transaction("扣除余额"): raise ValueError("余额不足")
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# import contextlib
#
# @contextlib.contextmanager
# def transaction(name: str):
#     print(f"  BEGIN TRANSACTION: {name}")
#     try:
#         yield
#         print(f"  COMMIT: {name}")
#     except Exception as e:
#         print(f"  ROLLBACK: {name}: {e}")
#         # 不 re-raise，吞掉异常
#
# with transaction("添加用户"):
#     print("  执行: INSERT INTO users ...")
#
# with transaction("扣除余额"):
#     print("  执行: UPDATE accounts ...")
#     raise ValueError("余额不足")
#
# print("程序继续执行（事务异常已被吞掉）")
