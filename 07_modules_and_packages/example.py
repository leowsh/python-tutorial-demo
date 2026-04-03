"""
第 07 章：模块与包
知识点：import、from...import、别名、__name__=="__main__"、
        标准库 os/sys/math/random/datetime
"""

# ============================================================
# 1. import 方式
# ============================================================

print("=== import 方式 ===")

# 方式一：import 模块
import math
print(f"math.pi  = {math.pi}")
print(f"math.e   = {math.e}")
print(f"math.sqrt(2) = {math.sqrt(2):.6f}")

# 方式二：import 模块 as 别名
import math as m
print(f"m.ceil(3.2)  = {m.ceil(3.2)}")
print(f"m.floor(3.9) = {m.floor(3.9)}")

# 方式三：from 模块 import 指定名称
from math import sin, cos, pi, log, factorial

print(f"sin(pi/2)    = {sin(pi/2)}")
print(f"cos(0)       = {cos(0)}")
print(f"log(100, 10) = {log(100, 10)}")
print(f"factorial(5) = {factorial(5)}")

# 方式四：from 模块 import * （不推荐，可能污染命名空间）
# from math import *   # 不推荐

# ============================================================
# 2. os 模块
# ============================================================

print("\n=== os 模块 ===")

import os

# 路径操作
cwd = os.getcwd()
print(f"当前目录: {cwd}")

# os.path 路径工具
path = os.path.join("folder", "subfolder", "file.txt")
print(f"path.join: {path}")
print(f"path.dirname:  {os.path.dirname(path)}")
print(f"path.basename: {os.path.basename(path)}")
print(f"path.splitext: {os.path.splitext(path)}")
print(f"path.exists(cwd): {os.path.exists(cwd)}")

# 环境变量
home = os.environ.get("USERPROFILE") or os.environ.get("HOME", "未知")
print(f"HOME: {home}")

# 列出目录内容
entries = os.listdir(".")[:5]
print(f"当前目录前5项: {entries}")

# ============================================================
# 3. sys 模块
# ============================================================

print("\n=== sys 模块 ===")

import sys

print(f"Python 版本: {sys.version.split()[0]}")
print(f"平台: {sys.platform}")
print(f"最大整数: {sys.maxsize}")
print(f"默认编码: {sys.getdefaultencoding()}")
print(f"sys.path 前3条: {sys.path[:3]}")

# ============================================================
# 4. math 模块（进阶）
# ============================================================

print("\n=== math 模块 ===")

import math

print(f"math.gcd(48, 18) = {math.gcd(48, 18)}")
print(f"math.lcm(4, 6)   = {math.lcm(4, 6)}")
print(f"math.comb(5, 2)  = {math.comb(5, 2)}")    # 组合数 C(5,2)
print(f"math.perm(5, 2)  = {math.perm(5, 2)}")    # 排列数 P(5,2)
print(f"math.isnan(float('nan')) = {math.isnan(float('nan'))}")
print(f"math.isinf(float('inf')) = {math.isinf(float('inf'))}")

# ============================================================
# 5. random 模块
# ============================================================

print("\n=== random 模块 ===")

import random

random.seed(2024)    # 固定种子，结果可重现

print(f"random()              = {random.random():.4f}")      # [0.0, 1.0)
print(f"randint(1, 10)        = {random.randint(1, 10)}")     # [1, 10]
print(f"randrange(0, 10, 2)   = {random.randrange(0, 10, 2)}")  # 偶数
print(f"uniform(1.0, 5.0)     = {random.uniform(1.0, 5.0):.4f}")

# 序列操作
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"choice(items)         = {random.choice(items)}")     # 随机选一个
print(f"sample(items, 3)      = {random.sample(items, 3)}")  # 无重复抽样

shuffled = items[:]
random.shuffle(shuffled)
print(f"shuffle:               {shuffled}")

# ============================================================
# 6. datetime 模块
# ============================================================

print("\n=== datetime 模块 ===")

from datetime import datetime, date, timedelta

# 当前时间
now = datetime.now()
print(f"现在: {now}")
print(f"格式化: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 日期解析
dt = datetime.strptime("2024-01-15 09:30:00", "%Y-%m-%d %H:%M:%S")
print(f"解析: {dt}")

# 日期计算
today = date.today()
one_week_later = today + timedelta(weeks=1)
print(f"今天: {today}")
print(f"一周后: {one_week_later}")

# 时间差
birthday = date(2000, 6, 15)
age_days = (today - birthday).days
print(f"距 2000-06-15 已过: {age_days} 天（约 {age_days//365} 岁）")

# ============================================================
# 7. __name__ == "__main__" 保护
# ============================================================

print("\n=== __name__ 保护 ===")

# 当本文件作为主程序运行时，__name__ == "__main__"
# 当本文件被其他模块 import 时，__name__ == "07_modules_and_packages.example"
# 这样可以防止导入时意外执行测试代码

print(f"当前 __name__ = {__name__!r}")

if __name__ == "__main__":
    print("本文件作为主程序运行")
    # 通常把测试/演示代码放在这里
