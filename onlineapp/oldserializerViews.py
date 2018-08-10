from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from onlineapp.models import College, Student,MockTest1
from onlineapp.serializers import CollegeSerializer, StudentSerializer


@csrf_exempt
def college_list(request):
    if request.method == 'GET':
        snippets = College.objects.all()
        serializer = CollegeSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        # print(request.data)
        serializer = CollegeSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def college_detail(request, pk):
    try:
        snippet = College.objects.get(pk=pk)
    except College.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CollegeSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        serializer = CollegeSerializer(snippet, request.PUT)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.post)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()

        return HttpResponse(status=204)


@csrf_exempt
def student_list(request):
    if request.method=='GET':
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method=='POST':
        serializer=StudentSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)


@csrf_exempt
def student_detail(request,pk):
    try:
        snippet=Student.objects.get(pk=pk)
        mock_snippet=MockTest1.objects.get(student_id= snippet.id)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method=='GET':
        serializer = StudentSerializer(snippet)
        return JsonResponse(serializer.data)

    if request.method=='DELETE':
        snippet.delete()
        return HttpResponse(status=204)