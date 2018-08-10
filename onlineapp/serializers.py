from rest_framework import serializers
from onlineapp.models import *

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model=College
        fields=('id','name','location','acronym','contact')


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields=('id','name','db_folder','email','dob','dropped_out')


class MockTest1Serializer(serializers.ModelSerializer):
    class Meta:
        model=MockTest1
        fields=('id','problem1','problem2','problem3','problem4','total')


class StudentDetailSerializer(serializers.ModelSerializer):
    mocktest1 = MockTest1Serializer()
    class Meta:
        model = Student
        fields = ('id','name','db_folder','email','dob','dropped_out','mocktest1')



    # def create(self,validated_data):
    #     mock_data = validated_data.pop('mocktest1')
    #     student = Student.objects.create(**validated_data)
    #     import ipdb
    #     ipdb.set_trace()
    #     #MockTest1.objects.create(student__id = student_id,mock_data)
    #
    #     return student



    def update(self, instance, validated_data):
        mock_data=validated_data.pop('mocktest1')
        mock_data['total'] = mock_data['problem1'] + mock_data['problem2'] + mock_data['problem3'] + mock_data['problem4']
        mocktest=instance.mocktest1
        instance.__dict__.update(**validated_data)
        instance.save()
        mocktest.__dict__.update(mock_data)
        mocktest.save()
        return instance