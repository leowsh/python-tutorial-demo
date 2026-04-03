"""
第 03 章：练习题
请先独立完成，再查看下方答案注释。
"""

# ============================================================
# 练习 1：成绩等级判断
# 要求：用 if/elif/else 实现以下判断，对分数列表
#       [100, 92, 85, 76, 64, 55] 输出每个分数的等级
#   >= 90 -> A
#   >= 80 -> B
#   >= 70 -> C
#   >= 60 -> D
#   <  60 -> F
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# scores = [100, 92, 85, 76, 64, 55]
# for s in scores:
#     if s >= 90:
#         grade = "A"
#     elif s >= 80:
#         grade = "B"
#     elif s >= 70:
#         grade = "C"
#     elif s >= 60:
#         grade = "D"
#     else:
#         grade = "F"
#     print(f"  {s} -> {grade}")

# ============================================================
# 练习 2：用 match/case 实现 HTTP 状态码描述
# 要求：对 [200, 201, 301, 404, 500, 503] 使用 match/case
#       输出每个状态码的描述，未知状态码输出 "未知状态"
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# def describe_status(code: int) -> str:
#     match code:
#         case 200:
#             return "OK"
#         case 201:
#             return "Created"
#         case 301:
#             return "Moved Permanently"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "Internal Server Error"
#         case 503:
#             return "Service Unavailable"
#         case _:
#             return "未知状态"
#
# for c in [200, 201, 301, 404, 500, 503, 418]:
#     print(f"  {c} -> {describe_status(c)}")

# ============================================================
# 练习 3：BMI 计算器
# 公式：bmi = weight(kg) / height(m)^2
# 判断标准：
#   < 18.5  -> 偏瘦
#   < 24.0  -> 正常
#   < 28.0  -> 超重
#   >= 28.0 -> 肥胖
# 要求：对 [(50, 1.65), (70, 1.75), (90, 1.70), (120, 1.68)] 输出 BMI 值及分类
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# data = [(50, 1.65), (70, 1.75), (90, 1.70), (120, 1.68)]
# for weight, height in data:
#     bmi = weight / height ** 2
#     if bmi < 18.5:
#         category = "偏瘦"
#     elif bmi < 24.0:
#         category = "正常"
#     elif bmi < 28.0:
#         category = "超重"
#     else:
#         category = "肥胖"
#     print(f"  体重={weight}kg, 身高={height}m, BMI={bmi:.1f} -> {category}")
