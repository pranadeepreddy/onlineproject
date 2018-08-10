
from django.urls import path

from onlineapp.serializerview.college import collegeListViewSerializer, CreateCollegeViewSerializer, \
    EditCollegeViewSerializer, DeleteCollegeViewSerializer, CollegeDetailViewSerializer
from onlineapp.serializerview.student import StudentDetailViewSerializer, EditStudentViewSerializer, \
    DeleteStudentViewSerializer, CreateStudenteViewSerializer
from onlineapp.views import *
from onlineapp import old_views, oldserializerViews
from onlineapp import views
from .serializerview import college

app_name = 'onlineapp'





urlpatterns = [
    path('colleges/',CollegeListView.as_view(), name='college_html'),
    path('colleges/<int:id>/', CollegeDetailedView.as_view(), name='college_detailed_list_html'),
    path('colleges/<int:college_id>/add/', CreateStudentView.as_view(), name='student_add'),
    path('college/add/', CreateCollegeView.as_view(), name='add_college_html'),
    path('college/edit/<int:college_id>/', EditCollegeView.as_view(), name='edit_college_html'),
    path('college/delete/<int:pk>/', DeleteCollegeView.as_view(), name='delete_college_html'),
    path('colleges/<int:college_id>/delete/<int:pk>/', DeleteStudentView.as_view(), name='student_delete'),
    path('colleges/<int:college_id>/edit/<int:pk>/', EditStudentView.as_view(), name='student_edit'),


    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),



    path('_colleges/', oldserializerViews.college_list),
    path('_colleges/<int:pk>/', oldserializerViews.college_detail),
    path('_students/',oldserializerViews.student_list),
    path('_students/<int:pk>/',oldserializerViews.student_detail),




    path('colleges_/',collegeListViewSerializer.as_view(),name="colleges_"),
    path('colleges_/add/',CreateCollegeViewSerializer.as_view(),name="addCollege_"),
    path('colleges_/<int:pk>/edit/',EditCollegeViewSerializer.as_view(),name="editCollege_"),
    path('colleges_/<int:pk>/delete/',DeleteCollegeViewSerializer.as_view(),name='deleteCollege_'),
    path('colleges_/<int:pk>/',CollegeDetailViewSerializer.as_view(),name="collegestudent_"),
    path('colleges_/<int:pk>/add/',CreateStudenteViewSerializer.as_view(),name="collegestudent_"),
    path('colleges_/<int:college_id>/student/<int:pk>/',StudentDetailViewSerializer.as_view(),name="studentdata_"),
    path('colleges_/<int:college_id>/student/<int:pk>/edit/',EditStudentViewSerializer.as_view(),name="editCollege_"),
    path('colleges_/<int:college_id>/student/<int:pk>/delete/',DeleteStudentViewSerializer.as_view(),name='deleteCollege_'),


    # path('studentdata/',CollegeDetailedView.as_view()),
    # path('studentbyid/<int:id>',views.getStudentById),
    # path('testsession/',views.testSession),
    # path('exception/', views.exception),
]
