from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['get'])
def api_home(request, *args, **kwargs):
    return Response({"Instruction": "For Instruction on api use refer to the postman file and change the localhost to heroku endpoint and login with the given user and password"}, status=200)