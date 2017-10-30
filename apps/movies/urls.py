
from django.conf.urls import url, include
from apps.movies import views

app_name = 'movies'

movies_patterns = [
    url(r'^inicio/$', views.movie_list, name='home'),
    url(r'^(?P<pk>[0-9]+)/$', views.movie_list, name='movies-detail'),
    url(r'^(?P<pk>[0-9]+)/editar/$', views.movie_update, name='movies-edit'),
    url(r'^(?P<pk>[0-9]+)/eliminar/$', views.movie_delete, name='movies-delete')
]

urlpatterns = [
    url(r'^$', views.log_in, name='log_in'),
    url(r'^peliculas/', include(movies_patterns))
]