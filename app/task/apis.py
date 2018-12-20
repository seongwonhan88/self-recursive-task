from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TaskSerializer
from .models import Task


class TaskAPIView(APIView):

    def get(self, request):
        task = Task.objects.filter(parent_tasks__isnull=True)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

