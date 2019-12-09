
from django.forms       import ModelForm, Textarea, ModelChoiceField, Select
from case.models        import RealEstate
from location.models    import City, Neighborhood
from account.models     import User
from django.contrib.auth.models import Group


class CaseForm(ModelForm):
    inspector = ModelChoiceField(label='المعاين', queryset = Group.objects.none())

    class Meta:
        model = RealEstate
        fields= ('contact_name', 'contact_number', 'region_id', 'city_id', 'neighborhood_id', 'location', 'coordinator_note','inspector')
        widgets = {
            'coordinator_note': Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city_id'].queryset = City.objects.none()
        self.fields['neighborhood_id'].queryset = Neighborhood.objects.none()
        # self.fields['inspector'].choices = list(Group.objects.filter(name = 'المعاينين').first().user_set.all())

        if 'region_id' in self.data:
            try:
                region_id = int(self.data.get('region_id'))
                self.fields['city_id'].queryset = City.objects.filter(region = region_id).order_by('city')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        if 'city_id' in self.data:
            try:
                city_id = int(self.data.get('city_id'))
                self.fields['neighborhood_id'].queryset = Neighborhood.objects.filter(city_id = city_id).order_by('neighborhood_name')
                self.fields['inspector'].queryset = Group.objects.filter(name = 'المعاينين').first().user_set.filter(city = city_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
    
        elif self.instance.pk:
            # self.fields['city_id'].queryset = self.instance.region_id.city_set.order_by('city')
            self.fields['city_id'].queryset = City.objects.filter(region = self.instance.region_id).order_by('city')
            self.fields['neighborhood_id'].queryset = Neighborhood.objects.filter(city_id = self.instance.city_id).order_by('neighborhood_name')
            self.fields['inspector'].queryset = Group.objects.filter(name = 'المعاينين').first().user_set.filter(city = self.instance.city_id)


