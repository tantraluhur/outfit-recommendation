from abc import ABC

from commons.middlewares.exception import *
from django.db import transaction
from clothes.models import Clothes, Segmentation

class ClothesService(ABC):
    
    @classmethod
    @transaction.atomic
    def create_clothes(cls, **kwargs):
        data = {
            "clothes" : "",
            "segmentations" : []
        }
        segmentations = kwargs.pop("segmentations")
        clothes = kwargs
        clothes = Clothes.objects.create(**clothes)
        data['clothes'] = clothes
        for key, value in segmentations.items() :
            value['clothes'] = clothes
            segmentation = Segmentation.objects.create(**value)
            data['segmentations'].append(segmentation)

        return data
    
    @classmethod
    def get_clothes(cls) :
        data = []
        clothes = Clothes.objects.all()
        for i in clothes :
            segmentation = Segmentation.objects.filter(clothes=i)
            object_data = {
                "clothes" : i,
                "segmentations" : segmentation
            }
            data.append(object_data)

        return data
    
    @classmethod
    def get_clothes_detail(cls, id) :
        clothes = Clothes.objects.filter(id=id).first()
        if(not clothes) :
            raise NotFoundException(f"Clothes with id {id} not exists.")

        segmentation = Segmentation.objects.filter(clothes=clothes)
        data = {
            "clothes" : clothes,
            "segmentations" : segmentation
        }
        return data
    
    @classmethod
    def upload_image(cls, id, **kwargs) :
        clothes = Clothes.objects.filter(id=id).first()
        image = kwargs.get("image")
        if(not clothes) :
            raise NotFoundException(f"Clothes with id {id} not exists.")
        
        clothes.image = image
        clothes.save()

        return clothes

            
        



