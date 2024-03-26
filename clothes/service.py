from abc import ABC

from commons.middlewares.exception import *
from django.db import transaction
from clothes.models import Clothes, Segmentation
from dataset.models import Dataset

class ClothesService(ABC):
    
    @classmethod
    @transaction.atomic
    def create_clothes(cls, dataset_id, **kwargs):
        data = {
            "clothes" : "",
            "segmentations" : []
        }

        dataset = Dataset.objects.filter(id=dataset_id).first()
        if(not dataset) :
            raise NotFoundException(f"Dataset with id {dataset_id} not exists.")
        
        segmentations = kwargs.pop("segmentations")
        clothes = kwargs
        clothes = Clothes.objects.create(**clothes, dataset=dataset)
        data['clothes'] = clothes
        for key, value in segmentations.items() :
            value['clothes'] = clothes
            segmentation = Segmentation.objects.create(**value)
            data['segmentations'].append(segmentation)

        return data
    
    @classmethod
    def get_clothes(cls, dataset_id) :
        # data = []
        dataset = Dataset.objects.filter(id=dataset_id).first()
        if(not dataset) :
            raise NotFoundException(f"Dataset with id {dataset_id} not exists.")
        
        clothes = Clothes.objects.filter(dataset=dataset)
        # for i in clothes :
        #     segmentation = Segmentation.objects.filter(clothes=i)
        #     object_data = {
        #         "clothes" : i,
        #         "segmentations" : segmentation
        #     }
        #     data.append(object_data)

        return clothes
    
    @classmethod
    def get_clothes_detail(cls, id) :
        clothes = Clothes.objects.filter(id=id).first()
        if(not clothes) :
            raise NotFoundException(f"Clothes with id {id} not exists.")

        # segmentation = Segmentation.objects.filter(clothes=clothes)
        # data = {
        #     "clothes" : clothes,
        #     "segmentations" : segmentation
        # }
        return clothes
    
    @classmethod
    def upload_image(cls, id, **kwargs) :
        clothes = Clothes.objects.filter(id=id).first()
        image = kwargs.get("image")
        if(not clothes) :
            raise NotFoundException(f"Clothes with id {id} not exists.")
        
        clothes.image = image
        clothes.save()

        return clothes

            
        



