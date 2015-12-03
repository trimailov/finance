from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin

from accounts import urls as accounts_urls
from books import urls as books_urls
from finance.views import home as finance_views_home


urlpatterns = [
    # Examples:
    url(r'^$', finance_views_home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^books/', include(books_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
