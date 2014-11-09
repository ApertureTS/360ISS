from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User 



# from within dragdrop
from dragdrop.forms import UploadFileForm
from dragdrop.models import UploadFile


from dragdrop.models import Usr_name
#a_user
#a_user
# passes an HttpRequest through DraggingAndDropping
def DraggingAndDropping(request):
    # this if statement uses a HttpRequest.method, POST - submits data to be
    # processed to a specified resource 
    if request.method == 'POST':
        ########################################################################
        # TA's code
        # debugging statment 
        user_session = Session.objects.get(pk=request.session._session_key)
        #print "this is the user id: %s" % user_session.get_decoded()
        ########################################################################
       
        session_var = Session.objects.get(pk=request.session._session_key).get_decoded()
        # remember that the session key is a string so the id number has to be
        # converted in to an integer
        user = User.objects.get(id = session_var['_auth_user_id'])
        #a_user=str(user)
        #print "view.py a_user string : %s" % user#a_user

        #Usr_name=user
        #Usr_name.save()

        form = UploadFileForm(request.POST, request.FILES, user)
        # this works by default without the user session id
        # form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = UploadFile(file = request.FILES['file'])
            new_file.save()
 
            # not sure what this does, look into the reverse class from django.core.urlresolvers
            return HttpResponseRedirect(reverse('dragdrop:DraggingAndDropping'))
    else:
        form = UploadFileForm()
 
    # this has global access for the entire website
    data = {'form': form}
    return render_to_response('dropzone-drag-drop.html', data, context_instance=RequestContext(request))


    #def cur_user():
     #   return (a_user)



# def get_user_session_id():
#     session_var = Session.objects.get(pk=request.session._session_key).get_decoded()
#     user = User.objects.get(id = session_var['_auth_user_id'])
#     return user


# this is a reference example
# this is where the user uploads the file
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.Files)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/login/')
#     else:
#         # not sure what this does
#         form = UploadedFileForm()
#     return render_to_response('upload.html', {'form': form})


# def handle_uploaded_file(f):
#     # python represents 'wb+' as a file mode
#     with open('static/media/handled_uploads/', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk) 

