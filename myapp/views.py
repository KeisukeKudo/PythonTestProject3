from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoBord


def MyAppIndex(request):
    msg = request.GET.get('words')

    delete_text = request.POST.getlist('delete_text')

    if delete_text:
        TodoBord.objects.all().delete()

    data_list = TodoBord.objects.order_by('-id')
    contexts = {
        'result_list': data_list
    }

    if msg is not None:
        message_data = TodoBord()
        message_data.new_message = msg
        message_data.image_url = request.FILES.get('files')
        message_data.save()

    return render(request, 'myapp/index.html', contexts)

