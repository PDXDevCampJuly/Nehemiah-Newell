from django.conf.urls import include, url
from javapic import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index, name='index'),
    url(r'^join.html/',views.join, name='join'),
    url(r'^gallery.html/',views.gallery, name='gallery')
]
