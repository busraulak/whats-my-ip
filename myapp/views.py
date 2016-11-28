
from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
   return render(request, "hello.html", {})

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

from django.http import HttpResponse
import datetime

now = datetime.datetime.now().strftime('%H:%M:%S')

def post_list(request):
    ip = request.META['REMOTE_ADDR']
    return HttpResponse("Merhaba, {}, saat su an {}".format(ip, now))

