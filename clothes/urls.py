from django.urls import path

from clothes.views import ClothesView, ClothesDetailView, UploadImageView, SegmentationView


urlpatterns = [
    path('<int:id>/', ClothesView.as_view()),
    path('detail/<int:id>/', ClothesDetailView.as_view()),
    path('upload-image/<int:id>/', UploadImageView.as_view()),
    path('segmentation/<int:id>/', SegmentationView.as_view()),
]
