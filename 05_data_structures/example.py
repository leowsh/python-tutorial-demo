"""
第 05 章：数据结构
知识点：list/tuple/set/dict 增删改查、推导式、嵌套结构、解包、walrus 运算符 :=
"""

# ============================================================
# 1. 列表（list）
# ============================================================

print("=== 列表 ===")

lst = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"原始列表: {lst}")

# 增
lst.append(7)           # 末尾追加
lst.insert(0, 0)        # 指定位置插入
lst.extend([8, 8])      # 追加另一个可迭代对象
print(f"增加后: {lst}")

# 删
lst.remove(1)           # 删除第一个匹配的值
popped = lst.pop()      # 弹出末尾元素
popped_idx = lst.pop(0) # 弹出指定索引元素
print(f"删除后: {lst}, pop()={popped}, pop(0)={popped_idx}")

# 改
lst[0] = 100
print(f"修改后: {lst}")

# 查
print(f"index(4): {lst.index(4)}")
print(f"count(8): {lst.count(8)}")
print(f"5 in lst: {5 in lst}")

# 排序
lst.sort()              # 原地排序（升序）
print(f"sort(): {lst}")
lst.sort(reverse=True)  # 降序
print(f"sort(reverse=True): {lst}")
print(f"sorted()（不修改原列表）: {sorted([3,1,2])}")

# 反转
lst.reverse()
print(f"reverse(): {lst}")

# ============================================================
# 2. 元组（tuple）
# ============================================================

print("\n=== 元组 ===")

t = (1, 2, 3, 4, 5)
print(f"元组: {t}")
print(f"t[1:3]: {t[1:3]}")
print(f"t.count(1): {t.count(1)}")
print(f"t.index(3): {t.index(3)}")

# 元组不可修改
# t[0] = 10  # TypeError

# 单元素元组必须有逗号
single = (42,)
not_tuple = (42)   # 这是整数，不是元组
print(f"单元素元组: {type(single).__name__}, 无逗号: {type(not_tuple).__name__}")

# 元组解包
x, y, z = (10, 20, 30)
print(f"解包: x={x}, y={y}, z={z}")

first, *rest = (1, 2, 3, 4, 5)
print(f"* 收集剩余: first={first}, rest={rest}")

# ============================================================
# 3. 集合（set）
# ============================================================

print("\n=== 集合 ===")

s = {3, 1, 4, 1, 5, 9, 2, 6}    # 自动去重
print(f"集合（去重）: {s}")

# 增
s.add(7)
s.update([10, 11])
print(f"add/update: {s}")

# 删
s.discard(99)           # 删除不存在的元素不报错
s.remove(10)            # 删除不存在的元素报 KeyError
print(f"discard/remove: {s}")

# 集合运算
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(f"a={a}, b={b}")
print(f"交集 a & b:       {a & b}")
print(f"并集 a | b:       {a | b}")
print(f"差集 a - b:       {a - b}")
print(f"对称差 a ^ b:     {a ^ b}")
print(f"a.issubset({{1,2,3,4,5,6}}): {a.issubset({1,2,3,4,5,6})}")

# ============================================================
# 4. 字典（dict）
# ============================================================

print("\n=== 字典 ===")

d = {"name": "Alice", "age": 20, "score": 95.5}
print(f"字典: {d}")

# 增/改
d["email"] = "alice@example.com"    # 新增
d["age"] = 21                        # 修改
print(f"增/改后: {d}")

# 查
print(f"d['name']: {d['name']}")
print(f"d.get('phone', '无'): {d.get('phone', '无')}")   # 安全取值，提供默认值

# 删
del d["email"]
removed = d.pop("score")
print(f"删除后: {d}, pop score={removed}")

# 遍历
print("\n遍历字典:")
info = {"语文": 88, "数学": 95, "英语": 82}
for key in info:
    print(f"  {key}: {info[key]}")
print("items():", list(info.items()))
print("keys():", list(info.keys()))
print("values():", list(info.values()))

# setdefault / update
info.setdefault("物理", 90)    # 仅在键不存在时设置
info.update({"化学": 78, "生物": 85})
print(f"setdefault/update: {info}")

# ============================================================
# 5. 推导式
# ============================================================

print("\n=== 推导式 ===")

# 列表推导式
squares = [x**2 for x in range(1, 6)]
print(f"列表推导式: {squares}")

# 带条件过滤
evens = [x for x in range(20) if x % 2 == 0]
print(f"偶数推导式: {evens}")

# 嵌套推导式（矩阵展平）
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [n for row in matrix for n in row]
print(f"矩阵展平: {flat}")

# 字典推导式
word_len = {word: len(word) for word in ["apple", "banana", "cherry"]}
print(f"字典推导式: {word_len}")

# 集合推导式
unique_squares = {x**2 for x in [-3, -2, -1, 0, 1, 2, 3]}
print(f"集合推导式: {unique_squares}")

# 生成器表达式（不建立完整列表，节省内存）
gen = (x**2 for x in range(10))
print(f"生成器求和: {sum(gen)}")

# ============================================================
# 6. 嵌套数据结构
# ============================================================

print("\n=== 嵌套数据结构 ===")

students = [
    {"name": "Alice", "scores": [85, 92, 78]},
    {"name": "Bob",   "scores": [70, 88, 95]},
    {"name": "Carol", "scores": [91, 76, 83]},
]

for stu in students:
    avg = sum(stu["scores"]) / len(stu["scores"])
    print(f"  {stu['name']}: 平均分 {avg:.1f}")

# ============================================================
# 7. 解包
# ============================================================

print("\n=== 解包 ===")

# * 解包列表
first, *middle, last = [1, 2, 3, 4, 5]
print(f"first={first}, middle={middle}, last={last}")

# ** 解包字典（用于函数调用）
def show_profile(name, age, city="未知"):
    print(f"  姓名={name}, 年龄={age}, 城市={city}")

profile = {"name": "Bob", "age": 25, "city": "Shanghai"}
show_profile(**profile)

# 合并字典（Python 3.9+: d1 | d2；通用方式用 **）
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}
merged = {**d1, **d2}   # d2 中的 b 覆盖 d1 中的 b
print(f"合并字典: {merged}")

# ============================================================
# 8. walrus 运算符 :=（Python 3.8+）
# ============================================================

print("\n=== walrus 运算符 := ===")

# 在 while 中避免重复读取
import random
random.seed(42)
values_collected = []
while (val := random.randint(1, 10)) != 5:
    values_collected.append(val)
    if len(values_collected) >= 10:
        break
print(f"收集的值（直到遇到5）: {values_collected}")

# 在推导式中复用计算结果
data = [2, 8, 3, 15, 4, 7, 12]
# 找出平方大于50的数，同时返回平方值
result = [(x, sq) for x in data if (sq := x**2) > 50]
print(f"平方>50 的数及其平方: {result}")
