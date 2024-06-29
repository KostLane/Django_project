from django import forms


class AddReview(forms.Form):
    name = forms.CharField(label='Имя', required=True, max_length=150,
                           widget=forms.TextInput(attrs={'placeholder': 'Представьтесь', 'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea({'placeholder': 'Содержание', 'class': 'form-control'}),
                           label='Содержание', required=True)
    star = forms.ChoiceField(choices=[(j, j) for j in range(1, 6)],
                             widget=forms.RadioSelect(attrs={'class': 'form-check-input'}), required=True)