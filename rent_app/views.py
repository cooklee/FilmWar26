from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request):
        return render(request, "base.html")
# Create your views here.
class MovieView(View):

    def get(self, request):
        return render(request, "movie.html")