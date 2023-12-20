from django.urls import path
from .views import (
    BookListApiView,
    BookDetailApiView,
    BookUpdateApiView,
    BookDeleteApiView,
    BookCreateApiView,
    get_options
)

urlpatterns = [
    path('all/', BookListApiView.as_view()),
    path('<int:pk>/book/', BookDetailApiView.as_view()),
    path('<int:pk>/delete/', BookDeleteApiView.as_view()),
    path('<int:pk>/update/', BookUpdateApiView.as_view()),
    path('create/', BookCreateApiView.as_view()),
    path('', get_options),
]

