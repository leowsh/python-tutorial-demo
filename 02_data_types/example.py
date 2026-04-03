"""
第 02 章：Python 数据类型
知识点：int/float/complex、bool、None、字符串切片/方法、f-string 格式化、isinstance()
"""

# ============================================================
# 1. 数值类型
# ============================================================

print("=== 数值类型 ===")

# 整数（int）：任意精度
i = 1_000_000        # 下划线分隔提升可读性
print(f"整数: {i}, 类型: {type(i).__name__}")

# 不同进制
print(f"二进制 0b1010 = {0b1010}")
print(f"八进制 0o17   = {0o17}")
print(f"十六进制 0xFF = {0xFF}")

# 浮点数（float）：IEEE 754 双精度
f = 3.14
sci = 2.5e-3         # 科学计数法，等于 0.0025
print(f"浮点: {f}, 科学计数: {sci}")

# 浮点精度问题
print(f"0.1 + 0.2 = {0.1 + 0.2}")       # 经典精度问题
import decimal
print(f"Decimal 精确计算: {decimal.Decimal('0.1') + decimal.Decimal('0.2')}")

# 复数（complex）
c = 3 + 4j
print(f"复数: {c}, 实部: {c.real}, 虚部: {c.imag}, 模: {abs(c)}")

# ============================================================
# 2. 布尔值（bool）
# ============================================================

print("\n=== 布尔值 ===")

t = True
f_val = False
print(f"True and False = {t and f_val}")
print(f"True or False  = {t or f_val}")
print(f"not True       = {not t}")

# bool 是 int 的子类
print(f"True + True = {True + True}")    # 2
print(f"True * 5    = {True * 5}")       # 5
print(f"isinstance(True, int) = {isinstance(True, int)}")

# ============================================================
# 3. None
# ============================================================

print("\n=== None ===")

result = None
print(f"result = {result}, 类型: {type(result).__name__}")

# 判断 None 应使用 is，不用 ==
if result is None:
    print("result 是 None")

# ============================================================
# 4. 字符串（str）
# ============================================================

print("\n=== 字符串 ===")

s = "Hello, Python!"

# 索引和切片 [start:stop:step]
print(f"s[0]      = {s[0]}")          # H
print(f"s[-1]     = {s[-1]}")         # !
print(f"s[0:5]    = {s[0:5]}")        # Hello
print(f"s[7:]     = {s[7:]}")         # Python!
print(f"s[::-1]   = {s[::-1]}")       # 反转

# 常用字符串方法
print(f"\n字符串方法演示:")
text = "  Hello, World!  "
print(f"  原始: '{text}'")
print(f"  strip():    '{text.strip()}'")
print(f"  upper():    '{text.strip().upper()}'")
print(f"  lower():    '{text.strip().lower()}'")
print(f"  replace():  '{text.strip().replace('World', 'Python')}'")
print(f"  split():    {text.strip().split(', ')}")
print(f"  startswith: {text.strip().startswith('Hello')}")
print(f"  find():     {text.strip().find('World')}")
print(f"  count():    {'aababc'.count('ab')}")

# join
words = ["Python", "is", "fun"]
print(f"  join():     {' '.join(words)}")

# 多行字符串
multi = """第一行
第二行
第三行"""
print(f"\n多行字符串行数: {len(multi.splitlines())}")

# ============================================================
# 5. f-string 高级格式化
# ============================================================

print("\n=== f-string 格式化 ===")

pi = 3.14159265
name = "Alice"
score = 98

# 精度与宽度
print(f"pi = {pi:.4f}")                 # 4 位小数
print(f"pi = {pi:10.4f}")              # 宽度 10，右对齐
print(f"pi = {pi:<10.4f}|")            # 左对齐
print(f"pi = {pi:^10.4f}|")            # 居中

# 整数格式
print(f"score = {score:05d}")           # 补零，宽度 5
print(f"255   = {255:#010x}")           # 十六进制带前缀，宽度 10

# 表达式
print(f"1 + 1 = {1 + 1}")
print(f"name 大写: {name.upper()}")

# = 调试格式（Python 3.8+）
x = 42
print(f"{x = }")                        # 输出 x = 42

# ============================================================
# 6. isinstance() 类型检查
# ============================================================

print("\n=== isinstance() 类型检查 ===")

values = [42, 3.14, "hello", True, None, [1, 2]]
for v in values:
    if isinstance(v, bool):
        print(f"  {repr(v):15s} -> bool")
    elif isinstance(v, int):
        print(f"  {repr(v):15s} -> int")
    elif isinstance(v, float):
        print(f"  {repr(v):15s} -> float")
    elif isinstance(v, str):
        print(f"  {repr(v):15s} -> str")
    elif v is None:
        print(f"  {repr(v):15s} -> NoneType")
    elif isinstance(v, list):
        print(f"  {repr(v):15s} -> list")

# 联合类型检查
print(f"\n42 是 int 或 float: {isinstance(42, (int, float))}")
print(f"3.14 是 int 或 float: {isinstance(3.14, (int, float))}")
