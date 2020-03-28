from django.urls import path, include
from rest_framework import routers
from siteusers.api import views

router = routers.DefaultRouter()
# 注册名为users的路由，网址通过此名称访问
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),   # 可用于用户登陆
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
