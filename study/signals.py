from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Progress
from core.models import CustomUser

@receiver(post_save, sender=Progress)
def create_progress_notification(sender, instance, created, **kwargs):
    if created or instance.completed == 100:
        title = "New Progress Record" if created else "Progress Completed!"
        message = f"Your progress in {instance.subject} has been recorded."
        if instance.completed == 100:
            message = f"Congratulations! You've completed {instance.subject}!"
        
        Notification.objects.create(
            user=instance.user,
            title=title,
            message=message,
            notification_type='PROGRESS'
        )