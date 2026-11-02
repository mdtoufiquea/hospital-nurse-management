from django import forms
from .models import Nurse


class NurseForm(forms.ModelForm):

    class Meta:
        model = Nurse

        fields = [
            'nurse_id',
            'name',
            'age',
            'gender',
            'department',
            'phone',
            'email',
            'experience',
            'image',
        ]

        widgets = {
            'nurse_id': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500',
                'placeholder': 'Enter Nurse ID'
            }),

            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500',
                'placeholder': 'Enter Nurse Name'
            }),

            'age': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500',
                'placeholder': 'Enter Age'
            }),

            'gender': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500',
                'placeholder': 'Enter Gender'
            }),

            'department': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500',
                'placeholder': 'Enter Department'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500',
                'placeholder': 'Enter Phone Number'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500',
                'placeholder': 'Enter Email'
            }),

            'experience': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500',
                'placeholder': 'Years of Experience'
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-xl'
            }),
        }