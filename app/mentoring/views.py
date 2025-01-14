from django.contrib.gis.geos import Point
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from .forms import ProfileForm
from .models import Profile


# Create your views here.
class IndexView(TemplateView):
    template_name = "mentoring/index.html"


class MyProfileView(generic.UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy("mentoring:my_profile")

    def get_object(self):
        profile = Profile.objects.filter(user=self.request.user).first()
        if not profile:
            profile = Profile(
                user=self.request.user,
                screen_name=self.request.user.username,
                # Snake Valley, Victoria
                # 37°36′43″S 143°35′04″E
                location=Point(-143.5844, 37.6119, srid=4326),
            )
        return profile
