from django.urls import path

from clothes.views import ClothesView, ClothesDetailView


urlpatterns = [
    path('', ClothesView.as_view()),
    path('<int:id>/', ClothesDetailView.as_view())
]
