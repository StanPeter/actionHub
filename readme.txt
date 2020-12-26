Information:


    A movie app. Simple CRUD functionality. 
    
    On BE using django3 and python3 together with Airtable database.

    On FE using HTML5, css3 and some JS.



Instructions: (commands for Windows might differ)


    1. Create a new environment                                 "  python -m venv venv  " 

    2. Activate it                                              "  source venv/bin/activate  "

    3. install required libraries by executing                  "  pip install -r requirements.txt  "

    4. now run the migrations                                   "  python manage.py makemigrations  "

    5. migrate                                                  "  python manage.py migrate  "

    6. run the server and open on displayed url                 " python manage.py runserver  "



PS: step 3 might encounter issues on ubuntu due to pg_config. -> fix by executing in terminal  "  sudo apt-get install libpq-dev  "

Also step 4 and 5 are optinals as this project uses Airtable DB instead of a local one -> thus no model inside models as well 
but maybe you will change that

4 movies inside mock_data.py in case you need some quick data. (uncomment 19th line inside views.py, run the server and comment again)