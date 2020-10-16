from django.urls import re_path, path
from basic_app import views

# For template tagging to work, need to see global variable app_name
app_name = 'basic_app'

urlpatterns = [
    # path('', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
