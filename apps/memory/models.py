from apps import user
from django.db import models

from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField


# class Memory(models.Model):
#     location = PointField(null=True)
#     name = models.CharField(max_length=128)
#     comment = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Owner: {self.owner} \nName: {self.name}"