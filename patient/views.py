from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Patient_Model
from .serializer import patientSerializer

class patientApi(APIView):
    def get(self,request,pk=None,format=None):
        try:
            if pk is not None:
                fetch_data = Patient_Model.objects.get(id=pk)
                seri_data = patientSerializer(fetch_data)
                return Response(seri_data.data)
            else:
                fetch_data = Patient_Model.objects.all()
                seri_data = patientSerializer(fetch_data , many = True)
                return Response(seri_data.data)
        except Exception as obj:
            return Response({'errors':repr(obj)}, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self,request,format=None):
        try: 
            deseri_data = patientSerializer(data= request.data)
            if deseri_data.is_valid():
                deseri_data.save()
                return Response({'mag':'data insert successfully'},status= status.HTTP_201_CREATED)
            else:
                 return Response(deseri_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as obj:
                 return Response({'errors':repr(obj)}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None,format=None):
        try:
            if pk is not None:
                fetch_data = Patient_Model.objects.get(id = pk)
                if fetch_data is not None:
                    fetch_data.delete()
                    return Response({'msg':'delete data successfully'})
            
        except Exception as obj:
                 return Response({'errors':repr(obj)}, status=status.HTTP_400_BAD_REQUEST) 
     
    def put(self,request,pk=None,format = None):
        try:
              if pk is not None:
                   old_data = Patient_Model.objects.get(id = pk)
                   deseri_data = patientSerializer(old_data, data=request.data)
                   if deseri_data.is_valid():
                        deseri_data.save()
                        return Response({'msg':'update data successfully'})
        except Exception as obj:
             return Response({'errors':repr(obj)}, status=status.HTTP_400_BAD_REQUEST)
         
# Create your views here.
