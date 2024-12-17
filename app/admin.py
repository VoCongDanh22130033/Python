from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Đảm bảo rằng bạn đã nhập UserAdmin
from django.contrib.auth.models import User
from .models import CustomUser
from .models import (
    Address,
    # PasswordReset,
    Category,
    Product,
    Size,
    Color,
    ProductVariant,
    Inventory,
    ProductImage,
    Coupon,
    Order,
    ShippingInfo,
    OrderDetail,
    Cart,
    CartDetail,
)

# Register all models with default configurations
admin.site.register(Address)





admin.site.register(Inventory)

admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(ShippingInfo)
admin.site.register(OrderDetail)
admin.site.register(Cart)
admin.site.register(CartDetail)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'last_login', 'phone_number')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    list_filter = ('is_staff', 'is_active', 'groups', 'user_permissions')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),  # Thêm phone_number
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# Đảm bảo chỉ đăng ký model CustomUser một lần
admin.site.register(CustomUser, CustomUserAdmin)  # Đăng ký lại với CustomUser

#Color
class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex_code')  # Các cột bạn muốn hiển thị
    search_fields = ('name', 'hex_code')  # Thêm ô tìm kiếm
admin.site.register(Color, ColorAdmin)

#Size
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
admin.site.register(Size, SizeAdmin)

#Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','parent')
    search_fields = ('name','parent')
admin.site.register(Category, CategoryAdmin)

# Tạo Custom Filter cho danh mục cha
class ParentCategoryFilter(admin.SimpleListFilter):
    title = 'Parent Category'  # Tên hiển thị trong Admin
    parameter_name = 'parent_category'

    def lookups(self, request, model_admin):
        # Lấy tất cả các danh mục cha (không có parent)
        parent_categories = Category.objects.filter(parent__isnull=True)
        return [(category.id, category.name) for category in parent_categories]

    def queryset(self, request, queryset):
        # Lọc các sản phẩm thuộc danh mục con của danh mục cha
        if self.value():
            return queryset.filter(id_category__parent_id=self.value())
        return queryset

class ProductAdmin(admin.ModelAdmin):
    # Hiển thị tất cả các trường
    list_display = ('id', 'id_category', 'title', 'price', 'discount', 
                    'create_at', 'update_at', 'is_new', 'brand', 'description')
    
    
    
    # Tìm kiếm theo title và brand
    search_fields = ('title', 'brand')

    # Thêm custom filter và filter mặc định
    list_filter = ('brand','id_category')

    # Sắp xếp mặc định
    ordering = ('-create_at',)

   

admin.site.register(Product, ProductAdmin)

#Product Variants
class ProductVariantAdmin(admin.ModelAdmin):
    def get_product_id(self, obj):
        return obj.id_product.id
    get_product_id.short_description = 'ID PRODUCT'

    def get_color_id(self, obj):
        return obj.id_color.id
    get_color_id.short_description = 'ID COLOR'

    def get_size_id(self, obj):
        return obj.id_size.id
    get_size_id.short_description = 'ID SIZE'

    # Hiển thị tất cả các trường, bao gồm 'id'
    list_display = ('id', 'get_product_id', 'get_color_id', 'get_size_id', 'quantity', 
                    'create_at', 'status')

    # Cho phép tìm kiếm theo các trường cụ thể
    search_fields = ('id_product__title', 'id_color__name', 'id_size__name')

    # Thêm filter cho các trường liên kết và status
    list_filter = ('id_product', 'id_color', 'id_size', 'status')

    # Sắp xếp mặc định theo ngày tạo
    ordering = ('-create_at',)
admin.site.register(ProductVariant, ProductVariantAdmin)
#Product Images
class ProductImageAdmin(admin.ModelAdmin):
    # Hàm trả về ID của id_product
    def get_product_id(self, obj):
        return obj.id_product.id if obj.id_product else 'No Product'
    get_product_id.short_description = 'ID PRODUCT'  # Đặt tên cột hiển thị

    # Hiển thị tất cả các cột của model ProductImage
    list_display = ('id', 'get_product_id', 'image_url', 'is_primary', 'create_at')

    # Tìm kiếm theo URL hình ảnh và trạng thái is_primary
    search_fields = ('image_url',)

    # Thêm filter để lọc theo id_product và is_primary
    list_filter = ('id_product', 'is_primary')

    # Sắp xếp mặc định theo ngày tạo
    ordering = ('-create_at',)

admin.site.register(ProductImage, ProductImageAdmin)
