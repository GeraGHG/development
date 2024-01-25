from django.urls import path
from .views import SoftwareAnimationFree, SoftwareAnimationPay, AnimationThemes

app_name = 'animation'
urlpatterns = [
    path('', AnimationThemes.as_view(), name='animationthemes'),
    path('Los-mejores-programas-de-animación-2D-GRATIS-2024/', SoftwareAnimationFree.as_view(), name='softwareanimationfree'),
    path('Los-mejores-programas-de-animación-2D-PAGO-2024/', SoftwareAnimationPay.as_view(), name='softwareanimationpay')
]