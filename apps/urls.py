# coding=utf
"""
author=Hui_T
"""
from rest_framework.routers import DefaultRouter
from .views import Article
urlpatterns = [ ]

routers = DefaultRouter()

routers.register('article',Article)
urlpatterns+=routers.urls