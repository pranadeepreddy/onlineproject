from django.views import View

from onlineapp.models import *
from django.http import *
from django.shortcuts import *

from onlineapp.models import *
from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import *
from onlineapp.forms import *
from django.urls import *

from django.contrib.auth.mixins import LoginRequiredMixin



class CollegeDetailedView(LoginRequiredMixin, DetailView):
    login_url = 'onlineapp:login'
    model = College
    template_name = 'onlineapp/studentData.html'


    def get_object(self, queryset=None):
        return get_object_or_404(College, **self.kwargs)

    def get_context_data(self, **kwargs):

        context = super(CollegeDetailedView, self).get_context_data(**kwargs)
        college = context.get('college')

        students = list(college.student_set.order_by("-mocktest1__total"))
        context.update({
            'studentList': students,
            'user_permissions': self.request.user.get_all_permissions,
        })

        return context



class CreateStudentView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = 'onlineapp:login'
    permission_required = 'onlineapp.add_student'
    model = Student
    form_class = AddStudent

    def get_context_data(self, **kwargs):
        context = super(CreateStudentView, self).get_context_data(**kwargs)
        test_form = AddMockTest()
        context.update({
            'student_form': context.get('form'),
            'test_form': test_form,
        })

        return context

    def post(self, request, *args, **kwargs):
        college = get_object_or_404(College, pk=kwargs.get('college_id'))
        student_form = AddStudent(request.POST)
        test_form = AddMockTest(request.POST)

        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.college = college
            student.save()

            if test_form.is_valid():
                score = test_form.save(commit=False)
                score.total = sum(test_form.cleaned_data.values())
                score.student = student
                score.save()
            return redirect('onlineapp:college_detailed_list_html',college.id)






class DeleteStudentView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'onlineapp:login'
    permission_required = 'onlineapp.delete_student'
    def post(self, request, *args, **kwargs):
        students = get_object_or_404(Student, pk=self.kwargs.get('pk'))
        students.delete()
        return redirect('onlineapp:college_detailed_list_html',self.kwargs.get('college_id'))


# class DeleteStudentView(DeleteView):
#     model = Student
#     success_url = reverse_lazy('onlineapp:college_html', pk = self.kwargs.get('pk'))



class EditStudentView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = 'onlineapp:login'
    permission_required = 'onlineapp.change_student'
    model = Student
    form_class = AddStudent
    template_name = 'OnlineApp/student_form.html'

    def get_context_data(self, **kwargs):
        context = super(EditStudentView, self).get_context_data(**kwargs)
        student_form = context.get('student')
        test_form = AddMockTest(instance=student_form.mocktest1)
        context.update({
            'student_form': context.get('form'),
            'test_form': test_form,
        })
        return context

    def post(self, request, *args, **kwargs):
        student = Student.objects.get(pk=kwargs.get('pk'))
        form = AddStudent(request.POST, instance=student)
        form.save()
        test_form = AddMockTest(request.POST, instance=student.mocktest1)
        test = test_form.save(False)
        test.total = sum(test_form.cleaned_data.values())

        test_form.save()
        return redirect("onlineapp:college_detailed_list_html", self.kwargs.get('college_id'))

