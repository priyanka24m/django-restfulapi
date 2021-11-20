# django-restfulapi

## Instruction to run the project

1. Import postman collection in postman for better visibility.
2. Clone the project with "git clone https://github.com/priyanka24m/django-restfulapi.git"
3. Install the requirements.txt - python install -r requirements.txt 
4. Run project - python manage.py runserver

## APIS
1. create_user = localhost:8000/create_user/ - use post method and give username, password in body
2. all_users   = localhost:8000/all_users/
3. get_user    = localhost:8000/get_user/id - pass id which is int number to get single user
4. update_user = localhost:8000/update_user/id - with post method pass id which is int number to update user, also pass any of first_name, last_name, email, is_staff fields in body need to get updated
5. search_user = localhost:8000/search_user?q= - pass str, or part of str contains to search user.
user will be search str containing first_name, last_name, email, id.

