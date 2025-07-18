from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from bs4 import BeautifulSoup
def home(request):
    return render(request, 'basic.html', locals())

def analyzeData(request):
    try:
        html = request.POST['html']
        ALLList = request.POST.getlist('ALLList[]')
        ADDList = request.POST.getlist('ADDList[]')
        DECList = request.POST.getlist('DECList[]')
    except:
        html = None
        ALLList = []
        ADDList = []
        DECList = []
    Status = "發生錯誤"
    CrawlerCount = 0
    CrawlerList = []
    OriginalOptions = []
    if bool(BeautifulSoup(html, "html.parser").find()):
        soup = BeautifulSoup(html, 'html.parser')
        fans = soup.find_all("span", class_="_ap3a _aaco _aacw _aacx _aad7 _aade")
        for i in fans:
            CrawlerCount += 1
            CrawlerList.append(i.text)

        if len(ALLList) != 0:
            for i in CrawlerList:
                if i not in ALLList:
                    if i not in ADDList:
                        ADDList.append(i)
            for i in ALLList:
                if i not in CrawlerList:
                    if i not in DECList:
                        DECList.append(i)
            Status = "未出現+" + str(len(ADDList)) + "：疑似少+" + str(len(DECList))
        else:
            ALLList = CrawlerList
            Status = "首次分析成功"

        ALLList = ALLList + ADDList
        ADDCount = len(ADDList)
        DECCount = len(DECList)
        ALLCount = len(ALLList)

    else:
        Status = "元素必須為HTML"


    return JsonResponse({'ALLList':ALLList, 'ALLCount':ALLCount, 'ADDList':ADDList, 'ADDCount':ADDCount, 'DECList':DECList, 'DECCount':DECCount, 'CrawlerCount':CrawlerCount, 'Status':Status}, safe=False)