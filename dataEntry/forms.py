
from django.forms       import ModelForm, DateField, TextInput, Textarea
from case.models        import RealEstate


class DataEntryForm(ModelForm):
    deed_date = DateField(
        widget= TextInput(     
            attrs={'type': 'date'} 
        ),
        label='تاريخ الصك', 
        required=False
    )    

    license_date = DateField(
        widget= TextInput(     
            attrs={'type': 'date'} 
        ),
        label='تاريخ الرخصة', 
        required=False
    )    

    class Meta:
        model = RealEstate
        fields= ('north_direction_value', 'north_length', 'west_direction_value', 'west_length', 'south_direction_value', 'south_length', 'east_direction_value', 'east_length', 'owner_name', 'deed_number', 'deed_date', 'notary', 'outline_number', 'outline_name', 'piece_number','area', 'license_number', 'license_date', 'dataEntry_note')
        widgets = {
            'dataEntry_note': Textarea(attrs={'rows': 5}),
        }

# 'north_direction_value', 'north_length', 'west_direction_value', 'west_length', 
# 'south_direction_value', 'south_length', 'east_direction_value', 'east_length', 
# 'owner_name', 'deed_number', 'deed_date', 'outline_number', 'outline_name', 
# , 'notary', 'piece_number','area', 'license_number', 'license_date', 'dataEntry_note'
