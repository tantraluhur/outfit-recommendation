from rest_framework import serializers

from clothes.models import Clothes, Segmentation

class CreateClothesSerializer(serializers.ModelSerializer) :
    segmentations = serializers.JSONField()
    class Meta :
        model = Clothes
        fields = "__all__"

    def validate(self, attrs) :
        segmentation = attrs.get("segmentations", None)
        for _, value in segmentation.items() :
            serializer = SegmentationSerializer(data=value)
            if(not serializer.is_valid()) :
                raise serializers.ValidationError(serializer.errors)
        return attrs
    
class ClothesSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Clothes
        fields = "__all__"


class SegmentationSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Segmentation
        fields = ['id', 'part', 'size', 'segmantation_colour']

class ClothesImageUploadSerializer(serializers.Serializer) :
    image = serializers.ImageField()

class ResponseSerializer(serializers.Serializer) :
    clothes = ClothesSerializer()
    segmentations = SegmentationSerializer(many=True)