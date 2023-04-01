from django.forms import ModelForm
from sales.models import Reserve

class ReserveForm(ModelForm):
    class META:
        model=Reserve
        fields=('name','surname','email','pets')