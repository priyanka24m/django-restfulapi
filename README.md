# django-restfulapi

## Instruction to run the project

1. Import postman collection in postman for better visibility.
2. Clone the project with "git clone https://github.com/priyanka24m/django-restfulapi.git"
3. Run proejct - python manage.py runserver

create_user = localhost:8000/create_user/ - use post method and give username, password in body
all_users   = localhost:8000/all_users/
get_user    = localhost:8000/get_user/id - pass id which is int number to get single user
update_user = localhost:8000/update_user/id - with post method pass id which is int number to update user , also pass any of first_name, last_name, email , is_staff fields in body need to get updated
search_user = localhost:8000/search_user?q= - pass str, or part of str contains to search user.
user will be search str containing first_name, last_name, email, id.

