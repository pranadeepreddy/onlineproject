

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

class CollegeListView(LoginRequiredMixin, ListView):
    login_url = 'onlineapp:login'
    model = College
    context_object_name = 'collegeList'
    template_name = 'onlineapp/collegeData.html'

    def get_context_data(self, **kwargs):
        context = super(CollegeListView, self).get_context_data(**kwargs)
        context.update(
            {
                'user_permissions' : self.request.user.get_all_permissions,
            }
        )
        return context




class CreateCollegeView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = 'onlineapp:login'
    permission_required = 'onlineapp.add_college'
    model = College
    form_class = AddCollege
    success_url = reverse_lazy('onlineapp:college_html')





class EditCollegeView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = 'onlineapp:login'
    permission_required = 'onlineapp.change_college'
    model = College
    form_class = AddCollege
    success_url = reverse_lazy('onlineapp:college_html')

    def get_object(self, queryset=None):

        return get_object_or_404(College, **{'pk': self.kwargs.get('college_id')})

    def get_context_data(self, **kwargs):
        context = super(EditCollegeView, self).get_context_data(**kwargs)
        return context


class DeleteCollegeView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = 'onlineapp:login'
    permission_required = 'onlineapp.delete_college'
    model = College
    success_url = reverse_lazy('onlineapp:college_html')

