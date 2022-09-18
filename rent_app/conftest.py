import pytest
from django.contrib.auth.models import User, Group
from django.template.defaultfilters import title

from rent_app.models import Category, Person, Movie


@pytest.fixture
def categories():
    lst = []
    for x in range(10):
        lst.append(Category.objects.create(name=x))
    return lst


@pytest.fixture
def persons():
    lst = []
    for x in range(10):
        lst.append(Person(first_name=x, last_name=x))
    Person.objects.bulk_create(lst)
    return lst


@pytest.fixture
def movies(persons):
    lst = []
    for person in persons:
        lst.append(Movie.objects.create(title='cos', year=1999, director=person))
    return lst

@pytest.fixture
def user():
    return User.objects.create(username='testowy')


@pytest.fixture
def group():
    return Group.objects.create(name='troskliwe misie')


@pytest.fixture
def user_in_group(user, group):
    user.groups.add(group)
    return user

