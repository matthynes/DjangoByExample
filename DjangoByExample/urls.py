from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.views.generic import RedirectView

from blog.feeds import LatestPostsFeed
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='blog'), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',
        include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]
