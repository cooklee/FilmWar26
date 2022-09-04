"""WyporzyczalniFilmowWarPytW26 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from rent_app import views

urlpatterns = [
    path("movies/", views.MovieListView.as_view(), name='movie_list'),
    path("add_person/", views.PersonAddView.as_view(), name='add_person'),
    path("person_list/", views.PersonListView.as_view(), name='list_person'),
    path("category/", views.CategoryListView.as_view(), name='list_category'),
    path("update_person/<int:id>/", views.PersonUpdateView.as_view(), name='person_update'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('update_category/<int:id>/', views.UpdateCategoryView.as_view(), name='update_category'),
    path('add_movie/', views.CreateMovieView.as_view(), name='add_movie'),
    path('add_studio/', views.CreateStudioView.as_view(), name='add_studio'),
    path('update_movie/<int:pk>/', views.UpdateMovieView.as_view(), name='update_movie'),
]
