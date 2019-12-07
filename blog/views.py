from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post,Hot,duizhao,shujuku


def index(request):
    if request.method == 'POST':
        bh_1 =request.POST.get('bh_1')
        bh_2 = request.POST.get('option1')
        return HttpResponse(bh_2)
    post_list=Post.objects.all().order_by('-created_time')
    hot_list = Hot.objects.all().order_by('number')
    return render(request, 'blog/index.html', context={
        'post_list':post_list,
        'hot_list':hot_list
    })
def index2(request):
    if request.method=='GET':
        post_list=Post.objects.all().order_by('-created_time')
        hot_list = Hot.objects.all().order_by('number')
        # print('111')
        return render(request, 'blog/index.html', context={
            'post_list':post_list,
            'hot_list':hot_list
        })
    else:
        bh_1=request.POST.get('bh_1')
        # bh_2=request.POST.get('bh_2')
        # bh_3=request.POST.get('bh_3')
        # bh_4=request.POST.get('bh_4')
        # bh_5=request.POST.get('bh_5')
        if request.POST.get('sl_1'):
            sl_1=request.POST.get('sl_1')
        else:
            sl_1=1
        if request.POST.get('sl_2'):
            sl_2=request.POST.get('sl_2')
        else:
            sl_2=1
        print(type(bh_1))
        print(sl_1)
        print('...')
        back_data=[]
        if bh_1:
            shujus = shujuku.objects.filter(已卖__exact='0').filter(宠物__icontains=bh_1)
            for shuju in shujus:
                if shujuku.宠物.count(bh_1)>=sl_1:
                    shuju.宠物 = chuli(shuju.宠物)
                    back_data.append(shuju)

        return render(request, 'blog/jg.html', {'shuju': back_data, 'shuliang': len(back_data)})



def index1(request):
    post_list=Post.objects.all().order_by('-created_time')
    paginator = Paginator(post_list,2) #每页显示2篇
    page= request.GET.get('page',1)
    posttomer=paginator.page(page)
    return render(request,'blog/index1.html',context={
        'post_list':posttomer,
    })

def chuli(cw):
    cw_1 = '\n75000宠物:\n'
    cw_2 = '50000宠物:\n'
    cw_3 = '6000宠物:\n'
    cw_4 = '15000宠物:\n'
    cw_6 = '25000宠物:\n'
    cw_5 = '其他宠物:\n'
    for data in cw.split(','):
        if len(data) > 4 or len(data) < 3:
            continue
        else:
            try:
                a = duizhao.objects.get(pk=data)
                if int(a.宠物价值)==75000:
                    cw_1=cw_1+'[' + a.宠物编号 + a.宠物名字 + '] '
                elif int(a.宠物价值)==50000:
                    cw_2 = cw_2 + '[' + a.宠物编号 + a.宠物名字 + '] '
                elif int(a.宠物价值) == 25000:
                    cw_6 = cw_6 + '[' + a.宠物编号 + a.宠物名字 + '] '
                elif int(a.宠物价值) == 15000:
                    cw_4 = cw_4 + '[' + a.宠物编号 + a.宠物名字 + '] '
                elif int(a.宠物价值)==6000:
                    cw_3 = cw_3 + '[' + a.宠物编号 + a.宠物名字 + '] '
                else:
                    cw_5 = cw_5+ '[' + a.宠物编号 + a.宠物名字 + '] '
            except:
                pass
    return cw_1+'\n'+cw_2+'\n'+cw_6+'\n'+cw_4+'\n'+cw_3+'\n'+cw_5