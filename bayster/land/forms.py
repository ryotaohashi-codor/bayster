from django import forms
from django.core.mail import send_mail

from .models import LandReview
from user.models import User

class LandReviewForm(forms.ModelForm):
    STATUS_CHOICE = ((1, '承認'),(2, '却下'))
    status = forms.ChoiceField(choices=STATUS_CHOICE)    
    
    def save(self, commit=True):
        instance = super().save(commit)

        instance.land.status = self.cleaned_data['status']
        instance.land.save()

        print(dir(instance.land))

        subject = "案件申請結果"
        message = "案件申請結果を確認して下さい"
        user = User.objects.get(id=instance.land.id)
        from_email = 'system@mail.com'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)


        return instance

    class Meta:
        model = LandReview
        fields = '__all__'