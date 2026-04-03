"""
第 05 章：练习题
请先独立完成，再查看下方答案注释。
"""

# ============================================================
# 练习 1：词频统计
# 有句子 sentence = "the quick brown fox jumps over the lazy dog the fox"
# 要求：用字典统计每个单词出现的次数，
#       然后输出出现次数最多的 3 个单词（按次数降序）
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# sentence = "the quick brown fox jumps over the lazy dog the fox"
# freq = {}
# for word in sentence.split():
#     freq[word] = freq.get(word, 0) + 1
# top3 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3]
# for word, count in top3:
#     print(f"  '{word}': {count}次")

# ============================================================
# 练习 2：列表去重并保持顺序
# 有列表 nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# 要求：去除重复元素，保持第一次出现的顺序，输出结果
# 提示：可以用 set 记录已见过的元素
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# seen = set()
# result = []
# for n in nums:
#     if n not in seen:
#         seen.add(n)
#         result.append(n)
# print(f"去重后保持顺序: {result}")

# ============================================================
# 练习 3：矩阵转置
# 有矩阵 matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 要求：用列表推导式实现矩阵转置（行变列），输出：
#   [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transposed = [[matrix[row][col] for row in range(len(matrix))]
#               for col in range(len(matrix[0]))]
# for row in transposed:
#     print(f"  {row}")
# # 也可以用 zip：
# # transposed2 = [list(row) for row in zip(*matrix)]
