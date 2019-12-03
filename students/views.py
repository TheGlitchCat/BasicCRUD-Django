
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

####################
# STUDENTS
####################


@api_view(['GET', ])
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)


@api_view(['PUT', ])
def update_student(request, pk):

    student = Student.objects.get(pk=pk)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Student Updated"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def delete_student(request, pk):

    student = Student.objects.get(pk=pk)

    if request.method == 'DELETE':
        operation = student.delete()
        data = {}
        if operation:
            data["success"] = "Student Deleted"
        else:
            data["error"] = "Student Delete failed"
        return Response(data=data)


@api_view(['POST', ])
def create_student(request):

    student = Student()

    if request.method == 'POST':
        serializer = StudentSerializer(student, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Student Created"
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


####################
# PROFESSORS
####################


@api_view(['GET', ])
def professor_detail(request, pk):
    professor = Professor.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)


@api_view(['PUT', ])
def update_professor(request, pk):

    professor = Professor.objects.get(pk=pk)

    if request.method == 'PUT':
        serializer = ProfessorSerializer(professor, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Professor Updated"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def delete_professor(request, pk):

    professor = Professor.objects.get(pk=pk)

    if request.method == 'DELETE':
        operation = professor.delete()
        data = {}
        if operation:
            data["success"] = "Professor Deleted"
        else:
            data["error"] = "Professor Delete failed"
        return Response(data=data)


@api_view(['POST', ])
def create_professor(request):

    professor = Professor()

    if request.method == 'POST':
        serializer = StudentSerializer(professor, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Professor Created"
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


####################
# SCORES
####################


@api_view(['GET', ])
def score_detail(request, pk):
    score = Score.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = ScoreSerializer(score)
        return Response(serializer.data)


@api_view(['PUT', ])
def update_score(request, pk):

    score = Score.objects.get(pk=pk)

    if request.method == 'PUT':
        serializer = ScoreSerializer(score, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Score Updated"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def delete_score(request, pk):

    score = Score.objects.get(pk=pk)

    if request.method == 'DELETE':
        operation = score.delete()
        data = {}
        if operation:
            data["success"] = "Score Deleted"
        else:
            data["error"] = "Score Delete failed"
        return Response(data=data)


@api_view(['POST', ])
def create_score(request):

    score = Score()

    if request.method == 'POST':
        serializer = ScoreSerializer(score, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Score Created"
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


#########
# LISTS
#########


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('id', 'name')

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk']
        )


class ProfessorList(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('id', 'name')

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk']
        )


class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('id', 'name', 'value', 'student__id', 'student__name', 'professor__id', 'professor__name')

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk']
        )