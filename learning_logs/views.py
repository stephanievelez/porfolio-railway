from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')
#@login_required
def topics(request):
    """Show all topics."""
    # topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context) #context is a dictionary [names to access data: data we sent to template]

#@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    #Make sure the topic belongs to the current user
    # if topic.owner != request.user:
    #     raise Http404
    entries = topic.entry_set.order_by('-date_added') # -date_added to display most recent entries first
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """"Add a new topic"""
    if request.method != 'POST': #determines if request is GET or POST; GET requests are for reading data, POST requests are for submitting data
        #No data submitted; create a blank form
        form = TopicForm()
    else:
        #POST data submitted; process data
        form = TopicForm(data=request.POST) #we intialize the form with the data entered by the user
        if form.is_valid():
            # new_topic = form.save(commit=False) #create a new topic object and assign it to new_topic without saving it to the database yet
            #new_topic.owner = request.user #set the owner attribute of the new topic object to the current user
            # new_topic.save() #save the new topic object to the database, now that it has an owner attached to it
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics')) #redirects the reader back to the topics page after they submit their topic
    #the reverse function: Django will generate the URL from a named URL pattern
    #Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """"Add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #No data submitted; create a blank form
        form = EntryForm()
    else:
        #POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) #create a new entry object and assign it to new_entry without saving it to the database yet
            new_entry.topic = topic #set the topic attribute of the new entry object to the topic we pulled from the database
            new_entry.save() #save the new entry object to the database, now that it has a topic attached to it
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id])) #reverse() gets URL from a named URL pattern, so Django redirects to the topics page
    #Display a blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """"Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    # if topic.owner != request.user:
    #     raise Http404

    if request.method != 'POST':
        #Initial request; pre-fill form with the current entry
        form = EntryForm(instance=entry) #instance argument tells Django to create a form prefilled with the information from the existing entry object, which the user will be able to see so they can edit
    else:
        #POST data submitted; process data
        form = EntryForm(instance=entry, data=request.POST) #instance argument tells Django to create a form prefilled with the information from the existing entry object and then update it with any relevant data from request.POST
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id])) #reverse() gets URL from a named URL pattern, so Django redirects to the topics page
    topic_image = Entry.objects.all()

    #Display a blank or invalid form
    context = {'entry': entry, 'topic': topic, 'form': form, 'topic_image': topic_image}
    return render(request, 'learning_logs/edit_entry.html', context)