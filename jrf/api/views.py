from django.http import HttpResponse, Http404
from rest_framework import generics, viewsets, mixins
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import *
from .serializers import *
from .permissions import *
from .paginations import *


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserViewSetPagination


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = GroupViewSetPagination


class PermissionsViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all().order_by('id')
    serializer_class = PermissionSerializer
    pagination_class = PermissionViewSetPagination
    

# Create your views here. ModelViewSet
class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlesViewSetPagination
    # permission_classes = [
    #     IsAuthenticated,
    #     isAdminOrReadOnly,
    # ]
    
    # def get_queryset(self):
    #     pk = self.kwargs.get("pk")
    #     if not pk:
    #         return Articles.objects.all()[:3]        
    #     return Articles.objects.filter(pk=pk)
    
    @action(methods=['get'], detail=False)
    def cats(self, request):
        categories = Categories.objects.all().values()
        return Response({
            "categories": categories
        })
    
# Create your views here. ModelViewSet
# class ArticlesViewSet(mixins.CreateModelMixin,
#                         mixins.RetrieveModelMixin,
#                         mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin,
#                         mixins.ListModelMixin,
#                         viewsets.GenericViewSet):
#     queryset = Articles.objects.all()
#     serializer_class = ArticleSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        IsAuthenticated,
        # IsAuthenticatedOrReadOnly
    ]
    # authentication_classes = [TokenAuthentication]   #Конкретный Способ аутентификации для данной вьюхи

# class ArticlesAPIView(generics.ListAPIView):
#     queryset = Articles.objects.all()
#     serializer_class = ArticleSerializer

# class CategoryAPIViewTest(APIView):
#     def get(self, request):
#         obj = Categories.objects.all()
#         serializer = CategorySerializer(obj, many=True)
#         return Response({
#             "data": "CategoryAPIViewTest GET",
#             "requestData": serializer.data,
#         })
#
#     def post(self, request):
#         return Response({
#             "data": "CategoryAPIViewTest POST",
#             "requestData": request.data,
#         })