from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class LearingStyle(models.TextChoices):
    VISUAL = 'Visual', 'Visual'
    AUDITORY = 'Auditory', 'Auditory'
    KINESTHETIC = 'Kinesthetic', 'Kinesthetic'

class ProgramingLevel(models.TextChoices):
    BEGINNER = 'Beginner', 'Beginner'
    INTERMEDIATE = 'Intermediate', 'Intermediate'
    ADVANCED = 'Advanced', 'Advanced'

class ProgramingLanguage(models.TextChoices):
    PYTHON = 'Python', 'Python'
    JAVASCRIPT = 'Javascript', 'Javascript'
    SQL = 'Sql', 'Sql'

class Student(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    uuid = models.UUIDField(editable=False, unique=True)
    learning_style = models.CharField(max_length=20,
                                      choices=LearingStyle.choices,
                                      default=LearingStyle.VISUAL)
    programing_level = models.CharField(max_length=20,
                                        choices=ProgramingLevel.choices,
                                        default=ProgramingLevel.BEGINNER)
    motivation_level = models.IntegerField(default=1)
    skills = models.JSONField(default=dict)
    difficulties = models.JSONField(default=dict)
    learning_history = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} - {self.programing_level}"


class LearningModule(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    programing_language = models.CharField(
        max_length= 50,
        choices=ProgramingLanguage.choices,
        default=ProgramingLanguage.PYTHON
    )
    difficult_level = models.CharField(
        max_length= 30,
        choices= ProgramingLevel.choices,
        default= ProgramingLevel.BEGINNER
    )
    content = models.JSONField(default=dict)
    estimated_time = models.IntegerField(help_text='Tempo estimado em minutos')
    prerequisites = models.ManyToManyField(
        'self',
        symmetrical= False,
        blank= True
    )

    def __str__(self):
        return self.title


class CodingChallenge(models.Model):
    title = models.CharField(null=False,max_length=200)
    description = models.TextField()
    problem_statement = models.TextField()
    programing_language = models.CharField(
        max_length= 20,
        choices= ProgramingLanguage.choices
    )
    difficulty_level = models.CharField(
        max_length= 20,
        choices= ProgramingLevel.choices
    )
    expected_solution = models.TextField()
    test_cases = models.JSONField(default=dict)

    def __str__(self):
        return self.title

class CodingSubmission(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    challenge = models.ForeignKey(
        CodingChallenge,
        on_delete=models.CASCADE
    )

    submitted_code = models.TextField()
    evaluation_score = models.FloatField(
        null=True,
        blank= True
    )
    passed_tests  = models.IntegerField(
        default=0
    )
    total_tests = models.IntegerField(
        default=0
    )
    is_solved = models.BooleanField(
        default= False
    )
    submitted_at = models.DateTimeField(
        auto_now_add= True
    )

    def __str__(self):
        return (f"{self.student} -"
                f" {self.challenge} -"
                f" {self.submitted_at}")

class ProgressRecord(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete= models.CASCADE
    )
    learning_module = models.ForeignKey(
        LearningModule,
        on_delete=models.CASCADE
    )
    completed = models.BooleanField(default=False)
    progress_percentage = models.FloatField(default=0.0)
    time_spent = models.IntegerField(
        help_text="Tempo gasto em minutos",
        default=0
    )
    last_accessed = models.DateTimeField(
        default= timezone.now
    )

    def __str__(self):
        return f"{self.student} - {self.learning_module} - {self.progress_percentage}"
