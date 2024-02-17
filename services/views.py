from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.parsers import JSONParser
from .models import Services_Model
from .serializer import servicesSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

class ServicesApi(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
    def get(self,request, pk=None,format =None):
        try:
            if pk is not None:
                data = Services_Model.objects.get(id = pk)
                seri_data = servicesSerializer(data)
                return Response(seri_data.data)
            else:
                data = Services_Model.objects.all()
                seri_data = servicesSerializer(data, many = True)
                return Response(seri_data.data)
        except Exception as obj:
             return Response({'error':repr(obj)},status= status.HTTP_400_BAD_REQUEST)
        
    def post(self,request,format = None):
        try:   
            deseri_data = servicesSerializer(data= request.data)
            if deseri_data.is_valid():
                deseri_data.save()
                return Response({'msg':'successfully Insert data'}, status= status.HTTP_202_ACCEPTED)
            else:
                return Response(deseri_data.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
                    return Res
        ponse({"error": repr(e) }, status= status.HTTP_400_BAD_REQUEST )

    def delete(self,request,pk=None,format=None):
         try:
            if pk is not None:
                fetch_data = Services_Model.objects.get(id = pk)
                fetch_data.delete()
                return Response({'msg':'data delete successfully'})
         except Exception as e:
             return Response({"error": repr(e) }, status= status.HTTP_400_BAD_REQUEST )
                              
    def put(self,request,pk=None,format=None):
         try:
                if pk is not None:
                   old_data = Services_Model.objects.get(id = pk)
                   deseri_data = servicesSerializer(old_data, data=request.data)
                   if deseri_data.is_valid():
                        deseri_data.save()
                        return Response({'msg':'successfully Update data'}, status= status.HTTP_202_ACCEPTED)
                else:
                    return Response(deseri_data.errors, status= status.HTTP_400_BAD_REQUEST)
         except Exception as e:
             return Response({'error': repr(e) }, status= status.HTTP_400_BAD_REQUEST ) 

# Create your views here.
