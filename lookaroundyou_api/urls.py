from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from .people.views import PersonViewSet

admin.autodiscover()

api_router = routers.SimpleRouter(trailing_slash=False)
api_router.register('people', PersonViewSet)

urlpatterns = patterns('',
    (r'^api/v1/', include(api_router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
