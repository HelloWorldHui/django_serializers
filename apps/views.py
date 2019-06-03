from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .models import Articles
from .serializers import ArticleSerializer

class Article(ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer