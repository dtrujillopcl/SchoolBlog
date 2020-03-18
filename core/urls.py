from django.urls import path
from .views import home, noticias, postNoticia

urlpatterns = [
    path('', home, name='home'),
    path('noticias/', noticias, name='noticias'),
    path('noticia/<id>', postNoticia, name='postNoticia')
]