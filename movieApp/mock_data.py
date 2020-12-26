
mock_data = [
    {
        'Name': 'The Bourne Ultimatum',
        'Notes': 'Jason Bourne, a former CIA assassin who suffers from amnesia, sets out to track down a CIA official whilst trying to retain memories of a forgotten past.',
        'Pictures': [{'url': 'https://images-na.ssl-images-amazon.com/images/I/51EBmpDHaBL.jpg'}],
        'Rating': 8
    },
    {
        'Name': 'Rambo',
        'Notes': 'John Rambo, a former US soldier traumatised by memories of the Vietnam War, gets into trouble when an incident with a small-town sheriff triggers his violent side.',
        'Pictures': [{'url': 'https://images-na.ssl-images-amazon.com/images/I/51TMEBCRY0L._AC_SY445_.jpg'}],
        'Rating': 7
    },
    {
        'Name': 'Terminator 2: Judgment Day',
        'Notes': 'A terminator is set on a mission to kill Sarah\'s son, John Connor. However, another cyborg, who was once after Sarah\'s life, has now been assigned to protect him.',
        'Pictures': [{'url': 'https://images-na.ssl-images-amazon.com/images/I/51hRUw7ba6L._AC_.jpg'}],
        'Rating': 8
    },
    {
        'Name': 'Black hawk down',
        'Notes': 'Captain Mike Steele leads a team of nearly 100 US Army Rangers who travel to the capital city of Mogadishu to catch the top two lieutenants of a Somali warlord.',
        'Pictures': [{'url': 'https://images02.military.com/sites/default/files/styles/full/public/2019-05/blackhawkdownedhelo1500.jpg'}],
        'Rating': 10
    },
]


# create initial data
def init_data(AT):

    for movie in mock_data:
        AT.insert(movie)
