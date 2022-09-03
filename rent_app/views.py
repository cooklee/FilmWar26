from django.shortcuts import render, redirect
from django.views import View

from rent_app.forms import CategoryForm, MovieModelForm
from rent_app.models import Person, Category


class IndexView(View):

    def get(self, request):
        return render(request, "base.html")


# Create your views here.
class MovieView(View):

    def get(self, request):
        return render(request, "movie.html")


class PersonAddView(View):

    def get(self, request):
        return render(request, 'add_person_view.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Person.objects.create(first_name=first_name, last_name=last_name)
        return redirect('add_person')


class PersonUpdateView(View):

    def get(self, request, id):
        person = Person.objects.get(pk=id)
        return render(request, 'add_person_view.html', {'person': person})

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        person.first_name = first_name
        person.last_name = last_name
        person.save()
        return redirect('add_person')


class PersonListView(View):
    def get(self, request):
        persons = Person.objects.all()
        return render(request, 'person_list.html', {'persons': persons})


class AddCategoryView(View):

    def get(self, request):
        form = CategoryForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Category.objects.create(name=name)
            return redirect('add_category')
        return render(request, 'form.html', {'form': form})


class UpdateCategoryView(View):

    def get(self, request, id):
        category = Category.objects.get(pk=id)
        form = CategoryForm(initial={'name': category.name})
        return render(request, 'form.html', {'form':form})

    def post(self, request, id):
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            c = Category.objects.get(id=id)
            c.name =name
            c.save()
            return redirect('index')
        return render(request, 'form.html', {'form': form})

class CreateMovieView(View):

    def get(self, request):
        form = MovieModelForm()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = MovieModelForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('index')
        print(form.errors)
        return render(request, 'form.html', {'form':form})