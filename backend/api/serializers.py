from rest_framework.serializers import ModelSerializer , SerializerMethodField , RelatedField , CharField
from .models import Quize 
from django.contrib.auth import  get_user_model




class Authorfirstnameandlastname(RelatedField):
	def to_representation(self, value):
		return value.first_name + " " + value.last_name

class QuizeSerializerGetter(ModelSerializer):
	

	owner = Authorfirstnameandlastname(read_only=True)		
	class Meta:
		model=Quize
		fields=['title','text','category','status','owner','file','date','pk']

class QuizeSerializerPost(ModelSerializer):		
	class Meta:
		model=Quize
		fields=['title','text','category','status','owner','file','date','pk']
			
class UserSerializer(ModelSerializer):
	class Meta:
		model=get_user_model()
		fields=['id','username','first_name','last_name','email','is_staff']
		



