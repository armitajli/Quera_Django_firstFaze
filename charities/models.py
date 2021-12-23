from django.db import models
from django.db.models import Q

from accounts.models import User

from django.db import models

from accounts.models import User


class Benefactor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience_levels = (
        (0, "beginner"),
        (1, "intermediate"),
        (2, "advance")
    )
    experience = models.SmallIntegerField(choices=experience_levels, default=0)
    free_time_per_week = models.PositiveSmallIntegerField(default=0)


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return self.filter(charity=user.charity)

    def related_tasks_to_benefactor(self, user):
        return self.filter(assigned_benefactor=user.benefactor)

    def all_related_tasks_to_user(self, user):
        return self.filter(Q(assigned_benefactor__user=user) | Q(charity__user=user) | Q(state="P"))


class Task(models.Model):
    objects = TaskManager()
    title = models.CharField(max_length=60)
    state_forms = (
        ("P", "Pending"),
        ("W", "Waiting"),
        ("A", "Assigned"),
        ("D", "Done")
    )
    state = models.CharField(max_length=10, choices=state_forms, default="P")
    gender_options = (
        ("F", "Female"),
        ("M", "Male")
    )
    gender_limit = models.CharField(choices=gender_options, max_length=1, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    age_limit_from = models.IntegerField(blank=True, null=True)
    age_limit_to = models.IntegerField(blank=True, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    assigned_benefactor = models.ForeignKey(Benefactor, null=True, on_delete=models.SET_NULL)
