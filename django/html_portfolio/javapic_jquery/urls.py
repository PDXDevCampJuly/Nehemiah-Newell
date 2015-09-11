from django.conf.urls import include, url
from javapic_jquery import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.index_jquery, name='index'),
    url(r'^join.html/',views.join_jquery, name='join'),
    url(r'^gallery.html/',views.gallery_jquery, name='gallery')
]
