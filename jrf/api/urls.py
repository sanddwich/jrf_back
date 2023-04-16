from django.http import HttpResponse
from django.urls import path, include, re_path
from .views import *
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# router = routers.SimpleRouter()
router = routers.DefaultRouter()
router.register(r'articles', ArticlesViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'users', UsersViewSet)
router.register(r'groups', GroupsViewSet)
router.register(r'permissions', PermissionsViewSet)

# print(router.urls)

urlpatterns = [
    path('v1/', include(router.urls)),
      
    # path('v1/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # path('v1/articles', ArticlesViewSet.as_view({'get': 'list'})),
    # path('v1/articles/<int:pk>', ArticlesViewSet.as_view({'put': 'update'})),
    # path('v1/categories/', CategoriesViewSet.as_view({'get': 'list'})),
    # path('v1/categories/<int:pk>', CategoriesViewSet.as_view({'put': 'update'})),

    # path('v1/article_list', ArticlesViewSet.as_view()),
    # path('v1/category_test', CategoriesViewSet.as_view()),
]