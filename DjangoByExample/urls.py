from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',
        include('DBE_blog.urls', namespace='blog', app_name='blog')),
]
