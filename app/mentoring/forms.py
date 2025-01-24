from django.contrib.gis import forms

from .models import Profile


class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = (
                "text-gray-700 dark:text-gray-200 bg-gray-200 dark:bg-gray-700 input input-bordered w-full max-w-xs"
            )


class ProfileForm(StyledModelForm):
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
