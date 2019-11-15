from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post,Hot

def index(request):
    post_list=Post.objects.all().order_by('-created_time')
    hot_list = Hot.objects.all().order_by('number')
    return render(request, 'blog/index.html', context={
        'post_list':post_list,
        'hot_list':hot_list
    })
def index1(request):
    post_list=Post.objects.all().order_by('-created_time')
    paginator = Paginator(post_list,2) #每页显示2篇
    page= request.GET.get('page',1)
    posttomer=paginator.page(page)
    return render(request,'blog/index1.html',context={
        'post_list':posttomer,
    })
