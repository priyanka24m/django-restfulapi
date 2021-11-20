from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import basicauth  
from django.db.models import Q

'''
Authenticate user with username and password
eg. in postman pass username and password with basic auth.
'''
def authenticate_user(request):
  
    if 'HTTP_AUTHORIZATION' in request.META:
        username, passwd = basicauth.decode(request.META['HTTP_AUTHORIZATION'])
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            login(request, user)
            return JsonResponse({'username':username,'password':passwd,'status':'logged in'})
    
    return JsonResponse({'status':'provide correct credentials'})


'''
Create user with username and password at first.
For creating user, must login with username and password via basic auth.

'''
@csrf_exempt
def create_user(request):
    if 'HTTP_AUTHORIZATION' in request.META:
        username, passwd = basicauth.decode(request.META['HTTP_AUTHORIZATION'])
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            login(request, user)
            username = request.POST['username']
            password = request.POST['password']
           
            User.objects.create_user(username=username,password=password)
            user = User.objects.get(username=username)
            user_data = {
                    'id':user.pk,
                    'username':user.username,
                    'first_name':user.first_name,
                    'last_name':user.last_name,
                    'email':user.email,
                    'is_staff':user.is_staff
                }
            return JsonResponse(user_data)
        else:
            return JsonResponse({'status':'Incorrect username or password'})        
   
    return JsonResponse({'status':'must login first'})        

'''
Get all users.
For this user, must login with username and password via basic auth 
'''
def get_all_users(request):
    if 'HTTP_AUTHORIZATION' in request.META:
        username, passwd = basicauth.decode(request.META['HTTP_AUTHORIZATION'])
        user = authenticate(request, username=username, password=passwd)
        print(username, passwd)
        if user is not None:
            login(request, user)
            users = User.objects.values()

            user_data = []
            if users != {}: 
                for user in users:
                    data = {
                        'id':user['id'],
                        'username':user['username'],
                        'first_name':user['first_name'],
                        'last_name':user['last_name'],
                        'email':user['email'],
                        'password':user['password'],
                        'is_staff':user['is_staff']
                    }
                    user_data.append(data)

            return JsonResponse({'users':user_data})
        else:
            return JsonResponse({'status':'Incorrect username or password'})        
   
    return JsonResponse({'status':'must login first'})        

'''
After creating user ,
For updating/adding any other fields - first_name, last_name, email, is_staff     
Get single user by providing id.
For this user, must login with username and password via basic auth 
'''
def get_single_user(request,id):
    if 'HTTP_AUTHORIZATION' in request.META:
        username, passwd = basicauth.decode(request.META['HTTP_AUTHORIZATION'])
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            login(request, user)

            try:
                user = User.objects.get(id=id)
                user_data = {
                    'id':user.pk,
                    'username':user.username,
                    'first_name':user.first_name,
                    'last_name':user.last_name,
                    'email':user.email,
                    'is_staff':user.is_staff
                }
            except ObjectDoesNotExist:
                user_data = {
                    'detail':'No user with id {} exist.'.format(str(id))
                }
            return JsonResponse(user_data)
        else:
            return JsonResponse({'status':'Incorrect username or password'})        
    
    return JsonResponse({'status':'must login first'}) 

'''
Update user data with providing id.
User will only be able to update first_name, last_name, email, is_staff.  
is_staff could be 0 or 1.
For this user, must login with username and password via basic auth 
'''
@csrf_exempt
def update_user(request,id):
    if 'HTTP_AUTHORIZATION' in request.META:
        username, passwd = basicauth.decode(request.META['HTTP_AUTHORIZATION'])
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            login(request, user)
            getuser = User.objects.filter(id=id)
            if 'first_name' in request.POST:
                getuser.update(first_name=request.POST['first_name'])
            if 'last_name' in request.POST:
                getuser.update(last_name=request.POST['last_name'])
            if 'email' in request.POST:
                getuser.update(email=request.POST['email'])    
            if 'is_staff' in request.POST:
                getuser.update(is_staff=request.POST['is_staff'])    
            
            try:
                user = User.objects.get(id=id)
                user_data = {
                    'id':user.pk,
                    'username':user.username,
                    'first_name':user.first_name,
                    'last_name':user.last_name,
                    'email':user.email,
                    'is_staff':user.is_staff
                }
            except ObjectDoesNotExist:
                user_data = {
                    'detail':'No user with id {} exist.'.format(str(id))
                }
            return JsonResponse(user_data)
    
        else:
            return JsonResponse({'status':'Incorrect username or password'})        
   
    return JsonResponse({'status':'must login first'}) 

'''
Search user with email ,first_name, last_name or id
For this user, must login with username and password via basic auth 
'''

def search_user(request):
    if 'HTTP_AUTHORIZATION' in request.META:
        username, passwd = basicauth.decode(request.META['HTTP_AUTHORIZATION'])
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            login(request, user)
            query = request.GET['q']
            results = User.objects.filter(Q(email__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(username__icontains=query) |Q(id__icontains=query)).values()
            
            user_data = []
            if results != {}:
                for result in results:
                    print(result)
                    data = {
                        'id':result['id'],
                        'username':result['username'],
                        'first_name':result['first_name'],
                        'last_name':result['last_name'],
                        'email':result['email'],
                        }
                    user_data.append(data)
            return JsonResponse({'search_results':user_data})
        else:
            return JsonResponse({'status':'Incorrect username or password'})        
   
    return JsonResponse({'status':'must login first'}) 
