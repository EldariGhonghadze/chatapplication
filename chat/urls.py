from django.urls import path

from chat.views import HomeView, QuestionCreateView, QuestionDetailView, QuestionDeleteView, QuestionUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('question/create/', QuestionCreateView.as_view(), name='question-create'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('questions/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
    path('questions/<int:pk>/update/', QuestionUpdateView.as_view(), name='question-update'),
]
