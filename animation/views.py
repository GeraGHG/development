from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Topic

# Create your views here.
class TopicList(View):
    def get(self, request, *args, **kwargs):
        topics = Topic.objects.all()
        context = {
            'topics': topics
        }
        return render(request, 'animationthemes.html', context)

class TopicDetails(View):
    def get(self, request, topic_id, *args, **kwargs):
        topic = get_object_or_404(Topic, pk=topic_id)
        context = {
            'topic': topic
        }
        return render(request, 'animationdetails.html', context)

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
