from django.shortcuts import render
from rest_framework.views import APIView
from .models import Appointment,Appointment_Detail,payment
from rest_framework.response import Response
from rest_framework import status
from .serializer import appointmentserializer,appointment_detailserializer
class AppointmentApi(APIView):
    def get(self,request,pk=None,format=None):
        try:
            if pk is not None:
                data=Appointment.objects.get(id=pk)
                seri_data=appointmentserializer(data)
                return Response(seri_data.data)
            else:
                data=Appointment.objects.all()
                seri_data=appointmentserializer(data,many=True)
                return Response(seri_data.data)
        except Exception as obj:
            return Response('error',repr(obj))
        
    def post(self,request,format=None):
        try:
            if request.method == "POST":
                
                deseri_data= appointmentserializer(data=request.data)
                if deseri_data.is_valid():
                    deseri_data.save()
                    return Response({'msg':'data inserted successfully'})
                else:
                    return Response(deseri_data.errors)
                
                
                # data = Appointment()
                # data.doctor_id=request.data.get('doctor_id')
                # data.patient_id=request.data.get('patient_id')
                # data.date=request.data.get('date')
                # data.appointment_status = request.data.get('patient_status')
                # data.note=request.data.get('note')
                # data.save()
                
        except Exception as e:
            return Response('error',repr(e))