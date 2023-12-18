from django.urls import path, include
from .views import RegisterView, BookView, BookDetailedView, BookReview

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name="sign_up"),

    path('book/', BookView.as_view(), name="book"),
    path('book/<int:pk>/', BookDetailedView.as_view(), name="book_detailed"),
    path('book/review/<int:pk>/', BookReview.as_view(), name="book"),
]