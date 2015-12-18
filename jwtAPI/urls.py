from django.contrib import admin
from django.conf.urls import include, url, patterns

from rest_framework_nested import routers
from authentication.views import UserViewSet, GroupViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = patterns(
    '',
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    # url('^.*$', IndexView.as_view(), name='index'),
)
