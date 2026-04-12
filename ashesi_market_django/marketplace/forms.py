"""
Django forms for web interface
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Product


class UserRegistrationForm(UserCreationForm):
    """User registration form"""
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    phone_whatsapp = forms.CharField(max_length=20, required=False)
    year_group = forms.ChoiceField(
        choices=[
            ('', 'Select year'),
            ('Year 1', 'Year 1'),
            ('Year 2', 'Year 2'),
            ('Year 3', 'Year 3'),
            ('Year 4', 'Year 4'),
            ('Graduate', 'Graduate'),
            ('Staff', 'Staff'),
        ],
        required=False
    )
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        initial='both'
    )
    id_image = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2',
                  'phone_whatsapp', 'year_group', 'role', 'id_image']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    """Login form"""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProductForm(forms.ModelForm):
    """Product creation/edit form"""
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'quantity', 'condition', 
                  'location', 'category', 'is_available']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class ProfileForm(forms.ModelForm):
    """User profile edit form"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_whatsapp', 'year_group', 
                  'bio', 'id_image', 'role']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }
