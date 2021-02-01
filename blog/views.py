from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Hot,duizhao,shujuku,danzhu,jiankong
import time
import requests
from bs4 import BeautifulSoup
from time import sleep

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
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4).filter(宠物__icontains=bh_5).filter(宠物__icontains=bh_6).exclude(账号编号__icontains='X').exclude(账号编号__icontains='Y')
            for shuju in shujus:
                if shuju.宠物.count(bh_1)>=int(cwysl) and shuju.宠物.count(bh_2)>=int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl + '|' + bh_2 + 'x' + cwesl + '|'+ bh_3 + '|' + bh_4 + '|' + bh_5 + '|' + bh_6
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2 and bh_3 and bh_4 and bh_5:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4).filter(宠物__icontains=bh_5).exclude(账号编号__icontains='X').exclude(账号编号__icontains='Y')
            for shuju in shujus:
                if shuju.宠物.count(bh_1)>=int(cwysl) and shuju.宠物.count(bh_2)>=int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl + '|' + bh_2 + 'x' + cwesl + '|'+ bh_3 + '|' + bh_4 + '|' + bh_5
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2 and bh_3 and bh_4:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4).exclude(账号编号__icontains='X').exclude(账号编号__icontains='Y')
            for shuju in shujus:
                if shuju.宠物.count(bh_1)>=int(cwysl) and shuju.宠物.count(bh_2)>=int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl + '|' + bh_2 + 'x' + cwesl + '|'+ bh_3 + '|' + bh_4
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2 and bh_3:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).exclude(账号编号__icontains='X').exclude(账号编号__icontains='Y')
            for shuju in shujus:
                if shuju.宠物.count(bh_1)>=int(cwysl) and shuju.宠物.count(bh_2)>=int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl + '|' + bh_2 + 'x' + cwesl + '|'+ bh_3
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).exclude(账号编号__icontains='X').exclude(账号编号__icontains='Y')
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2)>=int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl + '|' + bh_2 + 'x' + cwesl
            return render(request, 'blog/bhjg.html', context)
        elif bh_1:
            shujus=shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).exclude(账号编号__icontains='X').exclude(账号编号__icontains='Y')
            for shuju in shujus:
                if shuju.宠物.count(bh_1)>=int(cwysl):
                    jg.append({"bh":shuju.账号编号,"st":shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl
            return render(request, 'blog/bhjg.html', context)
        else:
            return render(request, 'blog/index.html')
    else:
        post_list=Post.objects.all().order_by('-created_time')
        a=[]
        b=[]
        paihangs = Hot.objects.get(name=1)
        dangqians = Hot.objects.get(name=2)
        for paihang in paihangs.number.split(','):
            a.append(paihang)
        for dangqian in dangqians.number.split(','):
            b.append(dangqian)
        return render(request, 'blog/index.html', context={
            'post_list':post_list,
            'paihang':a,    #队长排行
            'dangqian': b,   #当前合作
        })
def ww(request):
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
        cxbh=request.POST.get('cxbh')#查询编号,最大石头
        zxst=request.POST.get('zxst')#最小石头
        jg = []
        context = {}
        if cxbh and bh_1:
            try:
                shuju = shujuku.objects.get(账号编号=cxbh)
                str=shuju.宠物
                shuju.宠物=str.replace(bh_1+',', ',',1)
                shuju.save()
                return HttpResponse('账号:%s-%s_删除成功!' % (cxbh, bh_1))
            except:
                return HttpResponse('账号:%s-%s_删除失败!' % (cxbh, bh_1))
        elif zxst and cxbh:#加入最大石头限制 cxbh代替最大石头
            shujus = shujuku.objects.filter(已卖__exact='否').filter(石头数量__gte=int(zxst)).filter(石头数量__lte=int(cxbh))
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/bhjg.html', context)

        elif cxbh and xslx == '1':
            try:
                shuju = shujuku.objects.get(账号编号=cxbh)
                back = chuli_1(shuju.宠物)
                return render(request, 'blog/tpxq.html', {'shuju': shuju,'back':back})
            except:
                shuju = {}
                shuju['账号编号'] = '账号不存在!'
                return render(request, 'blog/tpxq.html', {'shuju': shuju})
        elif cxbh and xslx=='2':
            shujus = shujuku.objects.filter(已卖__exact='否').filter(账号编号__icontains=cxbh)
            for shuju in shujus:
                jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2 and bh_3 and bh_4 and bh_5 and bh_6:
            shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4).filter(宠物__icontains=bh_5).filter(宠物__icontains=bh_6)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl + '|' + bh_2 + 'x' + cwesl + '|' + bh_3 + '|' + bh_4 + '|' + bh_5 + '|' + bh_6
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2 and bh_3 and bh_4 and bh_5:
            shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4).filter(宠物__icontains=bh_5)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl + '|' + bh_2 + 'x' + cwesl + '|' + bh_3 + '|' + bh_4 + '|' + bh_5
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2 and bh_3 and bh_4:
            shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3).filter(宠物__icontains=bh_4)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl + '|' + bh_2 + 'x' + cwesl + '|' + bh_3 + '|' + bh_4
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2 and bh_3:
            shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(宠物__icontains=bh_3)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl + '|' + bh_2 + 'x' + cwesl + '|' + bh_3
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2 and  zxst: #编号1+编号2+最小石头
            shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(石头数量__gte=int(zxst))
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl + '|' + bh_2 + 'x' + cwesl+ '|最小石头:' + zxst
            print('000')
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2 and  bh_6: #编号1+编号2+组别
            shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2).filter(账号编号__icontains=bh_6)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl + '|' + bh_2 + 'x' + cwesl+ '|' + bh_6 + '组'
            return render(request, 'blog/bhjg.html', context)
        elif bh_1 and bh_2: #编号1+编号2
            shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(宠物__icontains=bh_2)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl) and shuju.宠物.count(bh_2) >= int(cwesl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl + '|' + bh_2 + 'x' + cwesl
            return render(request, 'blog/bhjg.html', context)

        elif bh_1 and  bh_6: #编号1+组别
            shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(账号编号__icontains=bh_6)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl + '|组别:' + bh_6
            return render(request, 'blog/bhjg.html', context)

        elif bh_1 and  zxst: #编号+最小石头
            shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1).filter(石头数量__gte=int(zxst))
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl + '|最小石头:' + zxst
            return render(request, 'blog/bhjg.html', context)
        elif zxst: #最小石头
            shujus = shujuku.objects.filter(已卖__exact='否').filter(石头数量__gte=int(zxst))
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            return render(request, 'blog/bhjg.html', context)
        elif bh_1: #编号1
            shujus = shujuku.objects.filter(已卖__exact='否').filter(宠物__icontains=bh_1)
            for shuju in shujus:
                if shuju.宠物.count(bh_1) >= int(cwysl):
                    jg.append({"bh": shuju.账号编号, "st": shuju.石头数量,"sx":shuju.买家})
            context['shujus'] = jg
            context['shuliang'] = len(jg)
            context['ss'] = bh_1 + 'x' + cwysl
            return render(request, 'blog/bhjg.html', context)

        else:
            return render(request, 'blog/index.html')

    else:
        a=[]
        b=[]
        paihangs = Hot.objects.get(name=1)
        dangqians = Hot.objects.get(name=2)
        for paihang in paihangs.number.split(','):
            a.append(paihang)
        for dangqian in dangqians.number.split(','):
            b.append(dangqian)
        return render(request, 'blog/wy.html', context={
            'paihang':a,    #队长排行
            'dangqian': b,   #当前合作
        })
def xq(request,zhid):
    try:
        shuju = shujuku.objects.get(账号编号=zhid)
        back = chuli_1(shuju.宠物)
        return render(request, 'blog/tpxq.html', {'shuju': shuju, 'back': back})
        # shuju.宠物 = chuli(shuju.宠物)
        # return render(request,'blog/xq.html',{'shuju':shuju})
    except:
        shuju={}
        shuju['账号编号']='账号不存在!'
        return render(request, 'blog/xq.html', {'shuju': shuju})
def ks(request,zhid):
    shuju = shujuku.objects.get(账号编号=zhid)
    return HttpResponse(shuju.宠物)
def sc(request,zhid,scid):#删除宠物 账号ID 删除id
    try:
        shuju = shujuku.objects.get(账号编号=zhid)
        str = shuju.宠物
        shuju.宠物 = str.replace(scid + ',', ',', 1)
        shuju.save()
        return HttpResponse('账号:%s-%s_删除成功!' % (zhid, scid))
    except:
        return HttpResponse('账号:%s-%s_删除失败!' % (zhid, scid))
def ptj(request,bh1,bh2):
    for i in range(int(bh1), int(bh2)+1):
        if duizhao.objects.filter(宠物编号=str(i)).exists():
            print("该数据已经存在")
        else:
            get_txt(str(i))
            sleep(2)
    return HttpResponse('加入:')
def get_txt(number):
    full_url = 'http://pad.skyozora.com/pets/'+number
    # print(full_url)
    try:
        r = requests.get(full_url)
        soup = BeautifulSoup(r.text,features="html.parser")
        b= soup.title.text.split('-')
        bb=soup.find('span',class_='yellow bold')
        # print(bb)
        shuju=duizhao(宠物编号=b[0].strip(),宠物名字=b[1].strip(),宠物价值=bb.text)
        shuju.save()
    except:
        pass


def zhqd(request):
    data=''
    shujus = shujuku.objects.filter(已卖__exact='否')
    for shuju in shujus:
        data=data+shuju.账号编号+'\n'
    return HttpResponse(data)
def jl(request):
    return render(request, 'blog/jl.html')
def addid(request,zhid,yxid):
    try:
        shuju = shujuku.objects.get(账号编号=zhid)
        shuju.账号ID = yxid
        shuju.save()
        return HttpResponse('更新:%s-%s' % (zhid, yxid))
    except:
        pass
def addsx(request,zhid,sx):
    try:
        shuju = shujuku.objects.get(账号编号=zhid)
        shuju.买家 = sx
        shuju.save()
        return HttpResponse('更新:%s-%s' % (zhid, sx))
    except:
        pass
def addjk(request,zhid,sx):
    try:
        shuju = jiankong.objects.get(手机编号=zhid)
        内容=shuju.内容
        if len(内容)>200:
            内容=''
        shuju.内容 = sx+'\n'+内容
        shuju.save()
        return HttpResponse('更新:%s-%s' % (zhid, sx))
    except:
        pass

def jk(request):
    shuju=jiankong.objects.all()
    return render(request, 'blog/jk.html',{'shuju':shuju})
def add(request,zhid,st='0',dj='0',cw='0'): #/账号编号/石头数量/等级/宠物编号/
    gxsj = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 更新时间
    try:
        shuju = shujuku.objects.get(账号编号=zhid)
        shuju.宠物 = shuju.宠物 + cw+','
        shuju.石头数量 = int(st[-4:])
        shuju.等级 = dj
        shuju.更新时间 = gxsj
        shuju.已卖 = '否'
        shuju.save()
        return HttpResponse('更新:%s-%s-%s' % (zhid,st,cw))
    except:
        shuju=shujuku(账号编号=zhid,宠物=cw+',',石头数量 = st[-4:],等级 = dj,更新时间 = gxsj,已卖='否')
        shuju.save()
        return HttpResponse('加入:%s-%s-%s' % (zhid,st,cw))
def dzadd(request,zhid,st='0',cw='0'): #/账号编号/石头数量/等级/宠物编号/
    gxsj = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 更新时间
    try:
        shuju = danzhu.objects.get(账号编号=zhid)
        shuju.宠物 = shuju.宠物 + cw+','
        shuju.石头数量 = int(st[-4:])
        shuju.等级 = '2'
        shuju.更新时间 = gxsj
        shuju.已卖 = '否'
        shuju.save()
        return HttpResponse('更新:%s-%s-%s' % (zhid,st,cw))
    except:
        shuju=danzhu(账号编号=zhid,宠物=cw+',',石头数量 = st[-4:],等级 = '2',更新时间 = gxsj,已卖='否')
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
                elif 0<int(a.宠物价值) < 1000:
                    pass
                else:
                    cw_5 = cw_5+ '[' + a.宠物编号 + a.宠物名字 + '] '
            except:
                cw_5 = cw_5 + '[' + data + '] '
    return cw_1+'\n'+cw_2+'\n'+cw_6+'\n'+cw_4+'\n'+cw_3+'\n'+cw_5

def chuli_1(cw):
    cw_1 = []
    cw_2 = []
    cw_3 = []
    cw_4 = []
    cw_6 = []
    cw_5 = []
    cw_7 = []
    for data in cw.split(','):
        if len(data) > 4 or len(data) < 3:
            continue
        else:
            try:
                a = duizhao.objects.get(pk=data)
                if int(a.宠物价值)==75000:
                    cw_1.append(a.宠物编号)
                elif int(a.宠物价值)==50000:
                    cw_2.append(a.宠物编号)
                elif int(a.宠物价值) == 25000:
                    cw_3.append(a.宠物编号)
                elif int(a.宠物价值) == 15000:
                    cw_4.append(a.宠物编号)
                elif int(a.宠物价值) == 10000:
                    cw_5.append(a.宠物编号)
                elif int(a.宠物价值)==6000:
                    cw_6.append(a.宠物编号)
                elif 0<int(a.宠物价值) < 1000:
                    pass
                else:
                    cw_7.append(a.宠物编号)
            except:
                pass
    return cw_1,cw_2,cw_3,cw_4,cw_5,cw_6,cw_7