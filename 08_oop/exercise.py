"""
第 08 章：练习题
请先独立完成，再查看下方答案注释。
"""

# ============================================================
# 练习 1：银行账户类
# 要求：设计 BankAccount 类
#   - 属性：owner（户主），balance（余额，初始为 0）
#   - 方法：deposit(amount) 存款、withdraw(amount) 取款
#     - 存款金额必须 > 0，否则抛出 ValueError
#     - 取款不能超过余额，否则抛出 ValueError
#   - @property balance：只读，不允许直接修改
#   - __str__：输出 "BankAccount[户主=Alice, 余额=1000.00]"
#   - 类方法 create_with_deposit(owner, amount) 创建并存入初始金额
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# class BankAccount:
#     def __init__(self, owner: str) -> None:
#         self.owner = owner
#         self._balance = 0.0
#
#     @property
#     def balance(self) -> float:
#         return self._balance
#
#     def deposit(self, amount: float) -> None:
#         if amount <= 0:
#             raise ValueError("存款金额必须大于0")
#         self._balance += amount
#         print(f"  存入 {amount:.2f}，余额: {self._balance:.2f}")
#
#     def withdraw(self, amount: float) -> None:
#         if amount <= 0:
#             raise ValueError("取款金额必须大于0")
#         if amount > self._balance:
#             raise ValueError(f"余额不足（余额: {self._balance:.2f}，取款: {amount:.2f}）")
#         self._balance -= amount
#         print(f"  取出 {amount:.2f}，余额: {self._balance:.2f}")
#
#     def __str__(self) -> str:
#         return f"BankAccount[户主={self.owner}, 余额={self._balance:.2f}]"
#
#     @classmethod
#     def create_with_deposit(cls, owner: str, amount: float) -> "BankAccount":
#         acc = cls(owner)
#         acc.deposit(amount)
#         return acc
#
# acc = BankAccount.create_with_deposit("Alice", 1000)
# print(acc)
# acc.deposit(500)
# acc.withdraw(200)
# try:
#     acc.withdraw(5000)
# except ValueError as e:
#     print(f"  错误: {e}")

# ============================================================
# 练习 2：图形类继承体系
# 要求：
#   - 抽象基类 Shape，有 area() 和 perimeter() 方法（只有 raise NotImplementedError）
#   - 子类 Rectangle(width, height)
#   - 子类 Triangle(a, b, c)  三边长，面积用海伦公式
#   - 子类 Circle(radius)
#   - 每个子类实现 __repr__ 和两个方法
#   - 创建一个列表存放不同图形，遍历输出每个图形的面积和周长
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# import math
#
# class Shape:
#     def area(self) -> float:
#         raise NotImplementedError
#     def perimeter(self) -> float:
#         raise NotImplementedError
#
# class Rectangle(Shape):
#     def __init__(self, width: float, height: float) -> None:
#         self.width = width
#         self.height = height
#     def area(self) -> float:
#         return self.width * self.height
#     def perimeter(self) -> float:
#         return 2 * (self.width + self.height)
#     def __repr__(self) -> str:
#         return f"Rectangle({self.width}x{self.height})"
#
# class Triangle(Shape):
#     def __init__(self, a: float, b: float, c: float) -> None:
#         self.a, self.b, self.c = a, b, c
#     def perimeter(self) -> float:
#         return self.a + self.b + self.c
#     def area(self) -> float:
#         s = self.perimeter() / 2
#         return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))
#     def __repr__(self) -> str:
#         return f"Triangle({self.a},{self.b},{self.c})"
#
# class Circle(Shape):
#     def __init__(self, radius: float) -> None:
#         self.radius = radius
#     def area(self) -> float:
#         return math.pi * self.radius ** 2
#     def perimeter(self) -> float:
#         return 2 * math.pi * self.radius
#     def __repr__(self) -> str:
#         return f"Circle(r={self.radius})"
#
# shapes: list[Shape] = [Rectangle(4, 6), Triangle(3, 4, 5), Circle(7)]
# for shape in shapes:
#     print(f"  {shape}: 面积={shape.area():.2f}, 周长={shape.perimeter():.2f}")

# ============================================================
# 练习 3：用 @dataclass 实现图书管理
# 要求：
#   - @dataclass Book(isbn, title, author, price, available=True)
#   - @dataclass Library，包含 books: list[Book]（默认空列表）
#   - Library 方法：
#     add_book(book)、find_by_author(author) -> list[Book]、
#     borrow(isbn) -> Book（将 available 设为 False）
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# from dataclasses import dataclass, field
#
# @dataclass
# class Book:
#     isbn: str
#     title: str
#     author: str
#     price: float
#     available: bool = True
#
# @dataclass
# class Library:
#     books: list[Book] = field(default_factory=list)
#
#     def add_book(self, book: Book) -> None:
#         self.books.append(book)
#
#     def find_by_author(self, author: str) -> list[Book]:
#         return [b for b in self.books if b.author == author]
#
#     def borrow(self, isbn: str) -> Book:
#         for book in self.books:
#             if book.isbn == isbn:
#                 if not book.available:
#                     raise ValueError(f"《{book.title}》已被借出")
#                 book.available = False
#                 return book
#         raise ValueError(f"未找到 ISBN={isbn} 的书")
#
# lib = Library()
# lib.add_book(Book("978-0001", "Python编程", "张三", 59.9))
# lib.add_book(Book("978-0002", "数据结构", "李四", 49.9))
# lib.add_book(Book("978-0003", "算法导论", "张三", 89.9))
# print(lib.find_by_author("张三"))
# book = lib.borrow("978-0001")
# print(f"借出: {book.title}")
# try:
#     lib.borrow("978-0001")
# except ValueError as e:
#     print(f"错误: {e}")
