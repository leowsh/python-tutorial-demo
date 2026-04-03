"""
第 02 章：练习题
请先独立完成，再查看下方答案注释。
"""

# ============================================================
# 练习 1：字符串处理
# 有字符串 s = "  Python3.10 is awesome!  "
# 要求：
#   (a) 去除首尾空格
#   (b) 将 "3.10" 替换为 "3.12"
#   (c) 转为大写并输出
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# s = "  Python3.10 is awesome!  "
# result = s.strip().replace("3.10", "3.12").upper()
# print(result)

# ============================================================
# 练习 2：f-string 格式化表格
# 有以下数据：
#   products = [("苹果", 3.5, 10), ("香蕉", 1.2, 25), ("橙子", 2.8, 15)]
# 用 f-string 输出对齐的表格（左对齐商品名，右对齐数量，保留1位小数的价格）：
#   苹果   3.5   10
#   香蕉   1.2   25
#   橙子   2.8   15
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# products = [("苹果", 3.5, 10), ("香蕉", 1.2, 25), ("橙子", 2.8, 15)]
# print(f"{'商品':<6} {'单价':>6} {'数量':>6}")
# print("-" * 20)
# for name, price, qty in products:
#     print(f"{name:<6} {price:>6.1f} {qty:>6}")

# ============================================================
# 练习 3：类型判断函数
# 要求：编写代码，对列表 [42, 3.14, "hi", True, None, [1,2], (3,4)]
#       中的每个值，使用 isinstance() 判断类型，输出格式：
#       "42 -> int"  "3.14 -> float" ...
#       注意：True/False 应识别为 bool 而非 int
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# data = [42, 3.14, "hi", True, None, [1, 2], (3, 4)]
# for v in data:
#     if isinstance(v, bool):
#         label = "bool"
#     elif isinstance(v, int):
#         label = "int"
#     elif isinstance(v, float):
#         label = "float"
#     elif isinstance(v, str):
#         label = "str"
#     elif v is None:
#         label = "NoneType"
#     elif isinstance(v, list):
#         label = "list"
#     elif isinstance(v, tuple):
#         label = "tuple"
#     else:
#         label = "unknown"
#     print(f"{repr(v)} -> {label}")
