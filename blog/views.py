from django.shortcuts import render
from .models import Post,Hot

def index(request):
    post_list=Post.objects.all().order_by('-created_time')
    hot_list = Hot.objects.all().order_by('number')
    return render(request, 'blog/base.html', context={
        'post_list':post_list,
        'hot_list':hot_list
    })
