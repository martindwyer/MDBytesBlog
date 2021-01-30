from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from app.models import Post
from app.forms import PostForm


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'app/post_detail.html'
    form_class = PostForm
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Post'
        context['message'] = 'A new blog post'
        return context
