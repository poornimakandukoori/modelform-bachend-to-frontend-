from django import forms
from modelform.models import *
class Topicform(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class Webpageform(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['name','url']
        #exclude=['email']
        #labels={'topic_name':'tn'}
        #widgets={'email':forms.PasswordInput}
        

class AccessRecordform(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'


