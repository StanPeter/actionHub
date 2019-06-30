from django.shortcuts import render
from django.contrib import messages
import os
from airtable import Airtable


os.environ['AIRTABLE_API_KEY']='keyEWA5dgzZT3UuEq'
AT = Airtable('appiQ5ITgJTbG4Gws', 'Movies')

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

    """
    for i in range(len(database)):
            try:                if user_query.lower() in str(database[i]['fields']['Name']).lower():
                        search_result.append(str(database[i]['fields']))
            excEpt KeyError:
                    pass
    
    return render(request, 'movieApp/index.html')

    """