from django.urls import path

from clothes.views import ClothesView, ClothesDetailView


urlpatterns = [
    path('<int:id>/', ClothesView.as_view()),
    path('upload-image/<int:id>/', ClothesDetailView.as_view())
]
