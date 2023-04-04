from django.forms import ModelForm,TextInput, DateTimeInput, Textarea,CheckboxInput, RadioSelect,NumberInput
from sales.models import Reserve

class ReserveForm(ModelForm):
    class Meta:
        model=Reserve
        fields=['name','surname','phone_number','bagage','handbag','email','pets','reserve_quantity']
        widgets = {
            'name': TextInput(attrs={
                'placeholder':"Имя", 'required name':"firstName"
            }),
            'surname': TextInput(attrs={
                'placeholder':"Фамилия", 'required name':"lastName"
            }),
            'phone_number': TextInput(attrs={
                'placeholder':"Номер Телефона", 'required name':"telNum",
                'type':"tel"
            }),
            'email': TextInput(attrs={
                'type':"email", 'placeholder':"Почта", 'required name':"Mail"
            }),
            'bagage':CheckboxInput(attrs={                               #докопаться до жени, чтобы сделал нормально
            "type":"checkbox", ' name':"luggage"
            }),
            "handbag":CheckboxInput(attrs={
            'type':"checkbox", 
            ' name':"handLuggage"
            }),
            'pets':CheckboxInput(attrs={
            'type':"checkbox",'name':'luggage'
            }),
            'reserve_quantity':NumberInput(attrs={
            'type':"number", 'min':"1", 'max':"8", 'placeholder':"Количество мест", 'name':"seats"
            })
        }
    