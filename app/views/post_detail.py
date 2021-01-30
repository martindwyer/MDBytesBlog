from django.views.generic import DetailView

from app.models import Post


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'by Martin Dwyer'
        return context

