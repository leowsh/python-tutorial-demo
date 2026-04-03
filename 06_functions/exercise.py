"""
第 06 章：练习题
请先独立完成，再查看下方答案注释。
"""

# ============================================================
# 练习 1：灵活的统计函数
# 要求：编写函数 stats(*numbers, precision=2)
#   - 接收任意数量的数值
#   - 返回字典，包含 min/max/avg/total 四个键
#   - avg 保留 precision 位小数
# 示例：stats(3, 1, 4, 1, 5, 9) ->
#   {'min': 1, 'max': 9, 'avg': 3.83, 'total': 23}
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# def stats(*numbers: int | float, precision: int = 2) -> dict:
#     total = sum(numbers)
#     avg = round(total / len(numbers), precision)
#     return {"min": min(numbers), "max": max(numbers), "avg": avg, "total": total}
#
# print(stats(3, 1, 4, 1, 5, 9))
# print(stats(10, 20, 30, precision=1))

# ============================================================
# 练习 2：用递归实现汉诺塔
# 要求：实现函数 hanoi(n, from_peg, to_peg, via_peg)
#   输出将 n 个盘子从 from_peg 移到 to_peg 的每一步
# 示例（n=3）：
#   移动盘子 1: A -> C
#   移动盘子 2: A -> B
#   ...
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# def hanoi(n: int, from_peg: str, to_peg: str, via_peg: str) -> None:
#     if n == 1:
#         print(f"  移动盘子 {n}: {from_peg} -> {to_peg}")
#         return
#     hanoi(n - 1, from_peg, via_peg, to_peg)
#     print(f"  移动盘子 {n}: {from_peg} -> {to_peg}")
#     hanoi(n - 1, via_peg, to_peg, from_peg)
#
# hanoi(3, "A", "C", "B")

# ============================================================
# 练习 3：函数式编程——数据处理管道
# 有学生数据：
#   students = [
#       {"name": "Alice", "score": 88, "dept": "CS"},
#       {"name": "Bob",   "score": 73, "dept": "Math"},
#       {"name": "Carol", "score": 95, "dept": "CS"},
#       {"name": "Dave",  "score": 61, "dept": "Math"},
#       {"name": "Eve",   "score": 90, "dept": "CS"},
#   ]
# 要求：用 filter + map + sorted（均用 lambda）完成：
#   1. 筛选 CS 系且分数 >= 85 的学生
#   2. 提取姓名和分数
#   3. 按分数降序排列
#   4. 输出 "Carol: 95, Eve: 90, Alice: 88"
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# students = [
#     {"name": "Alice", "score": 88, "dept": "CS"},
#     {"name": "Bob",   "score": 73, "dept": "Math"},
#     {"name": "Carol", "score": 95, "dept": "CS"},
#     {"name": "Dave",  "score": 61, "dept": "Math"},
#     {"name": "Eve",   "score": 90, "dept": "CS"},
# ]
# result = sorted(
#     map(
#         lambda s: (s["name"], s["score"]),
#         filter(lambda s: s["dept"] == "CS" and s["score"] >= 85, students)
#     ),
#     key=lambda x: x[1],
#     reverse=True
# )
# print(", ".join(f"{name}: {score}" for name, score in result))
