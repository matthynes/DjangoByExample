from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='blog'), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',
        include('blog.urls', namespace='blog', app_name='blog')),
]
