from .models import Solicitud143_Step1
from rest_framework import serializers

class SolicitudesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Solicitud143_Step1
		fields = ['num_expediente','estado_solicitud']

