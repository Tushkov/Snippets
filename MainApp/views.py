from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
 
def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == 'GET':
        form = SnippetForm()
        context = {"pagename" : "Добавление нового сниппета",
                   "form" : form
                   }
        return render(request, 'pages/add_snippet.html', context)

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request, "pages/add_snippet.html", {"form": form})
        
def delete_snippet_page(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    snippet.delete()    
    return redirect('list')

def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        "pagename" : "Просмотр сниппетов",
        "snippets" : snippets
    }
    return render(request, 'pages/view_snippets.html', context)

def detail_snippet_page(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    context = {
        "snippet" : snippet
    }
    return render(request, 'pages/detail.snippet.html', context)

# def create_snippet_page(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         lang = request.POST['lang']
#         code = request.POST['code']
#         snippet = Snippet(name=name, lang=lang, code=code)
#         snippet.save()
#     return redirect('list')
