from rest_framework.views import APIView
from .models import Clicks
from rest_framework.response import Response

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class MainApi(APIView):

    def get(self, request, *args, **kwargs):
        click, is_created = Clicks.objects.update_or_create(ip = get_client_ip(request))
        return Response({'total':Clicks.objects.all().count()})