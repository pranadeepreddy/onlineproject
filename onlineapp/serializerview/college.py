from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, GenericAPIView
from  onlineapp.serializers import *
from onlineapp.models import *

class collegeListViewSerializer(ListAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class CollegeDetailViewSerializer(ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.filter(college__id = self.kwargs['pk'])
        return queryset

class CreateCollegeViewSerializer(CreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer


class EditCollegeViewSerializer(ListAPIView ,UpdateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = College.objects.filter(pk = self.kwargs['pk'])
        return queryset



class DeleteCollegeViewSerializer(DestroyAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    lookup_field = 'pk'



