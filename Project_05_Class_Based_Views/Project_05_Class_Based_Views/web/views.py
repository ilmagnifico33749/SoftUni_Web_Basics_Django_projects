from django.forms import forms, TextInput, modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy

from Project_05_Class_Based_Views.web.models import Article
from django.views import generic as views


# Create your views here.


# def list_articles(request):
#     context = {
#         'articles': Article.objects.all()
#     }
#     return render(
#         request=request,
#         template_name='articles/list.html',
#         context=context
#     )

# views.CreateView
# views.ListView
# views.UpdateView
# views.DeleteView
# views.DetailView
# views.TemplateView

# class ArticlesListView(views.View):
#
#     def post(self):
#         # ...
#         pass
#
#     def get(self):
#         context = {
#             'articles': Article.objects.all()
#         }
#         return render(
#             request=self.request,
#             template_name='articles/list.html',
#             context=context
#         )


# class ArticlesListView(views.TemplateView):
#     template_name = 'articles/list.html'
#     extra_context = {
#         'articles': Article.objects.all()
#     }

class ArticlesListView(views.ListView):
    template_name = 'articles/list.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context


class ArticleDetailView(views.DetailView):
    model = Article
    template_name = 'articles/details.html'


class ArticleCreateView(views.CreateView):
    model = Article
    template_name = 'articles/create.html'
    success_url = reverse_lazy('list_articles')
    fields = ('__all__')
    # # fields = ('title', 'content')
    disabled_fields = ('title',)
    # widgets = {
    #     'title': forms.TextInput(
    #         attrs={
    #             'class': 'abc',
    #         }
    #     )
    # }
    # -----------------------------------------------------------------
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        for field in self.disabled_fields:
            form.fields[field].widget.attrs['disabled'] = 'disabled'

        return form


    # the above can actually evolve to the below class which to be inherited in class ArticleCreateView(views.CreateView)
    # however it should be written in the following way: ArticleCreateView(DisabledFormFieldsMixin, views.CreateView)
    # in that scenario the disabled fields will be simply set via the 'disabled_fields' parameter in the ArticleCreateView

# class DisabledFormFieldsMixin:
#     disabled_fields = ()
#
#     def get_form(self, *args, **kwargs):
#         form = super().get_form(*args, **kwargs)
#
#         for field in self.disabled_fields:
#             form.fields[field].widget.attrs['disabled'] = 'disabled'
#             form.fields[field].widget.attrs['readonly'] = 'readonly'
#
#         return form
    # -----------------------------------------------------------------


class ArticleUpdateView(views.UpdateView):
    pass


class ArticleDeleteView(views.DeleteView):
    model = Article
    template_name = 'articles/delete.html'
    success_url = reverse_lazy('list_articles')
    # the below is optional
    form_class = modelform_factory(
        Article,
        fields=('title', 'content'),
    )

    # the below fills the form with the data of the Model to be deleted
    def get_form_kwarg(self):
        instance = self.get_object()
        form_kwargs = super().get_form_kwargs()

        form_kwargs.update(instance=instance)
        return form_kwargs




