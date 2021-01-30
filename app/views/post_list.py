
from django.utils import timezone
from django.views.generic import ListView

from app.models import Post


class PostListView(ListView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Post List'
        context['message'] = 'Published posts ordered by publication date'
        return context

    def get_queryset(self):
        return Post.objects.filter(
            published_date__lte=timezone.now()).order_by('-published_date')

