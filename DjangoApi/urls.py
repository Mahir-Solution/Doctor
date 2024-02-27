"""
URL configuration for DjangoApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from services.views import ServicesApi
from patient.views import patientApi
from staff.views import StaffApi
from appointment import views
from appointment.views import AppointmentApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register("appointment",views.AppointmentApiViewSet,basename="appointment")
# router.register("appointment",views.AppointmentApiViewSet,basename="appointment")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/<int:pk>/',ServicesApi.as_view()),
    path('services/',ServicesApi.as_view()),
    path('patient/',patientApi.as_view()),
    path('patient/<int:pk>/',patientApi.as_view()),
    path('staff/',StaffApi.as_view()),
    path('staff/<int:pk>/',StaffApi.as_view()),
    path('api/',include(router.urls)),
    path('appointment/',AppointmentApi.as_view()),

    path('appointment/<int:pk>/',AppointmentApi.as_view()),
    
    path('login/',include('rest_framework.urls', namespace="rest_framework")),
]
