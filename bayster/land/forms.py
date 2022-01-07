from django import forms

from .models import LandReview

class LandReviewForm(forms.ModelForm):
    STATUS_CHOICE = ((1, '承認'),(2, '却下'))
    status = forms.ChoiceField(choices=STATUS_CHOICE)    
    
    def save(self, commit=True):
        instance = super().save(commit)

        instance.land.status = self.cleaned_data['status']
        instance.land.save()

        return instance

    class Meta:
        model = LandReview
        fields = '__all__'