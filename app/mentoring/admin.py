from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin

from .models import MentorshipSession, MentorshipSessionReview, Profile, Skill, SkillProficiency

# Register your models here.
admin.site.register(Skill)
admin.site.register(Profile, GISModelAdmin)
admin.site.register(SkillProficiency)
admin.site.register(MentorshipSession)
admin.site.register(MentorshipSessionReview)
