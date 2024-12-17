from django.contrib import admin
from django.urls import path
#load images
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Import views từ ứng dụng hiện tại



urlpatterns = [
   
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('verify/', views.verify_view, name='verify'),
    path('error/', views.error_view, name='error'),
    path('about-us/', views.about_us_view, name='about-us'),
    path('checkout/', views.checkout_view, name='checkout'), 
    path('compare/', views.compare_view, name='compare'),
    path('contact/', views.contact_view, name='contact'),
    path('faq/', views.faq_view, name='faq'), 
    path('payment/', views.payment_view, name='payment'), 
    path('shop-left-sidebar/', views.shop_left_sidebar_view, name='shop-left-sidebar'), 
    path('cart/', views.cart_view, name='cart'),
    path('detail/', views.single_product_view, name='detail'),
    path('wishlist/', views.wishlist_view, name='wishlist'),

    # Chuyen sang trang detail voi san pham
    path('product/<int:product_id>/', views.single_product_view, name='product_detail'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
