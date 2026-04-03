"""
第 04 章：循环
知识点：for/while、break/continue/else、range()、enumerate()、zip()
"""

# ============================================================
# 1. for 循环
# ============================================================

print("=== for 循环 ===")

# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  {fruit}")

# 遍历字符串
print()
for ch in "Python":
    print(ch, end=" ")
print()

# 遍历字典
print()
person = {"name": "Alice", "age": 20, "city": "Beijing"}
for key, value in person.items():
    print(f"  {key}: {value}")

# ============================================================
# 2. range()
# ============================================================

print("\n=== range() ===")

# range(stop)
print("range(5):", list(range(5)))

# range(start, stop)
print("range(2, 7):", list(range(2, 7)))

# range(start, stop, step)
print("range(0, 10, 2):", list(range(0, 10, 2)))
print("range(10, 0, -2):", list(range(10, 0, -2)))

# 用 range 遍历索引
letters = ["a", "b", "c", "d"]
for i in range(len(letters)):
    print(f"  letters[{i}] = {letters[i]}")

# ============================================================
# 3. enumerate() — 同时获取索引和值
# ============================================================

print("\n=== enumerate() ===")

colors = ["red", "green", "blue"]

# 默认从 0 开始
for idx, color in enumerate(colors):
    print(f"  {idx}: {color}")

# 指定起始值
print()
for idx, color in enumerate(colors, start=1):
    print(f"  第{idx}个颜色: {color}")

# ============================================================
# 4. zip() — 并行遍历多个序列
# ============================================================

print("\n=== zip() ===")

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
grades = ["B", "A", "C"]

for name, score, grade in zip(names, scores, grades):
    print(f"  {name}: {score}分，等级 {grade}")

# zip 遇到最短序列停止
short = [1, 2]
long_ = [10, 20, 30, 40]
print("zip 停止于最短:", list(zip(short, long_)))

# zip 配合 dict()
keys = ["a", "b", "c"]
vals = [1, 2, 3]
d = dict(zip(keys, vals))
print(f"dict(zip): {d}")

# ============================================================
# 5. while 循环
# ============================================================

print("\n=== while 循环 ===")

# 基本用法
count = 0
while count < 5:
    print(f"  count = {count}")
    count += 1

# 模拟 do-while（至少执行一次）
print()
n = 0
while True:
    n += 1
    if n >= 3:
        break
print(f"  n 最终值 = {n}")

# ============================================================
# 6. break / continue
# ============================================================

print("\n=== break / continue ===")

# break：立即退出循环
print("break 示例：找到第一个偶数")
numbers = [1, 3, 5, 4, 7, 8]
for n in numbers:
    if n % 2 == 0:
        print(f"  找到偶数: {n}")
        break

# continue：跳过当前迭代
print("\ncontinue 示例：跳过偶数")
for n in range(1, 10):
    if n % 2 == 0:
        continue
    print(n, end=" ")
print()

# ============================================================
# 7. 循环的 else 子句
# ============================================================

print("\n=== 循环 else 子句 ===")

# else 在循环正常结束（未被 break）后执行
def find_prime(nums):
    for n in nums:
        if n < 2:
            continue
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                break          # 找到因数，不是质数
        else:
            print(f"  {n} 是质数")  # 内层循环未 break → 是质数

find_prime([2, 3, 4, 5, 9, 11])

# while 的 else
print()
target = 7
x = 0
while x < 5:
    if x == target:
        print(f"找到 {target}")
        break
    x += 1
else:
    print(f"  未在 [0,5) 中找到 {target}，循环正常结束")

# ============================================================
# 8. 嵌套循环 + 列表推导式预览
# ============================================================

print("\n=== 嵌套循环 ===")

# 乘法表
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i}×{j}={i*j}", end="  ")
    print()
