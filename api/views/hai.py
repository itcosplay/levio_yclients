from rest_framework.views import APIView
from rest_framework.response import Response


class HiView(APIView):
    def get(self, request):
        return Response({"answer": "Hi from levio YC"})
