# Python 教学演示项目

> 适用版本：Python 3.10+
> 学习路径：从基础到高级，渐进式掌握 Python 核心知识点。

## 项目结构

每个章节目录下包含两个文件：
- `example.py` —— 知识点演示代码，可直接运行观察输出
- `exercise.py` —— 配套练习题，含答案注释

---

## 章节目录

| 章节 | 目录 | 核心知识点 |
|------|------|-----------|
| 第 01 章 | `01_basics` | 变量、注释、print/input、类型转换 |
| 第 02 章 | `02_data_types` | 数值/字符串/布尔/None、f-string、类型检查 |
| 第 03 章 | `03_operators_and_flow` | 运算符、if/elif/else、match/case |
| 第 04 章 | `04_loops` | for/while、break/continue/else、range/enumerate/zip |
| 第 05 章 | `05_data_structures` | list/tuple/set/dict、推导式、解包、walrus |
| 第 06 章 | `06_functions` | 函数定义、参数、lambda、类型注解、递归、闭包 |
| 第 07 章 | `07_modules_and_packages` | import、标准库 os/sys/math/random/datetime |
| 第 08 章 | `08_oop` | 类、继承、多态、property、dataclass |
| 第 09 章 | `09_exceptions` | try/except/finally、自定义异常、异常链 |
| 第 10 章 | `10_file_io` | 文件读写、csv、json、pathlib |
| 第 11 章 | `11_advanced` | 装饰器、生成器、迭代器、上下文管理器 |
| 第 12 章 | `12_stdlib_project` | 综合实战：命令行通讯录 |

---

## 快速开始

```bash
# 确认 Python 版本（需 3.10+）
python --version

# 运行任意示例
python 01_basics/example.py

# 完成练习后对比答案
python 01_basics/exercise.py
```

## 学习建议

1. 按章节顺序学习，每章先看 `example.py`，再独立完成 `exercise.py`
2. 遇到不理解的地方，可在代码中加 `print()` 打印中间结果
3. 第 12 章综合项目会用到前 11 章的所有知识，建议完成前面章节后再挑战
