from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from app.models import Post


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = '/app/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by(
            'created_date')
