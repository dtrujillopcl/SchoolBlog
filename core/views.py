from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

# Create your views here.

def home(request):
    noticias = Post.objects.all()
    data = {
        'noticias':noticias
    }

    return render(request, 'core/home.html', data)

def noticias(request):
    noticias = Post.objects.order_by('created_date')
    paginator = Paginator(noticias, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'noticias':noticias,
        'page_obj': page_obj,
        'paginator':paginator
    }
    return render(request, 'core/noticias.html', data)

def postNoticia(request, id):
    noticia = Post.objects.get(id=id)
    data = {
        'noticia': noticia
    }
    print(noticia)

    return render(request, 'core/post.html', data)