from django.urls import path, include
from . import views # urls.py에 들어갈 함수 및 클래스는 views.py에 정의
# FBV(Function Based View) : 함수 기반으로 직접 구현
# CBV(Class Based View) : 장고에서 제공하는 클래스를 이용한 정의

urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
    path('', include('single_pages.urls')),
]