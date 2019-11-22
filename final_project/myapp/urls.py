from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    path('hello/', views.hello, name = 'hello'),
    path('morning/', views.morning, name = 'morning'),
    path('article/<int:articleId>/', views.viewArticle, name = 'article')
]