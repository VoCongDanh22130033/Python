from django.db import models
from django.contrib.auth.models import AbstractUser


class Address(models.Model):
    address = models.CharField(max_length=100)
    ward = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    is_default = models.BooleanField()
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    class Meta:
        db_table = "address"

# class PasswordReset(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     token_reset = models.CharField(max_length=10)
#     expire_at = models.CharField(max_length=100)

#     class Meta:
#         db_table = "password_resets"

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',  # Tham chiếu đến chính model Category
        on_delete=models.SET_NULL,  # Khi parent bị xóa, set giá trị NULL
        null=True,  # Cho phép giá trị NULL
        blank=True,  # Cho phép để trống trong form
        related_name='children'  # Tạo quan hệ ngược để lấy các mục con
    )

    class Meta:
        db_table = "categories"
    def __str__(self):
        return self.name

class Product(models.Model):
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    create_at = models.DateField()
    update_at = models.DateField(null=True, blank=True)
    is_new = models.BooleanField()
    brand = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = "products"

class Size(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "sizes"

class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=10)

    class Meta:
        db_table = "colors"

class ProductVariant(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_color = models.ForeignKey(Color, on_delete=models.CASCADE)
    id_size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    create_at = models.DateField()
    status = models.IntegerField(choices=[(0, 'out of stockstock'), (1, 'in stock')], default=1)

    class Meta:
        db_table = "product_variants"

class Inventory(models.Model):
    id_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField()
    update_at = models.DateField()

    class Meta:
        db_table = "inventory"

class ProductImage(models.Model):
    id_product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)  # Cho phép null
    image_url = models.CharField(max_length=255)
    is_primary = models.BooleanField()
    create_at = models.DateField()

    class Meta:
        db_table = "product_images"

class Coupon(models.Model):
    code = models.CharField(max_length=10)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    discount_type = models.CharField(max_length=30)
    valid_from = models.DateField()
    valid_to = models.DateField()
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "coupons"

class Order(models.Model):
    id_user = models.IntegerField()
    id_coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    create_at = models.DateField()

    class Meta:
        db_table = "orders"

class ShippingInfo(models.Model):
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "shipping_infor"

class OrderDetail(models.Model):
    id_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    id_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity_product = models.IntegerField()
    price_at = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "order_detail"

class Cart(models.Model):
    id_user = models.IntegerField()
    create_at = models.CharField(max_length=100)

    class Meta:
        db_table = "cart"

class CartDetail(models.Model):
    id_cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    id_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    price_at = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_product = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "cart_detail"

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
