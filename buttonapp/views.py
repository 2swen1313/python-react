from rest_framework.viewsets import ModelViewSet
from .serializers import ButtonSerializer
from .models import Button




class ButtonViewSet(ModelViewSet):
    serializer_class = ButtonSerializer
    queryset = Button.objects.all()









# Create your views here.
