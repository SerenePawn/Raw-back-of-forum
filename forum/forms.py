from django import forms
from forum.models import TopicComments, PrivateMessage
from django.contrib.auth.models import User


class CommentsForm(forms.ModelForm):
    class Meta:
        model = TopicComments
        fields = ['comments_text']


class MessageSendForm(forms.ModelForm):
    class Meta:
        model = PrivateMessage
        fields = ('text',)


class NewDialogForm(MessageSendForm):
    recipient = forms.CharField(label='Recipient', help_text='Specify the username')
    subject = forms.CharField(label='Subject')

    def clean_recipient(self):
        try:
            recipient = User.objects.get(username=self.cleaned_data['recipient'])
        except User.DoesNotExist:
            raise forms.ValidationError('Username not found')

        return recipient
