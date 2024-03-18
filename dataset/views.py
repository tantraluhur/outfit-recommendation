from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from applibs.response import prepare_success_response, prepare_error_response, serializer_error_response
from dataset.serializer import DatasetSerializer
from dataset.models import Dataset

class DatasetView(APIView) :
    def __init__(self) :
        self.serializer = DatasetSerializer

    def post(self, request) :
        serializer = self.serializer(data=request.data)
        if(not serializer.is_valid()) :
            return Response(serializer_error_response(serializer.errors), status.HTTP_400_BAD_REQUEST)
        try :
            serializer.save()
            return Response(prepare_success_response(serializer.validated_data), status.HTTP_201_CREATED)
        except APIException as e :
            return Response(prepare_error_response(str(e)), e.status_code)
        except Exception as e :
            return Response(prepare_error_response(str(e)), status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self, request) :
        try :
            dataset = Dataset.objects.all()
            serializer = self.serializer(dataset, many=True)
            return Response(prepare_success_response(serializer.data), status.HTTP_201_CREATED)
        except APIException as e :
            return Response(prepare_error_response(str(e)), e.status_code)
        except Exception as e :
            return Response(prepare_error_response(str(e)), status.HTTP_500_INTERNAL_SERVER_ERROR)
        