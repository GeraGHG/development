from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class AnimationThemes(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'animationthemes.html', context)

class SoftwareAnimationFree(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'softwareanimationfree.html', context)
    
class SoftwareAnimationPay(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'softwareanimationpay.html', context)


