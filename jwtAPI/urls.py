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

    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^api-token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),

)
