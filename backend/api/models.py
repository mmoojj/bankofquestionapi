from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html
from .extensions.utils import  jalali_convertor
# Create your models here.
class User(AbstractUser):
	image=models.ImageField(upload_to="images", null=True)

	def image_tag(self):
		if self.image:
			return format_html("<img style='width:30;height:50px' src='{}'></img>".format(self.image.url))


class Quize(models.Model):
	title = models.CharField(max_length=100,null=True)
	text = models.TextField(max_length=500,null=True)
	category = models.CharField(max_length=100,null=True)
	status = models.CharField(max_length=1,default="d")
	created_at = models.DateTimeField(auto_now=True)
	owner = models.ForeignKey(get_user_model(),models.CASCADE)
	file  = models.FileField(upload_to="file" , null=True)

	class Meta:
		ordering = ['-pk']


	def date(self):
		return jalali_convertor(self.created_at)

	def __str__(self):
		return self.title

	def ispublish(self):
		if self.status == 'p':
			return True
		return False

	ispublish.boolean = True	