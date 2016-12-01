from django.http import HttpResponse
import datetime
now = datetime.datetime.now().strftime('%H:%M:%S')
def post_list(request):
        ip = request.META.get('HTTP_X_REAL_IP')
        return HttpResponse("Merhaba, {}, saat su an {}".format(ip, now))
