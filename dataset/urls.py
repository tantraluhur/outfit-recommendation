from django.urls import path

from dataset.views import DatasetView

urlpatterns = [
    path('', DatasetView.as_view()),
]
