from django.db import migrations

def forwards_func(apps, schema_editor):
    """Populate empty usernames with email prefixes"""
    CustomUser = apps.get_model("core", "CustomUser")
    for user in CustomUser.objects.filter(username__isnull=True):
        user.username = user.email.split('@')[0]
        user.save()

class Migration(migrations.Migration):
    dependencies = [
        # Replace with your last core migration file number
        ('core', '0001_initial'),  
    ]
    
    operations = [
        migrations.RunPython(forwards_func),
    ]