from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Thread, Message

@login_required
def inbox_view(request):
    """
    Display all message threads for the logged-in user.
    """
    threads = Thread.objects.filter(participants=request.user).order_by('-updated_at')
    return render(request, 'messaging/inbox.html', {'threads': threads})

@login_required
def thread_view(request, thread_id):
    """
    Display a specific message thread and its messages.
    """
    thread = get_object_or_404(Thread, id=thread_id, participants=request.user)
    messages = thread.messages.order_by('timestamp')
    return render(request, 'messaging/thread.html', {'thread': thread, 'messages': messages})

@login_required
def send_message_view(request):
    """
    Handle sending a new message to a thread.
    """
    if request.method == 'POST':
        thread_id = request.POST.get('thread_id')
        content = request.POST.get('content')
        thread = get_object_or_404(Thread, id=thread_id, participants=request.user)
        Message.objects.create(thread=thread, sender=request.user, content=content)
        return redirect('messaging:thread', thread_id=thread.id)
    return HttpResponse("Invalid request", status=400)
