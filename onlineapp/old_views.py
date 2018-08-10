from django.shortcuts import render

# Create your views here.




from onlineapp.models import *
from django.http import *

def collegeData(request):
    collegeListQuery = College.objects.values_list('name','acronym').order_by('name')
    context = {'collegeList' : collegeListQuery,}
    return render(request, 'collegeData.html', context)

def studentData(request):
    studentListQuery = Student.objects.values_list('name','email','college__acronym','mocktest1__total')
    context = {'studentList' : studentListQuery,}
    return render(request, 'studentData.html', context)

def getStudentById(request,id):
    studentListQuery = Student.objects.filter(pk = id).values('name','email','college__acronym')
    if(len(studentListQuery) == 0):
        return HttpResponse("student doesn't exist...")
    context = {'studentList' : studentListQuery,}
    return render(request, 'getStudentById.html', context)

def collegeStats(request):
    studentListQuery = Student.objects.filter(college__acronym__iexact = request.GET.get('acronym')).values_list('name', 'email', 'college__acronym', 'mocktest1__total').order_by('-mocktest1__total')
    context = {'studentList': studentListQuery, }


def testSession(request):
    if('counter' in request.session):
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    return HttpResponse(str(request.session['counter']))

def exception(request):
    raise Http404('my exception')
