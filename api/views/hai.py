from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response

from api.decorators import require_levio_backend_origin


class HiView(APIView):

    @method_decorator(require_levio_backend_origin)
    def get(self, request):
        
        return Response({"answer": "Hi from levio_yclients"})
