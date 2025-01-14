from django.contrib.auth import get_user_model
from django.contrib.gis.db import models

###
# Choices
###


class Proficiency(models.IntegerChoices):
    FUNDAMENTAL = 1, "Fundamental"
    NOVICE = 2, "Novice"
    INTERMEDIATE = 3, "Intermediate"
    ADVANCED = 4, "Advanced"
    EXPERT = 5, "Expert"


class Role(models.Choices):
    MENTEE = "Mentee"
    MENTOR = "Mentor"


class Rating(models.IntegerChoices):
    POOR = 1, "Poor"
    FAIR = 2, "Fair"
    GOOD = 3, "Good"
    VERY_GOOD = 4, "Very Good"
    EXCELLENT = 5, "Excellent"


###
# Models
###


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    """The Profile of the User, detached from the User model as User can de deleted however Profile will not."""

    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="profile",
        null=True,
    )
    active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    screen_name = models.CharField(max_length=100, unique=True)
    picture = models.ImageField(
        null=True, blank=True, upload_to="profile_pictures"
    )  # TODO: this requires user uploading, may not be the best idea
    bio = models.TextField(max_length=1_000, blank=True)
    birthday = models.DateField(null=True, blank=True)
    location = models.PointField(
        geography=True,
        # spatial_index=True,
    )
    skills = models.ManyToManyField(
        Skill,
        through="SkillProficiency",
        through_fields=("profile", "skill"),
        related_name="proficient_profiles",
    )

    def __str__(self):
        return self.screen_name if self.active else f"{self.screen_name} - Deactivated"


class SkillProficiency(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="skill_proficiencies",
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name="skill_proficiencies",
    )
    proficiency = models.IntegerField(choices=Proficiency)

    def __str__(self):
        return f"{self.profile} - {self.skill}: {self.proficiency}"


class MentorshipSession(models.Model):
    class Mode(models.IntegerChoices):
        IN_PERSON = 1, "In Person"
        VIRTUAL = 2, "Virtual"

    mentee = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="mentee_sessions",
    )
    mentor = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="mentor_sessions",
    )
    scheduled_time = models.DateTimeField()
    duration = models.DurationField()
    mode = models.SmallIntegerField(choices=Mode)


class MentorshipSessionReview(models.Model):
    session = models.ForeignKey(
        MentorshipSession,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    reviewer = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="session_reviews",
    )
    role = models.TextField(choices=Role)
    rating = models.IntegerField(choices=Rating)
    comment = models.TextField()
