from django.shortcuts import render
from home2.forms import BookForms
from home2.models import Book

# Create your views here.

def form_view(reuest):
    context = None
    msg = None
    form = None
    if request.method =='POST':
        form = BookForms(request.POST)
        if form.is_valid():
           # book = Book.objects.create(
            #name=form.cleane_data.get('name'),
            #purchase_date=form.cleaned_data.get('pur_date'),
            #genre=form.cleaned_dataget('genre'),
            #author=formcleaned_data.get('author')
            #)
            book save()
            msg = 'Book Added successfully!!!'
        else:
            msg = form.errors
    else:
        form = BookForms()
    return render(reuest,'forms.html',{ "msg":msg, "forms":form})
