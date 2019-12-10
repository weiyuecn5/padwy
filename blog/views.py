from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Post,Hot,duizhao,shujuku


def index(request):
    if request.method == 'POST':
        bh_1 =request.POST.get('bh_1')
        bh_2=request.POST.get('bh_2')
        bh_3=request.POST.get('bh_3')
        bh_4=request.POST.get('bh_4')
        bh_5=request.POST.get('bh_5')
        bh_6=request.POST.get('bh_6')
        cwysl = request.POST.get('cwysl')
        cwesl = request.POST.get('cwesl')
        jg = []
        context = {}
        if bh_1 and bh_2 and bh_3 and bh_4 and bh_5 and bh_6:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4).filter(宠物__icontains=bh_5)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    shuju.宠物 = chuli(shuju.宠物)
                    jg.append(shuju)
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/jg.html', context)
        elif bh_1 and bh_2 and bh_3 and bh_4 and bh_5:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4).filter(宠物__icontains=bh_5)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    shuju.宠物 = chuli(shuju.宠物)
                    jg.append(shuju)
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/jg.html', context)
        elif bh_1 and bh_2 and bh_3 and bh_4:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    shuju.宠物 = chuli(shuju.宠物)
                    jg.append(shuju)
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/jg.html', context)
        elif bh_1 and bh_2 and bh_3:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    shuju.宠物 = chuli(shuju.宠物)
                    jg.append(shuju)
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/jg.html', context)
        elif bh_1 and bh_2:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    shuju.宠物 = chuli(shuju.宠物)
                    jg.append(shuju)
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/jg.html', context)
        elif bh_1:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1)
            for shuju in shujus:
                if shuju.宠物.count(bh_1)>=int(cwysl):
                    shuju.宠物=chuli(shuju.宠物)
                    jg.append(shuju)
            # paginator = Paginator(jg, 10)
            # page_num = request.GET.get('page', 1)
            # page_of_jg = paginator.page(page_num)
            # context['page_of_jg'] = page_of_jg
            # context['shuliang'] = len(jg)
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/jg.html', context)
        else:
            return render(request, 'blog/index.html')
    else:
        post_list=Post.objects.all().order_by('-created_time')
        hot_list = Hot.objects.all().order_by('number')
        return render(request, 'blog/index.html', context={
            'post_list':post_list,
            'hot_list':hot_list
        })
def cxjg(request):
    bh_1 = request.POST.get('bh_1')
    bh_2 = request.POST.get('bh_2')
    bh_3 = request.POST.get('bh_3')
    bh_4 = request.POST.get('bh_4')
    bh_5 = request.POST.get('bh_5')
    bh_6 = request.POST.get('bh_6')
    cwysl = request.POST.get('cwysl')
    cwesl = request.POST.get('cwesl')
    jg = []
    context = {}
    if bh_1 and bh_2 and bh_3 and bh_4 and bh_5 and bh_6:
        shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(
            宠物__icontains=bh_3).filter(宠物__icontains=bh_4).filter(宠物__icontains=bh_5)
        for shuju in shujus:
            shuju.宠物 = chuli(shuju.宠物)
        return render(request, 'blog/jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
    elif bh_1 and bh_2 and bh_3 and bh_4 and bh_5:
        shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(
            宠物__icontains=bh_3).filter(宠物__icontains=bh_4).filter(宠物__icontains=bh_5)
        for shuju in shujus:
            shuju.宠物 = chuli(shuju.宠物)
        return render(request, 'blog/jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
    elif bh_1 and bh_2 and bh_3 and bh_4:
        shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(
            宠物__icontains=bh_3).filter(宠物__icontains=bh_4)
        for shuju in shujus:
            shuju.宠物 = chuli(shuju.宠物)
        return render(request, 'blog/jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
    elif bh_1 and bh_2 and bh_3:
        shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(
            宠物__icontains=bh_3)
        for shuju in shujus:
            shuju.宠物 = chuli(shuju.宠物)
        return render(request, 'blog/jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
    elif bh_1 and bh_2:
        shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2)
        for shuju in shujus:
            shuju.宠物 = chuli(shuju.宠物)
        return render(request, 'blog/jg.html', {'shuju': shujus, 'shuliang': len(shujus)})
    elif bh_1:
        shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1)
        for shuju in shujus:
            if shuju.宠物.count(bh_1) >= int(cwysl):
                shuju.宠物 = chuli(shuju.宠物)
                jg.append(shuju)
        paginator = Paginator(jg, 10)
        page_num = request.GET.get('page', 1)
        page_of_jg = paginator.page(page_num)
        context['page_of_jg'] = page_of_jg
        context['shuliang'] = len(jg)
        # context['shujus'] = jg
        # context['shuliang'] = len(jg)
        return render(request, 'blog/jg.html', context)

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