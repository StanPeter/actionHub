from django.shortcuts import render, redirect
from django.contrib import messages
import os
from airtable import Airtable
from dotenv import load_dotenv
from .mock_data import init_data

# load env variables
load_dotenv()

# connecting to the database
AIRTABLE_BASE_ID = os.environ['AIRTABLE_BASE_ID']
TABLE_NAME = os.environ['TABLE_NAME']
AIRTABLE_API_KEY = os.environ['AIRTABLE_API_KEY']

AT = Airtable(AIRTABLE_BASE_ID, TABLE_NAME, api_key=AIRTABLE_API_KEY)

# uncomment to replace all existing data by mock data
# init_data(AT)

# view for index route
def index(request):
    # getting user's input from the search form
    user_query = str(request.GET.get('query', ''))
    # get all matched movies from the database
    matched_movies = AT.get_all(
        formula="FIND('" + user_query.lower() + "',LOWER({Name}))")
    # send data to the front end
    movies = {'movies': matched_movies}
    return render(request, 'movieApp/index.html', movies)


# view for new/create route
def create(request):
    if request.method == 'POST':
        new_movie = {
            'Name': request.POST.get('Name'),
            'Notes': request.POST.get('Notes'),
            'Pictures': [{'url': request.POST.get('Pictures') or 'https://logox.com/logox/uploads/noimage300X300.jpg'}],
            'Rating': int(request.POST.get('Rating'))
        }
        try:
            AT.insert(new_movie)
            messages.success(request, 'Added succefully movie {}'.format(
                request.POST.get('Name')))
        except Exception:
            messages.warning(request, 'Creation of movie {} wasn\'t completed due to {}'.format(
                request.POST.get('Name')), Exception)
    return redirect('/')


# view for edit route
def edit(request, id):
    if request.method == 'POST':
        edited_movie = {
            'Name': request.POST.get('Name'),
            'Pictures': [{'url': request.POST.get('Pictures')}],
            'Rating': int(request.POST.get('Rating')),
            'Notes': request.POST.get('Notes')
        }

        try:
            AT.update(id, edited_movie)
            messages.success(request, 'Edited succefully movie {}'.format(
                request.POST.get('Name')))
        except Exception:
            messages.warning(request, 'Editation of {} movie wasn\'t succesful due to {}'.format(
                request.POST.get('Name')), Exception)
    return redirect('/')


# view for destroy route
def delete(request, id):
    movie_name = AT.get(id)['fields']['Name']
    AT.delete(id)

    messages.warning(request, 'Deleted succefully movie {}'.format(movie_name))
    return redirect('/')
