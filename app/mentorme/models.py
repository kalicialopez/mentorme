from django.contrib.auth.models import User
from django.contrib.gis.db import models as gis_models
from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)


class UserSkill(models.Model):
    class Proficiency(models.IntegerChoices):
        FUNDAMENTAL = 1, "Fundamental"
        NOVICE = 2, "Novice"
        INTERMEDIATE = 3, "Intermediate"
        ADVANCED = 4, "Advanced"
        EXPERT = 5, "Expert"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency = models.IntegerField(choices=Proficiency.choices)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField()
    bio = models.TextField(max_length=1_000)
    birthday = models.DateField()
    location = gis_models.PointField(geography=True, spatial_index=True)


class MentorshipSession(models.Model):
    class Mode(models.IntegerChoices):
        IN_PERSON = 1, "In Person"
        VIRTUAL = 2, "Virtual"

    mentee = models.ForeignKey(User, on_delete=models.CASCADE)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)

    scheduled_time = models.DateTimeField()
    duration = models.DurationField()
    mode = models.SmallIntegerField(choices=Mode.choices)


class MentorshipSessionReview(models.Model):
    class Role(models.Choices):
        MENTEE = "Mentee"
        MENTOR = "Mentor"

    class Rating(models.IntegerChoices):
        POOR = 1, "Poor"
        FAIR = 2, "Fair"
        GOOD = 3, "Good"
        VERY_GOOD = 4, "Very Good"
        EXCELLENT = 5, "Excellent"

    session = models.ForeignKey(MentorshipSession, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.TextField(choices=Role.choices)
    rating = models.IntegerField(choices=Rating.choices)
    comment = models.TextField()
