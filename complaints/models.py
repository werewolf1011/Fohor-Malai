from django.db import models


# Create your models here.
class Complaints(models.Model):
    COMPLAIN_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    complainer_name = models.CharField(max_length=50)
    complainer_address = models.CharField(max_length=128)
    complainer_phone = models.CharField(max_length=10)
    waste_type = models.CharField(max_length=20)
    image = models.FileField(upload_to="complaints/",max_length=250,null=True, default=None)
    complaint_desc = models.TextField()
    complain_status = models.CharField(max_length=20, choices=COMPLAIN_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add =True)
    modified_at = models.DateTimeField(auto_now = True)
