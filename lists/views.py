from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render

from lists.models import Item


def home_page(request):
    # return HttpResponse('<html><title>To-Do lists </title></html>')
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/lists/the-only-list-in-the-world/')

    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
