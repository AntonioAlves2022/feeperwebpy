from rest_framework import viewsets
from core.models import Student, LearningModule, CodingSubmission, CodingChallenge, ProgressRecord
from core.serializers import (
    StudentSerializer,
    LearningModuleSerializer,
    CodingChallengeSerializer,
    CodingSubmissionSerializer,
    ProgressRecordSerializer
)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class LearningModuleViewSet(viewsets.ModelViewSet):
    queryset = LearningModule.objects.all()
    serializer_class = LearningModuleSerializer

class CodingChallengeViewSet(viewsets.ModelViewSet):
    queryset = CodingChallenge.objects.all()
    serializer_class = CodingChallengeSerializer

class CodingSubmissionViewSet(viewsets.ModelViewSet):
    queryset = CodingSubmission.objects.all()
    serializer_class = CodingSubmissionSerializer

class ProgressRecordViewSet(viewsets.ModelViewSet):
    queryset = ProgressRecord.objects.all()
    serializer_class = ProgressRecordSerializer