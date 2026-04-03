"""
第 08 章：面向对象编程（OOP）
知识点：类定义、__init__、实例/类属性、继承与 super()、多态、
        @property/@classmethod/@staticmethod、__str__/__repr__、@dataclass
"""

from __future__ import annotations
from dataclasses import dataclass, field

# ============================================================
# 1. 基本类定义
# ============================================================

print("=== 基本类定义 ===")

class Animal:
    # 类属性（所有实例共享）
    kingdom: str = "Animalia"
    _count: int = 0       # 约定：下划线开头表示"内部使用"

    def __init__(self, name: str, age: int) -> None:
        # 实例属性（每个实例独立）
        self.name = name
        self.age = age
        Animal._count += 1

    # 实例方法
    def speak(self) -> str:
        return f"{self.name} 发出声音"

    # __str__：面向用户的可读字符串（print 时调用）
    def __str__(self) -> str:
        return f"Animal(name={self.name!r}, age={self.age})"

    # __repr__：面向开发者的详细字符串（调试时使用）
    def __repr__(self) -> str:
        return f"Animal(name={self.name!r}, age={self.age!r})"

    # 类方法：操作类属性，cls 代表类本身
    @classmethod
    def get_count(cls) -> int:
        return cls._count

    # 静态方法：与类相关但不需要访问类/实例属性
    @staticmethod
    def is_valid_age(age: int) -> bool:
        return 0 <= age <= 100


a1 = Animal("猫咪", 3)
a2 = Animal("小狗", 5)
print(a1)
print(repr(a2))
print(f"speak: {a1.speak()}")
print(f"类属性 kingdom: {Animal.kingdom}")
print(f"动物总数: {Animal.get_count()}")
print(f"is_valid_age(5): {Animal.is_valid_age(5)}")

# ============================================================
# 2. 继承与 super()
# ============================================================

print("\n=== 继承 ===")

class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(name, age)    # 调用父类 __init__
        self.breed = breed

    def speak(self) -> str:           # 方法重写（Override）
        return f"{self.name}（{self.breed}）: 汪汪汪！"

    def fetch(self, item: str) -> str:
        return f"{self.name} 捡回了 {item}"

    def __str__(self) -> str:
        return f"Dog(name={self.name!r}, breed={self.breed!r}, age={self.age})"


class Cat(Animal):
    def __init__(self, name: str, age: int, indoor: bool = True) -> None:
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self) -> str:
        return f"{self.name}: 喵～"


dog = Dog("旺财", 2, "金毛")
cat = Cat("奶茶", 1)

print(dog)
print(f"dog.speak(): {dog.speak()}")
print(f"dog.fetch(): {dog.fetch('球')}")
print(f"cat.speak(): {cat.speak()}")

# isinstance / issubclass
print(f"\nisinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"isinstance(dog, Cat):    {isinstance(dog, Cat)}")
print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")

# ============================================================
# 3. 多态
# ============================================================

print("\n=== 多态 ===")

animals: list[Animal] = [
    Dog("小黑", 3, "拉布拉多"),
    Cat("雪球", 2),
    Animal("鸟儿", 1),
]

for animal in animals:
    # 同一方法调用，根据实际类型执行不同实现
    print(f"  {animal.speak()}")

# ============================================================
# 4. @property
# ============================================================

print("\n=== @property ===")

class Circle:
    def __init__(self, radius: float) -> None:
        self._radius = radius     # 私有属性用下划线前缀

    @property
    def radius(self) -> float:
        """半径（只读）"""
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value < 0:
            raise ValueError("半径不能为负数")
        self._radius = value

    @property
    def area(self) -> float:
        """面积（计算属性，只读）"""
        import math
        return math.pi * self._radius ** 2

    @property
    def perimeter(self) -> float:
        """周长"""
        import math
        return 2 * math.pi * self._radius

    def __repr__(self) -> str:
        return f"Circle(radius={self._radius})"


c = Circle(5)
print(f"半径: {c.radius}")
print(f"面积: {c.area:.4f}")
print(f"周长: {c.perimeter:.4f}")
c.radius = 10
print(f"修改半径后面积: {c.area:.4f}")

try:
    c.radius = -1
except ValueError as e:
    print(f"setter 验证: {e}")

# ============================================================
# 5. __dunder__ 魔法方法
# ============================================================

print("\n=== 魔法方法 ===")

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> Vector:
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __len__(self) -> int:
        return 2   # 向量维度


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 * 3  = {v1 * 3}")
print(f"|v2|    = {abs(v2)}")
print(f"v1 == Vector(1,2): {v1 == Vector(1, 2)}")
print(f"len(v1) = {len(v1)}")

# ============================================================
# 6. @dataclass（Python 3.10+）
# ============================================================

print("\n=== @dataclass ===")

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0    # 带默认值的字段

    def distance_to_origin(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5


@dataclass
class Student:
    name: str
    scores: list[int] = field(default_factory=list)  # 可变默认值必须用 field

    def average(self) -> float:
        return sum(self.scores) / len(self.scores) if self.scores else 0.0


p1 = Point(3.0, 4.0)
p2 = Point(1.0, 1.0, 1.0)
print(f"p1 = {p1}")
print(f"p1 == Point(3,4): {p1 == Point(3.0, 4.0)}")
print(f"p1 到原点距离: {p1.distance_to_origin()}")

stu = Student("Alice", [88, 92, 79])
print(f"stu = {stu}")
print(f"stu.average() = {stu.average():.2f}")
