from G1DB_Site.models import User

def user_processor(request):
    context = dict()
    if(request.session.__contains__("uid")):
        context['currentUser'] = User.objects.get(uid=request.session["lid"])
    return context
