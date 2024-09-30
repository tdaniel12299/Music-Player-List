from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import DetailView, DeleteView, UpdateView, ListView, CreateView
from . models import Music
from .forms import MusicUploadForm

class MusicCreateView(CreateView):
    model = Music
    success_url = "/"
    template_name = 'music/music_create.html'
    fields = ['title','artist','category','song']

class MusicListView(ListView):
    model = Music
    template_name = 'music/music_list.html'
    context_object_name = 'songs'
    ordering = ['-upload_date']

def search(request):
    if request.method == "POST":
        query = request.POST.get('title', None)
        if query:
            results = Music.objects.filter(title_contains=query)
            return render(request, 'music/search.html', {'song':results})
        
    return render(request, 'music/search.html')

class MusicDeleteView(DeleteView):
    template_name = "music/music_delete.html"
    success_url = "/"
    model = Music

class MusicDetailView(DetailView):
    template_name = "music/music_details.html"
    model = Music

def music_update(request, pk):
    obj = get_object_or_404(Music, pk=pk)
    form = MusicUploadForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form':form
    }
    return render(request,'music/music_update.html', context)