from django.shortcuts import render, redirect
from django.views import View

from rent_app.models import Person


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
        return render(request, 'add_person_view.html', {'person':person})

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
        return render(request, 'person_list.html', {'persons':persons})