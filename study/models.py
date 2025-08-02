from django.db import models
from core.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

class Progress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='progress_records')
    subject = models.CharField(max_length=100)
    completed = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Percentage completed (0-100)"
    )
    notes = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    deadline = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Progress"
        ordering = ['-last_updated']

    def __str__(self):
        return f"{self.user.username}'s progress in {self.subject}"

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    notification_type = models.CharField(max_length=50, choices=[
        ('PROGRESS', 'Progress Update'),
        ('REMINDER', 'Study Reminder'),
        ('MESSAGE', 'New Message'),
    ])

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.user.username}"