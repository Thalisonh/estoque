from django.shortcuts import render
from produto.models import Produto

def home(request):
    produtos = Produto.objects.all().order_by('-id')

    return render(request, 'produto/index.html', {'produtos': produtos})

# Create your views here.
