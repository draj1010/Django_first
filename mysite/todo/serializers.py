from rest_framework import serializers
from .models import Userx

class UserxSerializers(serializers.ModelSerializer):
	class Meta:
		model = Userx
		fields = '__all__'