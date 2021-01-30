from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail, BadHeaderError

from app.models import Post, Comment
from app.forms import CommentForm, ContactForm


def index(request):
    return render(request, 'app/index.html')


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Insights on our contributors',
            'year': datetime.now().year,
        }
    )


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'app/comment_form.html', {'form': form})


@login_required
def comments_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Message From MDBytes > Blog"
            from_email = form.cleaned_data['from_email']
            message = "Subject: " + form.cleaned_data[
                'subject'] + "\n\nMessage:\n" + form.cleaned_data[
                          'message'] + "\n\nReply to: " + from_email
            try:
                send_mail(subject, message, 'martin@mdbytes.com',
                          ['martin.b.dwyer@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    return render(request, "app/contact.html", {
        'title': 'Contact',
        'message': 'Send us a message today',
        'year': datetime.now().year,
        'form': form
    }
                  )


def success_view(request):
    return HttpResponse('Success! Thank you for your message.')
