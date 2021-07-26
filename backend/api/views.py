from rest_framework.generics import  ListAPIView 
from rest_framework.viewsets import ModelViewSet
from .models import Quize 
from rest_framework import filters
from django.contrib.auth import  get_user_model
from rest_framework.permissions import IsAuthenticated ,IsAdminUser 
from .serializers import QuizeSerializerGetter , QuizeSerializerPost , UserSerializer
from .mixins import IsOwnerOrSuperuser , IsSuperuser
# Create your views here.


# this view useed  for ananyomst user
class QuizeListView(ListAPIView):
    queryset=Quize.objects.filter(status='p')
    serializer_class=QuizeSerializerGetter
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'text']

#this view used for authors and superuser 
class QuizeCreateView(ModelViewSet):

    def get_queryset(self):
        if self.request.user.is_staff and not self.request.user.is_superuser and self.action == 'list':
            return Quize.objects.filter(owner=self.request.user,status='d')    
        return  Quize.objects.all()   

    def get_permissions(self):
        if self.action in ["update","retrieve","destroy"]:
            permission_classes=[IsOwnerOrSuperuser]
        else:
            permission_classes=[IsAdminUser]
        return [permission() for permission in permission_classes]

    def  get_serializer_class(self):
        if self.action == "create":
            return QuizeSerializerPost
        else:
            return QuizeSerializerGetter
        
class UserList(ModelViewSet):
    queryset=get_user_model().objects.all()
    permission_classes=[IsSuperuser]
    serializer_class=UserSerializer






