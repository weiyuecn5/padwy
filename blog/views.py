from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Hot,duizhao,shujuku
import time

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
        xslx=request.POST.get('xslx')
        jg = []
        context = {}
        if bh_1 and bh_2 and bh_3 and bh_4 and bh_5 and bh_6:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4).filter(宠物__icontains=bh_5)
            for shuju in shujus:
                if shuju.宠物.count(bh_1)>=int(cwysl) and shuju.宠物.count(bh_2)>=int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2 and bh_3 and bh_4 and bh_5:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4).filter(宠物__icontains=bh_5)
            for shuju in shujus:
                if shuju.宠物.count(bh_1)>=int(cwysl) and shuju.宠物.count(bh_2)>=int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2 and bh_3 and bh_4:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4)
            for shuju in shujus:
                if shuju.宠物.count(bh_1)>=int(cwysl) and shuju.宠物.count(bh_2)>=int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2 and bh_3:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3)
            for shuju in shujus:
                if shuju.宠物.count(bh_1)>=int(cwysl) and shuju.宠物.count(bh_2)>=int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/bhjg.html', context)
        elif bh_1:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1)
            for shuju in shujus:
                if shuju.宠物.count(bh_1)>=int(cwysl):
                    jg.append({"bh":shuju.账号编号,"st":shuju.石头数量})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/bhjg.html', context)
        else:
            return render(request, 'blog/index.html')
    else:
        post_list=Post.objects.all().order_by('-created_time')
        hot_list = Hot.objects.all().order_by('number')
        return render(request, 'blog/index.html', context={
            'post_list':post_list,
            'hot_list':hot_list
        })
def wy(request):
    if request.method == 'POST':
        bh_1 =request.POST.get('bh_1')
        bh_2=request.POST.get('bh_2')
        bh_3=request.POST.get('bh_3')
        bh_4=request.POST.get('bh_4')
        bh_5=request.POST.get('bh_5')
        bh_6=request.POST.get('bh_6')
        cwysl = request.POST.get('cwysl')
        cwesl = request.POST.get('cwesl')
        xslx=request.POST.get('xslx') #显示类型
        cxbh=request.POST.get('cxbh')#查询编号
        zxst=request.POST.get('zxst')#最小石头
        cwst = request.POST.get('cwst')#宠物石头 1.单查石头,2.石头+宠物1
        jg = []
        context = {}
        if bh_1 and bh_2 and bh_3 and bh_4 and bh_5 and bh_6:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4).filter(宠物__icontains=bh_5)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    backdata = {
                        'bh': shuju.账号编号,
                        'st': shuju.石头数量,
                        'dj': shuju.等级,
                        'gxsj': shuju.更新时间,
                        'cw': chuli(shuju.宠物)
                    }
                    jg.append(backdata)
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            if xslx == '1':
                return render(request, 'blog/bhjg.html', context)
            else:
                return render(request, 'blog/jg.html', context)
        elif bh_1 and bh_2 and bh_3 and bh_4 and bh_5:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4).filter(宠物__icontains=bh_5)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    backdata = {
                        'bh': shuju.账号编号,
                        'st': shuju.石头数量,
                        'dj': shuju.等级,
                        'gxsj': shuju.更新时间,
                        'cw': chuli(shuju.宠物)
                    }
                    jg.append(backdata)
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            if xslx == '1':
                return render(request, 'blog/bhjg.html', context)
            else:
                return render(request, 'blog/jg.html', context)
        elif bh_1 and bh_2 and bh_3 and bh_4:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    backdata = {
                        'bh': shuju.账号编号,
                        'st': shuju.石头数量,
                        'dj': shuju.等级,
                        'gxsj': shuju.更新时间,
                        'cw': chuli(shuju.宠物)
                    }
                    jg.append(backdata)
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            if xslx == '1':
                return render(request, 'blog/bhjg.html', context)
            else:
                return render(request, 'blog/jg.html', context)
        elif bh_1 and bh_2 and bh_3:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    backdata = {
                        'bh': shuju.账号编号,
                        'st': shuju.石头数量,
                        'dj': shuju.等级,
                        'gxsj': shuju.更新时间,
                        'cw': chuli(shuju.宠物)
                    }
                    jg.append(backdata)
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            if xslx == '1':
                return render(request, 'blog/bhjg.html', context)
            else:
                return render(request, 'blog/jg.html', context)
        elif bh_1 and bh_2:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2)
            for shuju in shujus:
                if shuju.宠物.count(bh_1)>=int(cwysl) and shuju.宠物.count(bh_2)>=int(cwesl):
                    backdata={
                        'bh':shuju.账号编号,
                        'st':shuju.石头数量,
                        'dj':shuju.等级,
                        'gxsj':shuju.更新时间,
                        'cw':chuli(shuju.宠物)
                    }
                    jg.append(backdata)
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            if xslx=='1':
                return render(request, 'blog/bhjg.html', context)
            else:
                return render(request, 'blog/jg.html', context)
        elif zxst and bh_1:
            shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(石头数量__gte=int(zxst))
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl):
                    backdata = {
                        'bh': shuju.账号编号,
                        'st': shuju.石头数量,
                        'dj': shuju.等级,
                        'gxsj': shuju.更新时间,
                        'cw': chuli(shuju.宠物)
                    }
                    jg.append(backdata)
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            if xslx == '1':
                return render(request, 'blog/bhjg.html', context)
            else:
                return render(request, 'blog/jg.html', context)
        elif bh_1:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl):
                    backdata = {
                        'bh': shuju.账号编号,
                        'st': shuju.石头数量,
                        'dj': shuju.等级,
                        'gxsj': shuju.更新时间,
                        'cw': chuli(shuju.宠物)
                    }
                    jg.append(backdata)
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            if xslx == '1':
                return render(request, 'blog/bhjg.html', context)
            else:
                return render(request, 'blog/jg.html', context)
        elif cxbh:
            try:
                shuju = shujuku.objects.get(账号编号=cxbh)
                shuju.宠物 = chuli(shuju.宠物)
                return render(request, 'blog/xq.html', {'shuju': shuju})
            except:
                shuju = {}
                shuju['账号编号'] = '账号不存在!'
                return render(request, 'blog/xq.html', {'shuju': shuju})
        elif zxst:
            if int(zxst)<=300:
                return HttpResponse('没意义不显示!')
            else:
                shujus = shujuku.objects.filter(已卖__exact='否').filter(石头数量__gte=int(zxst))#修改数据类型后方法
                for shuju in shujus:
                    backdata = {
                        'bh': shuju.账号编号,
                        'st': shuju.石头数量,
                        'dj': shuju.等级,
                        'gxsj': shuju.更新时间,
                        'cw': chuli(shuju.宠物)
                    }
                    jg.append(backdata)
                context['shujus'] = jg
                context['shuliang'] = len(jg)
                if xslx == '1':
                    return render(request, 'blog/bhjg.html', context)
                else:
                    return render(request, 'blog/jg.html', context)
        else:
            return render(request, 'blog/wy.html')
    else:
        post_list=Post.objects.all().order_by('-created_time')
        hot_list = Hot.objects.all().order_by('number')
        return render(request, 'blog/wy.html', context={
            'post_list':post_list,
            'hot_list':hot_list
        })

def xq(request,zhid):
    try:
        shuju = shujuku.objects.get(账号编号=zhid)
        shuju.宠物 = chuli(shuju.宠物)
        return render(request,'blog/xq.html',{'shuju':shuju})
    except:
        shuju={}
        shuju['账号编号']='账号不存在!'
        return render(request, 'blog/xq.html', {'shuju': shuju})
def ks(request,zhid):
    shuju = shujuku.objects.get(账号编号=zhid)
    return HttpResponse(shuju.宠物)
def add(request,zhid,st='0',dj='0',cw='0'): #/账号编号/石头数量/等级/宠物编号/
    gxsj = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 更新时间
    try:
        shuju = shujuku.objects.get(账号编号=zhid)
        shuju.宠物 = shuju.宠物 + cw+','
        shuju.石头数量 = int(st)
        shuju.等级 = dj
        shuju.更新时间 = gxsj
        shuju.已卖 = '否'
        shuju.save()
        return HttpResponse('更新:%s-%s-%s' % (zhid,st,cw))
    except:
        shuju=shujuku(账号编号=zhid,宠物=cw+',',石头数量 = st,等级 = dj,更新时间 = gxsj,已卖='否')
        shuju.save()
        return HttpResponse('加入:%s-%s-%s' % (zhid,st,cw))
def delshuju(request,zhid):
    try:
        shuju=shujuku.objects.get(pk=zhid)
        shuju.已卖='是'
        shuju.save()
        return HttpResponse('编号:%s 已经删除!'%zhid)
    except:
        return HttpResponse('编号:%s 不存在!'%zhid)
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
                cw_5 = cw_5 + '[' + data + '] '
    return cw_1+'\n'+cw_2+'\n'+cw_6+'\n'+cw_4+'\n'+cw_3+'\n'+cw_5