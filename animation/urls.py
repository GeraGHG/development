from django.urls import path
from . import views

app_name = 'animation'
urlpatterns = [
    path('', views.TopicList.as_view(), name='animationthemes'),
    path('<int:topic_id>/', views.TopicDetails.as_view(), name='topicdetails'),
    path('Los-mejores-programas-de-animación-2D-GRATIS-2024/', views.SoftwareAnimationFree.as_view(), name='softwareanimationfree'),
    path('Los-mejores-programas-de-animación-2D-PAGO-2024/', views.SoftwareAnimationPay.as_view(), name='softwareanimationpay')
]
