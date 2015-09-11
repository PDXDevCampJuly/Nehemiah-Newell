from django.conf.urls import include, url
import about.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'html_portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'forum/',include('forum.urls')),
    url(r'javapic/',include('javapic.urls')),
    url(r'javapic_jquery/',include('javapic_jquery.urls')),
    url(r'zen_mockup/',include('zen_mockup.urls')),
    url(r'about/',include('about.urls')),
    url(r'^$',about.views.table_of_contents, name='table_of_contents'),
]
