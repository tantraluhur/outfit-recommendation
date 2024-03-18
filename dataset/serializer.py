from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from dataset.models import Dataset
class DatasetSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Dataset
        fields = "__all__"
