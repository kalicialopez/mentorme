from django.contrib import admin

from .models import MentorshipSession, MentorshipSessionReview, Profile, Skill, SkillProficiency

# Register your models here.
admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(SkillProficiency)
admin.site.register(MentorshipSession)
admin.site.register(MentorshipSessionReview)
