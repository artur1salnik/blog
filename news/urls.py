from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.new, name='new'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]