from django.shortcuts import render

# Create your views here.

def send_message(request):
    zaki='zakijson my firsdt application using django'
    context = {'zaki':zaki}
    return render(request,'contact/contact.html',context)
