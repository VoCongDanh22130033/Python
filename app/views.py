from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404


#home
#video9(đừng xóa dòng comment này)
def home_view(request):
    products = Product.objects.all()
    for product in products:
        product.primary_image = ProductImage.objects.filter(id_product=product, is_primary=True).first()
    
    context = {'products': products}
    return render(request, 'app/index.html', context)

#view login
def login_view(request):
    return render(request, 'app/login-register.html')

#verify
def verify_view(request):
    return render(request, 'app/verify.html')

#checkout
def checkout_view(request):
    return render(request, 'app/checkout.html')

#404html
def error_view(request):
    return render(request, 'app/404.html')

#about us page
def about_us_view(request):
    return render(request, 'app/about-us.html')

#compare page
def compare_view(request):
    return render(request, 'app/compare.html')

#contact page
def contact_view(request):
    return render(request, 'app/contact.html')

#faq page
def faq_view(request):
    return render(request, 'app/faq.html')

#payment page
def payment_view(request):
    return render(request, 'app/payment.html')

#shop left sidebar page
def shop_left_sidebar_view(request):
    return render(request, 'app/shop-left-sidebar.html')

#shopping cart page
def cart_view(request):
    return render(request, 'app/shopping-cart.html')

#single-product page
def single_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Lấy ảnh chính (primary image)
    primary_image = ProductImage.objects.filter(id_product=product, is_primary=True).first()
    
    # Lấy các ảnh con (secondary images)
    secondary_images = ProductImage.objects.filter(id_product=product, is_primary=False)

    print("Primary Image:", primary_image)
    print("Secondary Images:", secondary_images)  # Kiểm tra lại xem dữ liệu có đúng không

    context = {
        'product': product,
        'primary_image': primary_image,
        'secondary_images': secondary_images
    }
    return render(request, 'app/single-product.html', context)

#wishlist page
def wishlist_view(request):
    return render(request, 'app/wishlist.html')