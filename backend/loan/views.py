from django.shortcuts import render
from django.http import JsonResponse
from .models import Userdetails
from .serializers import UserdeatilsSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def get_users_list(request):
    if request.method == 'GET':
        users_list = Userdetails.objects.order_by('-apply_date')
        serializer = UserdeatilsSerializer(users_list, many=True)
        return JsonResponse(serializer.data, safe=False)


