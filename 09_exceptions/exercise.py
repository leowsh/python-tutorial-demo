"""
第 09 章：练习题
请先独立完成，再查看下方答案注释。
"""

# ============================================================
# 练习 1：健壮的类型转换函数
# 要求：编写 safe_convert(value, target_type, default=None)
#   - 尝试将 value 转换为 target_type（int/float/str/bool）
#   - 成功返回转换后的值，失败返回 default
#   - 对列表 [("42", int), ("3.14", float), ("hello", int), (None, str)]
#     调用并输出结果
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# def safe_convert(value, target_type, default=None):
#     try:
#         return target_type(value)
#     except (ValueError, TypeError):
#         return default
#
# tests = [("42", int), ("3.14", float), ("hello", int), (None, str), ("true", bool)]
# for v, t in tests:
#     result = safe_convert(v, t)
#     print(f"  safe_convert({v!r}, {t.__name__}) = {result!r}")

# ============================================================
# 练习 2：自定义异常体系
# 要求：为一个"在线商城"设计异常体系：
#   - ShopError（基类）
#     - OutOfStockError(product_name, requested, available)
#     - InvalidCouponError(code, reason)
#     - PaymentError(amount, reason)
#
# 编写函数 place_order(product, qty, coupon=None)：
#   - 库存不足时抛出 OutOfStockError
#   - 优惠码无效时抛出 InvalidCouponError
#   - 用例：
#     place_order("苹果手机", 100)  -> 库存不足
#     place_order("耳机", 1, "INVALID")  -> 无效优惠码
#     place_order("充电器", 1)  -> 下单成功
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# class ShopError(Exception):
#     pass
#
# class OutOfStockError(ShopError):
#     def __init__(self, product_name: str, requested: int, available: int) -> None:
#         self.product_name = product_name
#         self.requested = requested
#         self.available = available
#         super().__init__(
#             f"《{product_name}》库存不足：需要 {requested}，库存 {available}"
#         )
#
# class InvalidCouponError(ShopError):
#     def __init__(self, code: str, reason: str) -> None:
#         self.code = code
#         self.reason = reason
#         super().__init__(f"优惠码 {code!r} 无效：{reason}")
#
# class PaymentError(ShopError):
#     def __init__(self, amount: float, reason: str) -> None:
#         self.amount = amount
#         self.reason = reason
#         super().__init__(f"支付 {amount:.2f} 元失败：{reason}")
#
# STOCK = {"苹果手机": 5, "耳机": 10, "充电器": 50}
# VALID_COUPONS = {"SAVE10", "HALF"}
#
# def place_order(product: str, qty: int, coupon: str | None = None) -> None:
#     available = STOCK.get(product, 0)
#     if qty > available:
#         raise OutOfStockError(product, qty, available)
#     if coupon is not None and coupon not in VALID_COUPONS:
#         raise InvalidCouponError(coupon, "不存在或已过期")
#     print(f"  下单成功：{product} x{qty}"
#           + (f"，使用优惠码 {coupon}" if coupon else ""))
#
# orders = [
#     ("苹果手机", 100, None),
#     ("耳机", 1, "INVALID"),
#     ("充电器", 1, "SAVE10"),
# ]
# for args in orders:
#     try:
#         place_order(*args)
#     except OutOfStockError as e:
#         print(f"  OutOfStockError: {e}")
#     except InvalidCouponError as e:
#         print(f"  InvalidCouponError: {e}")

# ============================================================
# 练习 3：带重试机制的网络请求模拟
# 要求：
#   - 定义 NetworkError 和 TimeoutError（继承 NetworkError）
#   - 编写 fetch_data(url, max_retries=3) 函数：
#     - 用随机数模拟：30% 概率 TimeoutError，20% 概率 NetworkError，50% 成功
#     - 失败时重试，超过 max_retries 则抛出最后一次异常
#     - 每次重试打印 "第N次重试..."
#     - 成功打印 "获取成功: <url>"
# ============================================================

# 在此处编写你的代码：


# --- 答案 ---
# import random
# random.seed(1)
#
# class NetworkError(Exception):
#     pass
#
# class TimeoutError(NetworkError):
#     pass
#
# def fetch_data(url: str, max_retries: int = 3) -> str:
#     last_exc = None
#     for attempt in range(max_retries + 1):
#         try:
#             r = random.random()
#             if r < 0.3:
#                 raise TimeoutError(f"连接超时: {url}")
#             elif r < 0.5:
#                 raise NetworkError(f"网络错误: {url}")
#             return f"数据内容 from {url}"
#         except (TimeoutError, NetworkError) as e:
#             last_exc = e
#             if attempt < max_retries:
#                 print(f"  [{type(e).__name__}] 第{attempt+1}次重试...")
#             else:
#                 raise
#
# for url in ["https://example.com/api/1", "https://example.com/api/2"]:
#     try:
#         result = fetch_data(url, max_retries=3)
#         print(f"  获取成功: {url} -> {result}")
#     except NetworkError as e:
#         print(f"  最终失败: {e}")
