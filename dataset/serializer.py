from rest_framework import serializers

from dataset.models import Dataset
from clothes.models import Clothes

class DatasetSerializer(serializers.ModelSerializer) :
    total_image = serializers.SerializerMethodField('get_total_image')
    class Meta :
        model = Dataset
        fields = "__all__"

    def get_total_image(self, instance):
        total_image = Clothes.objects.filter(dataset__id=instance.id).count()
        return total_image
