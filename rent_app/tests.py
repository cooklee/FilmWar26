import pytest
# Create your tests here.
from django.urls import reverse

from rent_app.forms import MovieModelForm
from rent_app.models import Person, Studio, Movie


def test_index_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_category_list_view(client, categories):
    url = reverse('list_category')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(categories)
    for cat in categories:
        assert cat in response.context['object_list']


@pytest.mark.django_db
def test_person_list_view(client, persons):
    url = reverse('list_person')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['persons'].count() == len(persons)
    for person in persons:
        assert person in response.context['persons']


@pytest.mark.django_db
def test_movie_list_view(client, movies):
    url = reverse('movie_list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(movies)
    for movie in movies:
        assert movie in response.context['object_list']

def test_add_person_get_not_login(client):
    url = reverse('add_person')
    response = client.get(url)
    assert response.status_code == 302
    url_redirect =reverse('login')
    assert response.url.startswith(url_redirect)

@pytest.mark.django_db
def test_add_person_get_login(client, user):
    url = reverse('add_person')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_person_get_login(client, user):
    url = reverse('add_person')
    client.force_login(user)
    data = {
        'first_name':'gamon',
        'last_name':'popasmerf',
        'year':1987
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == url
    Person.objects.get(**data)


def test_add_studio_get_not_login(client):
    url = reverse('add_studio')
    response = client.get(url)
    assert response.status_code == 302
    url_redirect =reverse('login')
    assert response.url.startswith(url_redirect)

@pytest.mark.django_db
def test_add_studio_get_login(client, user):
    url = reverse('add_studio')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_add_studio_get_login_with_permission(client, user_in_group):
    url = reverse('add_studio')
    client.force_login(user_in_group)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_studio_post_login(client, user_in_group, persons):
    url = reverse('add_studio')
    p = persons[0]
    client.force_login(user_in_group)
    data = {
        'name':'gamon',
        'city':'popasmerf',
        'year':1987,
        'ceo':1
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == url
    Studio.objects.get(**data)


@pytest.mark.django_db
def test_update_movie_get(client, movies):
    movie = movies[0]
    url = reverse("update_movie", args=(movie.id,))
    response = client.get(url)
    form_obj = response.context['form']
    assert response.status_code == 200
    assert isinstance(form_obj, MovieModelForm)


@pytest.mark.django_db
def test_update_movie_get(client, movies):
    movie = movies[0]
    url = reverse("update_movie", args=(movie.id,))
    data = {
        'title':'cokolwiek',
        'year':2000,
        "category":[1,2],
        'director':movie.director.id
    }
    response = client.post(url, data)
    assert response.status_code == 302
    Movie.objects.get(title=data['title'])
