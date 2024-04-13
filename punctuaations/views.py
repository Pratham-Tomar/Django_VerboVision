from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    textara=request.POST.get('text','default')
    checkbx=request.POST.get('ip','off')
    uppercas=request.POST.get('To_uppercase','off')
    lowercas=request.POST.get('To_lowercase','off')
    newlineremove=request.POST.get('newlineremover','off')
    spaceremove=request.POST.get('spaceremover','off')
    charcounter=request.POST.get('charcount','off')
    if checkbx=="on":
        punctuations = '''!()-[]{ };:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for i in textara:
            if i not in punctuations:
                analyzed=analyzed+i
        params={'purpose':'Your Text Punctuation-Stripped Text  is here','analyzed_code':analyzed}
        textara=analyzed
        # return render(request,'analyze.html',params)
    if uppercas=="on":
        analyzed=""
        for i in textara:
            analyzed=analyzed+i.upper()
            params={'purpose':'Your Text Transformed to Uppercase is here','analyzed_code':analyzed}
        textara=analyzed
        # return render(request,'analyze.html',params)
    if lowercas=="on":
        analyzed=""
        for i in textara:
            analyzed=analyzed+i.lower()
        params={'purpose':'Your Text Transformed to Lowercase is here','analyzed_code':analyzed}
        textara=analyzed
    # return render(request,'analyze.html',params)
    if newlineremove=="on":
        analyzed=""
        for i in textara:
            if i!="\n" and i!="\r":
                analyzed=analyzed+i
        params={'purpose':'Your Text with Line-Free Output  is Here ','analyzed_code':analyzed}
        textara=analyzed
        # return render(request,'analyze.html',params)
    if spaceremove=="on":
        analyzed=""
        for index,char in enumerate(textara):
            if not (textara[index]==" " and textara[index+1]==" "):
                analyzed=analyzed+char 
        params={'purpose':'Your Text with Space-Free Output is Here ','analyzed_code':analyzed}
        textara=analyzed
        
    
        # return render(request,'analyze.html',params)
    if charcounter=="on":
        count=0
        for i in textara:
            if i!=" ":
                count+=1;
                analyzed=count;
        params={'purpose':'Total Characters in the statements are','analyzed_code':count}
        textara=analyzed
        

    
    if(spaceremove!="on" and newlineremove!="on" and lowercas!="on" and charcounter!="on" and  uppercas!="on" and checkbx!="on"):
        return HttpResponse("<h1>Error</h1> \n <h1> Please Do Belect Any Options Below</h1>")
    return render(request,'analyze.html',params)
