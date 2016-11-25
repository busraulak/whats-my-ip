from django.http import HttpResponse
import datetime

now = datetime.datetime.now().strftime('%H:%M:%S')

def post_list(request):
    ip = request.META['REMOTE_ADDR']
    return HttpResponse("Merhaba, {}, saat su an {}".format(ip, now))