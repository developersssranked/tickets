from django.forms import ModelForm,TextInput, DateTimeInput, Textarea,CheckboxInput, RadioSelect,NumberInput,Select,DateInput
from sales.models import Reserve,Products
from django import forms

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
            'bagage':CheckboxInput(attrs={                               
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
            'type':"number", 'min':"1", 'max':"8", 'placeholder':"Количество мест", 'id':"seatsInput", 'name':"seats"
            })
        }
punkt_choices=[
        ('Ist','Ist' ),
        ('Варна','Варна'),
        ('Бяла','Бяла'),
        ("Обзор","Обзор"),
        ("Святой влас","Святой влас"),
        ("Равда","Равда"),
        ("Солнечный берег","Солнечный берег"),
        ("Бургас","Бургас"),
        ]
class Sotrform(ModelForm):
    
    class Meta:
        model=Products
        fields=['start_punkt','finish_punkt','date']
        start_punkt=forms.ChoiceField(choices=punkt_choices,widget=forms.Select(attrs={'name':"fromCity", 'id':"fromCity"}))
        finish_punkt=forms.ChoiceField(choices=punkt_choices,widget=forms.Select(attrs={
                'name':"toCity", 'id':"toCity"
            }))
        widgets = {
            # 'start_punkt': TextInput(attrs={
            #     'name':"fromCity", 'id':"fromCity"
            # }),
            # 'finish_punkt': TextInput(attrs={
            #     'name':"toCity", 'id':"toCity"
            # }),
            'date': DateInput(attrs={
                'type':"date",'id':"datePicker", 'class':"datepicker-input"
            }),
            
        }