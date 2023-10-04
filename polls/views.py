# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, abc_world. You're at the polls index.")