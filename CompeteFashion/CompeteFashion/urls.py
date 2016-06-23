"""CompeteFashion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap
from django.contrib.sitemaps import views
from zinnia.views.channels import EntryChannel


sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^FashionPoll/', include('FashionPoll.urls')),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^sitemap.xml$', views.index ,sitemaps),
    url(r'^sitemap-(?P<section>.+)\.xml$', views.sitemap, sitemaps),
    url(r'^weblog/$', EntryChannel.as_view(query='category:python OR category:django')),
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
