from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from .views import dashboard, create_payment, edit_payment

import session_csrf
session_csrf.monkeypatch()

urlpatterns = (
    # Examples:
    # url(r'^$', 'odengec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^_ah/', include('djangae.urls')),

    # Note that by default this is also locked down with login:admin in app.yaml
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^csp/', include('cspreports.urls')),

    url(r'^auth/', include('djangae.contrib.gauth.urls')),

    url(r'^$', dashboard, name='dashboard'),
    url(r'^payment/create/$', create_payment, name='create_payment'),
    url(r'^payment/(?P<pk>[\d]+)/$', edit_payment, name='edit_payment'),
)

if settings.DEBUG:
    urlpatterns += tuple(static(settings.STATIC_URL, view=serve, show_indexes=True))
