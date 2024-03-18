from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from applibs.response import prepare_success_response, prepare_error_response, serializer_error_response

from clothes.serializer import ResponseSerializer, CreateClothesSerializer, ClothesImageUploadSerializer, ClothesSerializer
from clothes.service import ClothesService
from clothes.models import Clothes

class ClothesView(APIView) :
    def __init__(self) :
        self.serializer = CreateClothesSerializer
        self.response_serializer = ResponseSerializer

    def post(self, request) :
        try :
            serializer = self.serializer(data=request.data)
            if(not serializer.is_valid()) :
                return Response(serializer_error_response(serializer.errors), status.HTTP_400_BAD_REQUEST)

            data = ClothesService.create_clothes(**serializer.validated_data)
            serializer_response = self.response_serializer(data)
            return Response(prepare_success_response(serializer_response.data), status.HTTP_201_CREATED)
        except APIException as e :
            return Response(prepare_error_response(str(e)), e.status_code)
        except Exception as e :
            return Response(prepare_error_response(str(e)), status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request) :
        try :
            data = ClothesService.get_clothes()
            serializer = self.response_serializer(data, many=True)
            return Response(prepare_success_response(serializer.data), status.HTTP_200_OK)
        except APIException as e :
            return Response(prepare_error_response(str(e)), e.status_code)
        except Exception as e :
            return Response(prepare_error_response(str(e)), status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ClothesDetailView(APIView) :

    def __init__(self) :
        self.serializer =  ClothesImageUploadSerializer
        self.clothes_serializer = ClothesSerializer
        self.response_serializer = ResponseSerializer

    def post(self, request, id) :
        try :
            serializer = self.serializer(data=request.data)
            if(not serializer.is_valid()) :
                return Response(serializer_error_response(serializer.errors), status.HTTP_400_BAD_REQUEST)
            
            data = ClothesService.upload_image(id, **serializer.validated_data)
            serializer = self.clothes_serializer(data)
            return Response(prepare_success_response(serializer.data), status.HTTP_201_CREATED)
        except APIException as e :
            return Response(prepare_error_response(str(e)), e.status_code)
        except Exception as e :
            return Response(prepare_error_response(str(e)), status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, id) :
        try :
            data = ClothesService.get_clothes_detail(id)
            serializer = self.response_serializer(data)
            return Response(prepare_success_response(serializer.data), status.HTTP_200_OK)
        except APIException as e :
            return Response(prepare_error_response(str(e)), e.status_code)
        except Exception as e :
            return Response(prepare_error_response(str(e)), status.HTTP_500_INTERNAL_SERVER_ERROR)