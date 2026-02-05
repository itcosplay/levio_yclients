from django.urls import path

from .views.hai import HiView

urlpatterns = [
    path("test", HiView.as_view()),
]
