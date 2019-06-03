# coding=utf
"""
author=Hui_T
"""
from rest_framework import serializers
from .models import Articles

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ["title","content","created"]

