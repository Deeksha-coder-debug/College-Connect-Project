from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class StudyMaterial(models.Model):
    CATEGORY_CHOICES = [
            ('Math', 'Math'),
            ('Science', 'Science'),
            ('History', 'History'),
            ('Language', 'Language'),
            ('Other', 'Other'),
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='materials/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')

    def __str__(self):
        return self.title
