# not sure if this import is needed
# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from drinker.forms import RegistrationForm, LoginForm
from drinker.models import Drinker
from django.contrib.auth import authenticate, login, logout


# Create your views here.

# if user hits the registration or already logged-in send them to profile since they are already registered
def DrinkerRegistration(request):
    if request.user.is_authenticated():
        # return HttpResponseRedirect('/profile/')
        return render_to_response('dropzone-drag-drop.html', context_instance=RequestContext(request))
    
    # what happens after someone submits the form
    if request.method == 'POST':
        # take the registration form takes what evers been filled out and post it
        form = RegistrationForm(request.POST)
        # custom validation through our clean methods through our fields
        if form.is_valid():
            # creates the user object with the attributes from form by passing it the input from POST
            user = User.objects.create_user(username=form.cleaned_data['username'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            # save the user object, which provides the user the ability to log in
            user.save()
            
 ##########################
 # DELETE THIS            
            # provided by 'off profile' module from 'settings' which has get_profile method() which gets the drinker object from the user
 #           drinker = user.get_profile()
            # set user = drinker attached to the user that is logged in according to the request
 #           user = request.get_profile()
 #           drinker.name = form.cleaned_data['name']
 #           drinker.birthday = form.cleaned_data['birthday']
 #           drinker.save()
 ##########################
 
            # creates the drinker object manually
            # drinker = Drinker(user=user, name=form.cleaned_data['name'], birthday=form.cleaned_data['birthday'])
            # without birthday
            drinker = Drinker(user=user, name=form.cleaned_data['name'])
            drinker.save();
            # return HttpResponseRedirect('/profile/')
            return render_to_response('dropzone-drag-drop.html', context_instance=RequestContext(request))
        
        # incase the form does not validate, when the user's are taken and passwords do not match, or email is invalid
        else:
            # send the form submitted that is not valid back to register.html to display the errors, so users can fix it
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
                                                                                                                                    
                                                                                                                                                    
    # responsible for showing the form
    else:
        ''' user is not submitting the form, show them a blank registration form '''
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))
        
# don't name a method "Login" since Django already provides a method for that.       
def LoginRequest(request):
    if request.user.is_authenticated():
        # so that the user does not login twice
        # return HttpResponseRedirect('/profile')
        return render_to_response('dropzone-drag-drop.html', context_instance=RequestContext(request))

    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            drinker = authenticate(username=username, password=password)
            # None: is the NULL variable in Python
            if drinker is not None:
                login(request, drinker)
                # return HttpResponseRedirect('/profile/')
                return render_to_response('dropzone-drag-drop.html', context_instance=RequestContext(request))
           
            else:
                # if there is an error, show the user the error
                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
    else:
        ''' user is not submitting the form, show the login form '''
        form = LoginForm()
        context = {'form': form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))
    
    
def LogOutRequest(request):
    logout(request)
    return HttpResponseRedirect('/')

