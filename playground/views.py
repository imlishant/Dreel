from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# 1. description
## 2. video se caption
## 3. time cut silnce remover. stable timecutt.
# 4. video pe video merge 
# 5. photo frame by frame overlay

def say_hello(request):
    # return HttpResponse("Heeloo Mere World")
    return render(request, 'hello.html', {'name':'Lishant'})



