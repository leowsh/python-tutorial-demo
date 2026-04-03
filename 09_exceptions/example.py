"""
第 09 章：异常处理
知识点：try/except/else/finally、多异常捕获、自定义异常类、raise、raise...from（异常链）
"""

# ============================================================
# 1. 基本 try / except
# ============================================================

print("=== 基本 try/except ===")

# 捕获除零错误
try:
    result = 10 / 0
except ZeroDivisionError:
    print("  捕获到除零错误")

# 捕获多个不同异常
def safe_parse(text: str):
    try:
        return int(text)
    except ValueError:
        print(f"  '{text}' 无法转为整数")
        return None
    except TypeError:
        print(f"  类型错误：{type(text)}")
        return None

safe_parse("123")
safe_parse("abc")
safe_parse(None)

# ============================================================
# 2. 获取异常对象 (as e)
# ============================================================

print("\n=== 获取异常对象 ===")

try:
    lst = [1, 2, 3]
    _ = lst[10]
except IndexError as e:
    print(f"  IndexError: {e}")
    print(f"  异常类型: {type(e).__name__}")

# ============================================================
# 3. else 子句（无异常时执行）
# ============================================================

print("\n=== try/except/else/finally ===")

def divide(a: float, b: float) -> float | None:
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"  [except] 除零错误: {e}")
        return None
    else:
        # 只有 try 没有抛异常时才执行
        print(f"  [else]   计算成功，结果 = {result}")
        return result
    finally:
        # 无论是否发生异常，总会执行（常用于资源清理）
        print(f"  [finally] 执行完毕（无论是否异常）")

print("divide(10, 2):")
divide(10, 2)
print("divide(10, 0):")
divide(10, 0)

# ============================================================
# 4. 捕获多个异常（同一 except）
# ============================================================

print("\n=== 同时捕获多个异常类型 ===")

def risky_operation(value):
    try:
        result = 100 / int(value)
        print(f"  结果: {result}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"  [{type(e).__name__}] {e}")

risky_operation("5")
risky_operation("abc")
risky_operation("0")

# ============================================================
# 5. 捕获所有异常（谨慎使用）
# ============================================================

print("\n=== 捕获所有异常 ===")

try:
    x = int("not a number")
except Exception as e:
    # Exception 是大多数内置异常的基类
    # 注意：不要用裸 except: 或 except BaseException（会屏蔽 KeyboardInterrupt）
    print(f"  捕获到: [{type(e).__name__}] {e}")

# ============================================================
# 6. raise 主动抛出异常
# ============================================================

print("\n=== raise ===")

def set_age(age: int) -> None:
    if not isinstance(age, int):
        raise TypeError(f"age 必须是整数，收到 {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"age 超出合理范围: {age}")
    print(f"  年龄设置为 {age}")

set_age(25)
try:
    set_age(-1)
except ValueError as e:
    print(f"  ValueError: {e}")
try:
    set_age("twenty")
except TypeError as e:
    print(f"  TypeError: {e}")

# re-raise：重新抛出当前异常
print()
def process():
    try:
        1 / 0
    except ZeroDivisionError:
        print("  记录日志：除零错误")
        raise    # 原样重新抛出

try:
    process()
except ZeroDivisionError:
    print("  外层捕获到重新抛出的异常")

# ============================================================
# 7. 自定义异常类
# ============================================================

print("\n=== 自定义异常 ===")

class AppError(Exception):
    """应用基础异常，所有自定义异常继承自此。"""
    pass


class ValidationError(AppError):
    """数据验证失败。"""
    def __init__(self, field: str, message: str) -> None:
        self.field = field
        self.message = message
        super().__init__(f"[{field}] {message}")


class NotFoundError(AppError):
    """资源未找到。"""
    def __init__(self, resource: str, identifier) -> None:
        self.resource = resource
        self.identifier = identifier
        super().__init__(f"{resource}（id={identifier}）未找到")


# 使用自定义异常
def create_user(name: str, age: int) -> dict:
    if not name:
        raise ValidationError("name", "姓名不能为空")
    if age < 0 or age > 150:
        raise ValidationError("age", f"年龄 {age} 超出范围")
    return {"name": name, "age": age}


for test in [("Alice", 25), ("", 25), ("Bob", 200)]:
    try:
        user = create_user(*test)
        print(f"  创建用户: {user}")
    except ValidationError as e:
        print(f"  ValidationError: {e} (field={e.field})")

# ============================================================
# 8. 异常链 raise...from
# ============================================================

print("\n=== 异常链 raise...from ===")

class DatabaseError(AppError):
    pass

def fetch_user_from_db(user_id: int) -> dict:
    """模拟数据库查询。"""
    raw_data = {"1": "Alice,25", "2": "Bob,30"}
    if str(user_id) not in raw_data:
        raise NotFoundError("用户", user_id)

    try:
        name, age_str = raw_data[str(user_id)].split(",")
        return {"name": name, "age": int(age_str)}
    except ValueError as e:
        # 用 raise...from 保留原始异常上下文
        raise DatabaseError(f"解析用户 {user_id} 数据失败") from e


for uid in [1, 2, 99]:
    try:
        user = fetch_user_from_db(uid)
        print(f"  用户 {uid}: {user}")
    except NotFoundError as e:
        print(f"  NotFoundError: {e}")
    except DatabaseError as e:
        print(f"  DatabaseError: {e}")
        if e.__cause__:
            print(f"    原始原因: {e.__cause__}")

# ============================================================
# 9. 异常层次结构（了解）
# ============================================================

print("\n=== 常见内置异常层次 ===")

common_exceptions = [
    ValueError, TypeError, KeyError, IndexError,
    AttributeError, FileNotFoundError, PermissionError,
    ZeroDivisionError, OverflowError, RecursionError,
]

for exc in common_exceptions:
    bases = [c.__name__ for c in exc.__mro__ if c not in (object,)]
    print(f"  {exc.__name__:25s} -> {' -> '.join(bases)}")
