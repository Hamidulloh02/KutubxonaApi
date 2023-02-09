from rest_framework import serializers
from .models import TeatrArxiv
from .models import Category


class TeatrArxivSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeatrArxiv
        fields = ['year','title','image','body','is_active','updated_at','created_at']

class TeatrArxivCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','is_active']