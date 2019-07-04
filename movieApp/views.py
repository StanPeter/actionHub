from django.shortcuts import render, redirect
from django.contrib import messages
import os
from airtable import Airtable
from .appi_key import AIRTABLE_API_KEY, AIRTABLE_BASE_ID, TABLE_NAME


os.environ['AIRTABLE_API_KEY']= AIRTABLE_API_KEY
AT = Airtable(AIRTABLE_BASE_ID, TABLE_NAME)

#database = AT.get('Movies')['records']
#movie_name = database['records'][i]['fields']['Name']
#KeyError: 'Name'

# Create your views here.

def home_page(request):
        user_query = str(request.GET.get('query', ''))
        # pulls information from our query (index.html)    print(user_query)
        search_result = AT.get_all(formula="FIND('" + user_query.lower() + "',LOWER({Name}))")
        stuff_for_frontend = {'search_result':search_result}
        return render(request, 'movieApp/index.html', stuff_for_frontend)

def movie_create(request):
        if request.method == 'POST':
                new_movie = {
                        'Name': request.POST.get('Name'),
                        'Notes': request.POST.get('Notes'),
                        'Pictures': [{'url': request.POST.get('Pictures')}],
                        'Rating': int(request.POST.get('Rating'))
                }
                AT.insert(new_movie)
        return redirect('/')

"""
for i in range(len(database)):
        try:                if user_query.lower() in str(database[i]['fields']['Name']).lower():
                search_result.append(str(database[i]['fields']))
        excEpt KeyError:
                pass

return render(request, 'movieApp/index.html')

"""