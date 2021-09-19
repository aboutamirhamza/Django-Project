from django.shortcuts import render
from .models import *
# Create your views here.
def user_data(request):
    user = UserProfile.objects.all()
    con = {'userData':user}
    return render(request, 'home.html', con)