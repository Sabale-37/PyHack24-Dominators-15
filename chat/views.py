# chat/views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message

@login_required
def chat_home(request):
    form = MessageForm()
    return render(request, 'chat_home.html', {'form': form})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            # Assuming there's only one superuser
            superuser = User.objects.filter(is_superuser=True).first()
            if superuser:
                message.receiver = superuser
                message.save()
                return redirect('view_messages')
    return redirect('chat_home')

@login_required
def view_messages(request):
    if request.user.is_superuser:
        messages = Message.objects.all()
    else:
        messages = Message.objects.filter(sender=request.user)
    return render(request, 'view_message.html', {'messages': messages})
