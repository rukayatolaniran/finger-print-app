from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    institution = models.CharField(max_length=100)
    faculty = models.CharField(max_length=190)
    department = models.CharField(max_length=100)
    fingerprint = ProcessedImageField(
        upload_to='fingerprints/',
        processors=[ResizeToFit(300, 300)],
        format='JPEG',
        options={'quality': 90}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
