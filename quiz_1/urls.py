from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup', views.SignUpView.as_view(), name='signup'),
    path('quiz/<int:pk>/', views.QuizDetail.as_view(), name='quiz'),
    path('', views.QuizListView.as_view(), name='all_quizzes')
]
