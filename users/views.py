from rest_framework.decorators import api_view
from rest_framework.response import Response 

# Create your views here.
@api_view(['GET'])
def hello(request):
    return Response('hello')