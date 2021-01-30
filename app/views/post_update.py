from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from app.models import Post
from app.forms import PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'app/post_detail.html'
    form_class = PostForm
    model = Post

