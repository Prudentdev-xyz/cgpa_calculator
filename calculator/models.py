from django.db import models
from django.contrib.auth.models import User

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gp = models.DecimalField(max_digits=4, decimal_places=2)
    total_units = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - GP: {self.gp}"

class Course(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=100)
    units = models.IntegerField()
    grade = models.CharField(max_length=2)
    grade_point = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f"{self.name} - {self.grade}"