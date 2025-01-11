from django.contrib.auth.models import User
from django.contrib.gis.db import models as gis_models
from django.db import models


class SkillProficiencyLevel(models.IntegerChoices):
    FUNDAMENTAL = 1, "Fundamental"
    NOVICE = 2, "Novice"
    INTERMEDIATE = 3, "Intermediate"
    ADVANCED = 4, "Advanced"
    EXPERT = 5, "Expert"


class SessionMode(models.IntegerChoices):
    IN_PERSON = 1, "In Person"
    VIRTUAL = 2, "Virtual"


class Skill(models.Model):
    name = models.CharField(max_length=100)


class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency = models.IntegerField(choices=SkillProficiencyLevel.choices)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField()
    bio = models.TextField(max_length=1_000)
    birthday = models.DateField()
    location = gis_models.PointField(geography=True, spatial_index=True)


class MentorshipSession(models.Model):
    mentee = models.ForeignKey(User, on_delete=models.CASCADE)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)

    scheduled_time = models.DateTimeField()
    duration = models.DurationField()
    mode = models.SmallIntegerField(choices=SessionMode.choices)


class MentorshipSessionReview(models.Model):
    class Role(models.Choices):
        MENTEE = "Mentee"
        MENTOR = "Mentor"

    session = models.ForeignKey(MentorshipSession, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.TextField(choices=Role.choices)
    rating = models.IntegerField()
    comment = models.TextField()
