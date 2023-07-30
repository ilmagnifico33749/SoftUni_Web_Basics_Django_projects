from django.contrib import admin
from django.urls import path, include

# from Project_05_Class_Based_Views.web.views import list_articles, ArticlesListView
from Project_05_Class_Based_Views.web.views import ArticlesListView, ArticleDetailView, \
    ArticleCreateView, ArticleDeleteView


urlpatterns = (
    path('', ArticlesListView.as_view(), name='list_articles'),
    path('<int:pk>', ArticleDetailView.as_view(), name='details_article'),
    path('create/', ArticleCreateView.as_view(), name='create_article'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete_article'),

)

