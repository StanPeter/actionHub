from django.shortcuts import render, redirect
from django.contrib import messages
import os
from airtable import Airtable
from .appi_key import AIRTABLE_API_KEY, AIRTABLE_BASE_ID, TABLE_NAME


os.environ['AIRTABLE_API_KEY']= AIRTABLE_API_KEY
AT = Airtable(AIRTABLE_BASE_ID, TABLE_NAME)


# Create your views here.

def home_page(request):
    user_query = str(request.GET.get('query', ''))
    # pulls information from our query (index.html)  
    search_result = AT.get_all(formula="FIND('" + user_query.lower() + "',LOWER({Name}))")
    stuff_for_frontend = {'search_result':search_result}
    return render(request, 'movieApp/index.html', stuff_for_frontend)
    
def movie_create(request):
    if request.method == 'POST':
        data = {
        'Name': request.POST.get('Name'),
        'Notes': request.POST.get('Notes'),
        'Pictures': [{'url': request.POST.get('Pictures') or 'https://www.harpersphoto.co.uk/user/products/large/no%20image.gif'}],
        'Rating': int(request.POST.get('Rating'))
            }
        try:
            AT.insert(data)
            messages.success(request, 'Added succefully movie {}'.format(request.POST.get('Name')))
        except Exception:
            messages.warning(request, 'Creation of movie {} wasn\'t completed due to {}'.format(request.POST.get('Name')), Exception)
    return redirect('/')

def movie_edit(request, id):
    if request.method == 'POST':
        data = {
        'Name':request.POST.get('Name'), 
        'Pictures':[{'url':request.POST.get('Pictures')}],
        'Rating':int(request.POST.get('Rating')),
        'Notes':request.POST.get('Notes')
        }

        try:
            AT.update(id, data)
            messages.success(request, 'Edited succefully movie {}'.format(request.POST.get('Name')))
        except Exception:
            messages.warning(request, 'Editation of {} movie wasn\'t succesful due to {}'.format(request.POST.get('Name')), Exception)
    return redirect('/')

def movie_delete(request, id):
    movie_name = AT.get(id)['fields']['Name']
    AT.delete(id)

    messages.warning(request, 'Deleted succefully movie {}'.format(movie_name))
    return redirect('/')
        
        
        
