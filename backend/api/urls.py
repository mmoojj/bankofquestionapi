from django.urls import path 
from .views import  QuizeListView , QuizeCreateView , UserList
from rest_framework import routers



app_name='bankofquestion'
urlpatterns = [
    path('quize/get/', QuizeListView.as_view(),name='quize'),
    # path('user/' , UserList.as_view(),name='user')
    # path('api/quize/post/', QuizeCreateView.as_view(),name='quize'),
    # path('api/quize/<int:pk>/post/', QuizeCreateView.as_view(),name='quize'),
]

router = routers.SimpleRouter()
router.register(r'quize', QuizeCreateView,basename="quize")
router.register(r'user',UserList,basename="user")
urlpatterns += router.urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)