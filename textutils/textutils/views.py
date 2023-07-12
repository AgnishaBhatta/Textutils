#i created this
from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
    #return HttpResponse('''<h4>hello Agnisha</h4><a href ="https://www.youtube.com/@DevDynamos_">Django coderAgnisha</a>''')
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("<h1>home</h1>")
#personal navigator
def ex1(request):
    s='''<h1>Navigation bar<br></h1>
    <a href="https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12">video</a><br>
    <a href="https://mail.google.com/mail/u/0/#inbox">mail</a><br>'''
    return HttpResponse(s)
def analyse(request):
    djtext=request.POST.get('text','default')
    remove_punc=request.POST.get('analyse','default')
    capfirst=request.POST.get('capfirst','default')
    unique=request.POST.get('unique','default')
    print(djtext)
    print(remove_punc)
    print(capfirst)
    #return HttpResponse("<h4>remove punctuation</h4>")
    #analyse=djtext
    if remove_punc=="on":
        punctuation='''"";:?''></.,{}[]|\+=!@#$%^&*()'''
        analyse=""
        for char in djtext:
            if char not in punctuation:
                analyse=analyse + char
        params={'purpose':"removed punctuation",'analysed_text':analyse}
        djtext=analyse
        #return render(request, 'analyse.html', params)
    if capfirst=="on":
        ana=""
        for i in djtext:
            ana=ana+ i.capitalize()
        params={'purpose':"capitalised",'analysed_text':ana}
        #return render(request, 'analyse.html',params)
        djtext=ana
    if unique=="on":
        def check_unique(str):
            for i in range(len(str)):
                for j in range(i + 1,len(str)):
                    if(str[i] == str[j]):
                        return False
                return True
        x=check_unique(djtext)
        params={'purpose':"whether it is unique or not",'analysed_text':x,"originaltext":djtext,"abc":"yes"}
        #return render(request, 'analyse.html', params)
        return render(request, 'analyse.html', params)
    if (remove_punc!="on" and capfirst!="on" and unique!="on"):
     return HttpResponse("error")
'''def cap_first(request):
    return HttpResponse("<h2>capitalise first</h2>")
def newlineremove(request):
    return HttpResponse("<h2>remove newline</h2><a href='/'>back</a>")
def spaceremove(request):
    return HttpResponse("<h2>spaceremove</h2>")'''