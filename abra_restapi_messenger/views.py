from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from messenger_api.models import Message
from messenger_api.serializers import MessageSerializer

@api_view(['get'])
def api_home(request, *args, **kwargs):
    return Response({"Instruction": "For Instruction on api use refer to the postman file and change the localhost to heroku endpoint and login with the given user and password"}, status=200)