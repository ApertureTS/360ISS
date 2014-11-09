from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from drinker.forms import RegistrationForm, LoginForm
from drinker.models import Drinker
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session


# if user hits the registration or already logged-in send them to profile since they are already registered
def DrinkerRegistration(request):
    
    if request.user.is_authenticated():
        
        ##################
        # printing the session id to a string
        request.session._session_key
        print "this is the sessionid: %s" % request.session._session_key
        ##################  
        # return HttpResponseRedirect('/logout/')
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
            drinker = Drinker(user=user, name=form.cleaned_data['name'])
            drinker.save();
           
            ##################
            # printing the session id to a string
            request.session._session_key
            print "this is the sessionid: %s" % request.session._session_key
            ##################  
            
            return HttpResponseRedirect('/login/')
            # getting errors from uploading dropzone pictures when the after the
            # user registers with a valid form
            # return render_to_response('dropzone-drag-drop.html', context_instance=RequestContext(request))
       
        # incase the form does not validate, when the user's are taken and passwords do not match, or email is invalid
        else:

            ##################
            # printing the session id to a string    
            request.session._session_key
            print "this is the sessionid: %s" % request.session._session_key
            ##################  

            # send the form submitted that is not valid back to register.html to display the errors, so users can fix it
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
                                                                                                                                                                                                                                                          
    # responsible for showing the form
    else:
        ''' user is not submitting the form, show them a blank registration form '''
        form = RegistrationForm()
        context = {'form': form}

        ##################  
        # printing the session id to a string
        request.session._session_key
        print "this is the sessionid: %s" % request.session._session_key
        ##################  

        return render_to_response('register.html', context, context_instance=RequestContext(request))
        
# don't name a method "Login" since Django already provides a method for that.       
def LoginRequest(request):

    ##################
    # cookie test
    # request.session.set_test_cookie()

    # if request.session.test_cookie_worked():
    #     print ">>>> TEST COOKIE WORKED!"
    #     request.session.delete_test_cookie()
    ##################

    ##################
    # using sessions in views
    # request.session["fav_color"] = "blue"
    # fav_color = request.session["fav_color"]
    # 
    # if "fav_color" in request.session:
        # print 'the fav_color is stored'
    # 
    # del request.session["fav_color"]
    ##################

    ##################
    # session cookie test
    # request.session.set_test_cookie()

    # if request.session.test_cookie_worked():
    #     print ">>>> TEST SESSION COOKIE WORKED!"
    #     request.session.delete_test_cookie()
    ##################


    if request.user.is_authenticated():        
        
        # TA's suggestion, use render_to_response and pass in a variable with
        # as for one of the arguments and using ERB?
        # 
        # create a session id for the user
        #
        # images_ = images_of_current_user();

        # get session key
        # Note that all cookie values are returned as strings; do not assume 
        # that a cookie storing whole numbers will return an integer. You have 
        # to manually cast this to the correct type yourself
        # 
        # this is for Django => 1.4
        
        # this prints out the user 
        session_var = Session.objects.get(pk=request.session._session_key)
        print "this is the sessionid: %s" % session_var.get_decoded()
        

        # using sessions outside of views
        # s = Session.objects.get(pk='2b1189a188b44ad18c35e113ac6ceead')
        # s.expire_date
        # s.session_data
        #  to get the actual session data. This is necessary because the 
        #  dictionary is stored in an encoded format:
        # s.get_decoded()
        
        # when saving sessions
        # this should probably occur while logging in
        #

        return render_to_response('dropzone-drag-drop.html', context_instance=RequestContext(request))

    if request.method =='POST':

        # get session key
        # Note that all cookie values are returned as strings; do not assume 
        # that a cookie storing whole numbers will return an integer. You have 
        # to manually cast this to the correct type yourself
        # 
        # this is for Django => 1.4
        request.session._session_key
        print "this is the sessionid: %s" % request.session._session_key

        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            drinker = authenticate(username=username, password=password)
            # None: is the NULL variable in Python
            
            if drinker is not None:
                login(request, drinker)
                
                # session_var = Session.objects.get(pk=request.session._session_key).get_decoded()
                # print "this is the sessionid: %s" % session_var.get_decoded()
                # 
                # request.session['current_user_id'] = 
                return render_to_response('dropzone-drag-drop.html', context_instance=RequestContext(request))
                # return render_to_response('dropzone-drag-drop.html', context_instance=RequestContext(request))
           
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


def indexer(request):
    # rendering the response, also make the thankyou.html document
    return render_to_response("index-image.html",
                              locals(),
                              context_instance=RequestContext(request))



def get_images(request):
    return



    
# TA's suggestion
# get_images function for the user 
# def get_images
# end