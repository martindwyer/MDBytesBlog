from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Post, Comment


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses bootstrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'post-title-input'}),
            'text': forms.Textarea(attrs={'class': 'post-text-input',
                                          'placeholder': 'Enter post as HTML'})
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'comment-author-input',
                                             'placeholder': 'Enter your name'}),
            'text': forms.Textarea(
                attrs={'class': 'comment-text-input',
                       'placeholder': 'Enter your comment '
                                      'here.\n\nAdministrators review '
                                      'comments for approval at least once '
                                      'every 24 hours.'})
        }


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Your Email Address',required=True)
    subject = forms.CharField(label='Subject',required=True)
    message = forms.CharField(label='Message',widget=forms.Textarea, required=True)


