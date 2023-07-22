from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import NewsStory
from users.models import CustomUser
from .forms import StoryForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        NewsStory.objects.all().order_by("pub_date")
        author_id= self.request.GET.get('author', "0")
        print(author_id == "0")
        if author_id != "0":
            return NewsStory.objects.all().order_by("-pub_date").filter(author = author_id)
        else:
            return NewsStory.objects.all().order_by("-pub_date")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")
        author_id = self.request.GET.get('author', "0")
        if author_id != "0":
            context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date").filter(author = author_id)
        else:
            context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")
            
        context['latest_stories'] = context['latest_stories'][:4]
        context['authors'] = CustomUser.objects.all()
        context['author_id'] = int(author_id)
        
  
        return context
    
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(LoginRequiredMixin,generic.CreateView):
    form_class = StoryForm 
    context_object_name = 'storyform' 
    template_name = 'news/createStory.html' 
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateStoryView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model = NewsStory
    form_class = StoryForm 
    context_object_name = 'storyform' 
    template_name = 'news/createStory.html' 
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #Only the author of the post can update the post
    def test_func(self):
        story = self.get_object()
        if self.request.user == story.author:
            return True
        return False
    
class DeleteStoryView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = NewsStory
    context_object_name = 'deleteStory' 
    template_name = 'news/deleteStory.html' 
    success_url = reverse_lazy('news:index')


        #Only the author of the post can delete the post
    def test_func(self):
        story = self.get_object()
        if self.request.user == story.author:
            return True
        return False