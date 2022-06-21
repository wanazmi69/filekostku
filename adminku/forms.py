from django import forms


    


class Login(forms.Form):
    nama = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class':'text-sm rounded-lg border-none ',
            }
        )
    )
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'text-sm rounded-lg border-none '
            }
        )
        
    )
    
    

class Admin(forms.Form):
    mingguan = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class':'text-xs rounded-lg border-none ',
            }
        )
    )