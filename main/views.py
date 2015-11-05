from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.template import RequestContext
from main.models import Recipe 


def recipe_list_view(request):
    recipes = Recipe.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'recipe_list_view.html', {'recipes': recipes})


def recipe_detail_view(request, pk):
    recipes = Recipe.objects.get(pk=pk)

    return render(request, 'recipe_detail_view.html', {'recipes': recipes})


def common_ingredients(request):
    context = {}
    return render_to_response('common_ingredients.html', context, context_instance=RequestContext(request))


def main_view(request):
    context = {}
    return render_to_response('main_page.html', context, context_instance=RequestContext(request))


def new_entries(request):
    context = {}
    return render_to_response('new_entries.html', context, context_instance=RequestContext(request))


def cookie(request):
    recipies = Recipe.objects.all()
    context = {}
    cookies = []
    print "Here"

    for cookie in recipies:
        print cookie
        print type(cookie)
        print cookie.recipe_type
        print type(cookie.recipe_type)
        if cookie.recipe_type == "cookie":
            print 'success'
            cookies.append()
    print cookies
    context['cookies'] = cookies

    return render_to_response('cookie.html', context, context_instance=RequestContext(request))


def cakes(request):
    context = {}
    return render_to_response('cakes.html', context, context_instance=RequestContext(request))


def dessert_bars(request):
    context = {}
    return render_to_response('dessert_bars.html', context, context_instance=RequestContext(request))


# #def create_view1(request):
#         context = {}
#         form = RecipeModelForm()

#         context['form'] = form

#         if request.method == 'POST':
#             form = RecipeModelForm(request.POST, request.FILES)
#             if form.is_valid():
#                 print form.is_valid()

#                 form.save()
#                 return HttpResponseRedirect('/recipe_list_view/')

#             else:
#                 context['errors'] = form.errors
#         return render_to_response('create_view1.html', context, context_instance=RequestContext(request))


# #def create_view2(request):
#     context = {}

#     form = RecipeModelForm2()
#     context['form'] = form

#     if request.method == "POST":
#         form = RecipeModelForm2(request.POST, request.FILES)

#         if form.is_valid():

#             print form.cleaned_data

#             title = form.cleaned_data['title']
#             info = form.cleaned_data['info']
#             image = form.cleaned_data['image']

#             new_object = RecipeModel()

#             new_object.title = title

#             return HttpResponseRedirect('/list_view/')
#         else:
#             context['errors'] = form.errors

#     return render_to_response('create_view2.html', context, context_instance=RequestContext(request))


# #def update_view(request, pk):
#     context = {}

#     recipe_object = RecipeModel.object.get(pk=pk)

#     context['recipe_object'] = recipe_object

#     form = RecipeModelUpdateForm()

#     context['form'] = form

#     if request.method == "POST":
#         form = RecipeModelUpdateForm(request.POST, request.FILES)

#         if form.is_valid():
#             recipe_object.title = form.cleaned_data['title']
#             recipe_object.info = form.cleaned_data['info']

#             if form.cleaned_data['image'] != None:
#                 speed_object.image = form.cleaned_data['image']

#             speed_object.save()

#             return HttpResonseRedirect('/update_view/%s/' % pk)

#         else:
#             context['errors'] = form.errors
#     return render_to_response('update_view.html', context, context_instance=RequestContext(request))

# #def delete_view(request, pk):
#     RecipeModel.objects.get(pk=pk).delete()

#     return HttpResonseRedirect('/list_view/')

# #def signup(request):
#     context = {} 

#     form = UserSignUp()
#     context['form'] = form

#     if request.method == 'POST':
#         if form.is_valid():
#             print form.cleaned_data

#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']

#         try:
#             new_user = User.objects.creeate_user(name, email, password)
#             context['valid'] = "Thank You For Signing Up!"

#             auth_user = authenticae(username=name, password=password)
#             login(request, auth_user)

#             return HttpResonseRedirect('/list_view/')
#         except IntegrityError, e:
#             context['valid'] = "A User With That Name Already Exists"
#     else:
#         context['valid'] = form.errors

#     if request.method == 'GET':
#         context['valid'] = "Please Sign Up!"

# return render_to_response('signup.html', context, context_instance=RequestContext(request))

# #def login_view(request):

#     context = {}

#     context['form'] = UserLogin()

#     username = request.POST.get('username', None)
#     password = request.POST.get('password', None)

#     auth_user = authenticate(username=username, password=password)

#     if auth_user is not None:
#         if auth_user.is_active:
#             login(request, auth_user)
#             context['valid'] = 'Login Successful'

#             return HttpResponseRedirect('/home/')
#         else:
#             context['valid'] = "Invalid User"
#     else:
#         context['valid'] = "Please enter a User Name"

# return render_to_response('login_view.html', context, context_instance=RequestContext(request))

# #def logout_view(request):
#     logout(request)

#     return HttpResonseRedirect('/login_view/')
