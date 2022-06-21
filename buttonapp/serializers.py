from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Button



class ButtonSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Button
        fields = ('field1',)

