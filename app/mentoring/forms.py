from django.contrib.gis import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [
            "user",
            "active",
            "skills",
        ]

        widgets = {
            # TODO: I can't get this to work, not sure how the map selector is meant to function. - Ben
            "location": forms.OSMWidget(
                attrs={
                    "display_raw": False,
                    "map_width": 500,
                    "map_height": 500,
                    # "display_wkt": True,
                    # "default_lat": 57,
                    # "default_lon": 12,
                }
            ),
        }
