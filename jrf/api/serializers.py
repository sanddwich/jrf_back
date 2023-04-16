from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from .models import *
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:       
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active']
        

class GroupSerializer(serializers.ModelSerializer):
    class Meta:       
        model = Group
        fields = ['id', 'name']
        

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:       
        model = Permission
        fields = ['id', 'name', 'codename']
        

class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = Articles
        fields = ['id', 'title', 'info', 'content', 'slug', 'create_date', 'ispublished', 'category', 'user']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'create_date', 'slug']