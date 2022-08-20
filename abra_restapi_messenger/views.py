from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from messenger_api.models import Message
from messenger_api.serializers import MessageSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # instance = form.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)