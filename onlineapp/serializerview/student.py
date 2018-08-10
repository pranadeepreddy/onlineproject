from django.http import HttpResponse
from rest_framework.generics import ListAPIView,UpdateAPIView,CreateAPIView,DestroyAPIView
from  onlineapp.serializers import *
from onlineapp.models import *



class StudentDetailViewSerializer(ListAPIView):
    serializer_class = StudentDetailSerializer

    def get_queryset(self):
        queryset = Student.objects.filter(pk = self.kwargs['pk'],college_id = self.kwargs['college_id'])
        return queryset


class CreateStudenteViewSerializer(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer


    def create(self, request, *args, **kwargs):
        student = Student.objects.create(name = request.data['name'][0],dob = request.data['dob'],email = request.data['email'][0],college_id = kwargs['pk'])
        total = request.data['mocktest1.problem1'][0]+request.data['mocktest1.problem2'][0]+request.data['mocktest1.problem3'][0]+request.data['mocktest1.problem4'][0]
        MockTest1.objects.create(problem1 = request.data['mocktest1.problem1'],problem2 = request.data['mocktest1.problem2'][0],problem3 = request.data['mocktest1.problem3'][0],problem4 = request.data['mocktest1.problem4'][0],total=total,student_id = student.id)
        html="success"
        return HttpResponse(html)


class EditStudentViewSerializer(ListAPIView ,UpdateAPIView):
    serializer_class = StudentDetailSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Student.objects.filter(pk = self.kwargs['pk'],college_id = self.kwargs['college_id'])
        return queryset



class DeleteStudentViewSerializer(DestroyAPIView):
    serializer_class = StudentDetailSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Student.objects.filter(pk = self.kwargs['pk'],college_id = self.kwargs['college_id'])
        return queryset
