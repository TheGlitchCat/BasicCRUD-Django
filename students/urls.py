from django.conf.urls import url
from students.views import *
from django.urls import path

# urlpatterns = [
#     url(r'^students/$', StudentList.as_view(), name='Students')
# ]

urlpatterns = [
    path('students/', StudentList.as_view(), name='Students'),
    path('student/<int:pk>/', student_detail, name='show student'),
    path('student/update/<int:pk>/', update_student, name='update student'),
    path('student/create/', create_student, name='create student'),
    path('student/delete/<int:pk>/', delete_student, name='delete student'),
    path('professors/', ProfessorList.as_view(), name='Professors'),
    path('professor/<int:pk>/', professor_detail, name='show professor'),
    path('professor/update/<int:pk>/', update_professor, name='update professor'),
    path('professor/create/', create_professor, name='create professor'),
    path('professor/delete/<int:pk>/', delete_professor, name='delete professor'),
    path('scores/', ScoreList.as_view(), name='Scores'),
    path('score/<int:pk>/', score_detail, name='show score'),
    path('score/update/<int:pk>/', update_score, name='update score'),
    path('score/create/', create_score, name='create score'),
    path('score/delete/<int:pk>/', delete_score, name='delete score'),

]

