from django.urls import path
from .views import SoftwareAnimation

app_name = 'animation'
urlpatterns = [
    path('', SoftwareAnimation.as_view(), name='softwareanimation'),
]