"""
第 07 章：练习题
请先独立完成，再查看下方答案注释。
"""

# ============================================================
# 练习 1：文件路径工具
# 要求：给定路径列表
#   paths = [
#       "C:/Users/Alice/Documents/report.pdf",
#       "/home/bob/projects/app/main.py",
#       "D:/data/images/photo.jpg",
#   ]
# 用 os.path 对每个路径输出：目录名、文件名、扩展名
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# import os
# paths = [
#     "C:/Users/Alice/Documents/report.pdf",
#     "/home/bob/projects/app/main.py",
#     "D:/data/images/photo.jpg",
# ]
# for p in paths:
#     dirname = os.path.dirname(p)
#     basename = os.path.basename(p)
#     name, ext = os.path.splitext(basename)
#     print(f"  路径: {p}")
#     print(f"    目录: {dirname}  文件名: {name}  扩展名: {ext}")

# ============================================================
# 练习 2：随机密码生成器
# 要求：用 random 和 string 模块编写函数 generate_password(length=12)
#   - 密码包含大写字母、小写字母、数字、特殊字符(!@#$%^&*)
#   - 确保每种字符至少出现一次
#   - 返回随机顺序的密码字符串
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# import random
# import string
#
# def generate_password(length: int = 12) -> str:
#     if length < 4:
#         raise ValueError("密码长度至少为4")
#     special = "!@#$%^&*"
#     # 确保每类至少一个
#     pwd = [
#         random.choice(string.ascii_uppercase),
#         random.choice(string.ascii_lowercase),
#         random.choice(string.digits),
#         random.choice(special),
#     ]
#     # 补充剩余长度
#     all_chars = string.ascii_letters + string.digits + special
#     pwd += random.choices(all_chars, k=length - 4)
#     random.shuffle(pwd)
#     return "".join(pwd)
#
# for _ in range(3):
#     print(f"  密码: {generate_password()}")

# ============================================================
# 练习 3：日期计算工具
# 要求：编写函数 date_info(birth_str: str)，输入格式 "YYYY-MM-DD"，
#   输出：
#   - 年龄（岁）
#   - 距下一个生日还有多少天
#   - 是否为闰年出生
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# from datetime import date
#
# def date_info(birth_str: str) -> None:
#     birth = date.fromisoformat(birth_str)
#     today = date.today()
#     age = today.year - birth.year - (
#         (today.month, today.day) < (birth.month, birth.day)
#     )
#     # 下一个生日
#     try:
#         next_birthday = birth.replace(year=today.year)
#     except ValueError:
#         # 2月29日在非闰年用3月1日代替
#         next_birthday = date(today.year, 3, 1)
#     if next_birthday < today:
#         try:
#             next_birthday = birth.replace(year=today.year + 1)
#         except ValueError:
#             next_birthday = date(today.year + 1, 3, 1)
#     days_to_birthday = (next_birthday - today).days
#     # 是否闰年
#     import calendar
#     is_leap = calendar.isleap(birth.year)
#     print(f"  出生日期: {birth_str}")
#     print(f"  年龄: {age} 岁")
#     print(f"  距下次生日: {days_to_birthday} 天")
#     print(f"  出生年是否为闰年: {is_leap}")
#
# date_info("2000-02-29")
# date_info("1995-08-20")
