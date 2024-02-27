from django.shortcuts import render
from rest_framework.views import APIView
from .models import Appointment,Appointment_Detail,payment
from rest_framework.response import Response
from rest_framework import status
from .serializer import appointmentserializer,appointment_detailserializer
from patient.serializer import patientSerializer
from rest_framework import status
from rest_framework import viewsets
from patient.models import Patient_Model
from .models import Appointment
# class AppointmentApiViewSet(viewsets.ModelViewSet):
#     queryset = Appointment.objects.all()
#     serializer_class = appointmentserializer

#     def list(self,request):
#         appoint_serializer = appointmentserializer(self.queryset,many=True)
#         return Response(appoint_serializer.data)
    
#     def create(self, request, *args, **kwargs):
#         # Assuming the patient data is sent along with the appointment data in the request
#         patient_serializer = patientSerializer(data=request.data.get('patient'))
#         if patient_serializer.is_valid():
#             patient_instance = patient_serializer.save()
#             # Link the appointment to the newly created patient
#             request.data['patient'] = patient_instance.pk
#             appointment_serializer = self.get_serializer(data=request.data)
#             if appointment_serializer.is_valid():
#                 appointment_serializer.save()
#                 return Response(appointment_serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
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
            return Response({'error',repr(obj)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self,request,format=None):
        try:

            if request.method == "POST":
                patient_data = request.data.get('patient')
                appointment_data = request.data.get('appointment')
                # print(request.data)
                # Check if patient data exists in the request
                if patient_data is None:
                    return Response({'error': 'Patient data is missing'}, status=status.HTTP_400_BAD_REQUEST)

                # Serialize patient data
                deseri_patient = patientSerializer(data=patient_data)
                if deseri_patient.is_valid():
                    patient_instance = deseri_patient.save()
                else:
                    return Response(deseri_patient.errors, status=status.HTTP_400_BAD_REQUEST)
                
                # # Add patient_id to appointment data
                
                appointment_data['patient'] = {'id': patient_instance.id}

                # appointment_data['patient_id'] = patient_instance.id
                # print("add patient id ")
                print(appointment_data)
                # Serialize appointment data
                deseri_appointment = appointmentserializer(data=appointment_data)
                if deseri_appointment.is_valid():
                    deseri_appointment.save()
                    return Response({'msg': 'Patient and appointment data inserted successfully'}, status=status.HTTP_201_CREATED)
                else:
                    
                    return Response(deseri_appointment.errors, status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            return Response({'error': repr(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # try:
        #     if request.method == "POST":
        #         patient_data = request.data.get('patient')
        #         appointment_data = request.data.get('appointment')
        #         deseri_patient= patientSerializer(data=patient_data)
        #         if deseri_patient.is_valid():
        #             patient =deseri_patient.save()
                    
        #         else:
        #             return Response(deseri_patient.errors, status=status.HTTP_400_BAD_REQUEST)
                
        #         patient_id = patient.id
        #         doctor_id = request.data.get('doctor_id')
        #         date = request.data.get('date')
        #         appointment_status = request.data.get('appointment_status')
        #         note= request.data.get('note')
        #         data = {'patient_id':patient_id,'doctor_id':doctor_id,'date':date,'appointment_status':appointment_status,'note':note}
        #         deseri_appointment = appointmentserializer(data=data)
        #         if deseri_appointment.is_valid():
        #             deseri_appointment.save()
        #             return Response({'msg':'Patient and appointment data inserted successfully'}, status=status.HTTP_201_CREATED)
        #         else:
        #             return Response(deseri_appointment.errors, status=status.HTTP_400_BAD_REQUEST)
                
                
        # except Exception as e:
        #     return Response({'error':repr(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)