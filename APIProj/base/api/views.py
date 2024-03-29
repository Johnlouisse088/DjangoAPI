from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Task
from .serializers import TaskSerializer

@api_view(["GET"])
def getRoutes(request):
    routes= [
        "GET /api",
        "GET /api/rooms",
        "GET /api/rooms/:id",
    ]
    return Response(routes)

@api_view(["GET"])
def view_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def view_task(request, id):
    tasks = Task.objects.get(id=id)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def create_task(request):
    serializer =TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print("wrong")
    return Response(serializer.data)

@api_view(["PUT"])
def update_task(request, id):
    task = Task.objects.get(id=id)
    serializer =TaskSerializer(data=request.data, instance=task)
    if serializer.is_valid():
        serializer.save()
    else:
        print("wrong")
    return Response(serializer.data)
@api_view(["DELETE"])
def remove_task(request, id):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    tasks = Task.objects.get(id=id)
    tasks.delete()
    return Response(serializer.data)


