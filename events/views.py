from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import View
from .models import Event, Participant
from .forms import EventForm, ParticipantForm, UserRegisterForm, UserLoginForm
from datetime import datetime

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('homepage')
        
        form = UserRegisterForm()
        return render(request, 'auth/register.html', {'form': form})
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('homepage')
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('homepage')
        
        return render(request, 'auth/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('homepage')
        
        form = UserLoginForm()
        return render(request, 'auth/login.html', {'form': form})
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('homepage')
        
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('homepage')
            else:
                messages.error(request, 'Invalid username or password')
        
        return render(request, 'auth/login.html', {'form': form})

class LogoutView(View):
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully!')
        return redirect('login')

class HomepageView(View):
    def get(self, request):
        # Get all events that aren't deleted
        events = Event.objects.filter(isDeleted=False).order_by('-eventDate')
        return render(request, 'homepage.html', {'events': events})

class CreateEventView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = EventForm()
        return render(request, 'events/create_event.html', {'form': form})
    
    @method_decorator(login_required)
    def post(self, request):
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.authorId = request.user.id
            event.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event_detail', event_id=event.id)
        
        return render(request, 'events/create_event.html', {'form': form})

class EditEventView(View):
    @method_decorator(login_required)
    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id, isDeleted=False)
        
        # Check if the user is the author of the event
        if str(request.user.id) != event.authorId:
            messages.error(request, 'You do not have permission to edit this event')
            return redirect('event_detail', event_id=event.id)
        
        form = EventForm(instance=event)
        return render(request, 'events/edit_event.html', {'form': form, 'event': event})
    
    @method_decorator(login_required)
    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id, isDeleted=False)
        
        # Check if the user is the author of the event
        if str(request.user.id) != event.authorId:
            messages.error(request, 'You do not have permission to edit this event')
            return redirect('event_detail', event_id=event.id)
        
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_detail', event_id=event.id)
        
        return render(request, 'events/edit_event.html', {'form': form, 'event': event})

class EventDetailView(View):
    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id, isDeleted=False)
        participants = Participant.objects.filter(eventId=event)
        form = ParticipantForm()
        
        # Get author name from User model
        author_name = "Unknown"
        try:
            author = User.objects.get(id=event.authorId)
            author_name = author.username
        except User.DoesNotExist:
            # If user doesn't exist, keep the default "Unknown"
            pass
        
        context = {
            'event': event,
            'participants': participants,
            'form': form,
            'is_author': str(request.user.id) == event.authorId if request.user.is_authenticated else False,
            'author_name': author_name
        }
        
        return render(request, 'events/event_detail.html', context)
    
    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id, isDeleted=False)
        participants = Participant.objects.filter(eventId=event)
        form = ParticipantForm(request.POST)
        
        # Get author name from User model
        author_name = "Unknown"
        try:
            author = User.objects.get(id=event.authorId)
            author_name = author.username
        except User.DoesNotExist:
            # If user doesn't exist, keep the default "Unknown"
            pass
        
        if form.is_valid():
            # Check if email is already registered for this event
            email = form.cleaned_data.get('email')
            if Participant.objects.filter(eventId=event, email=email).exists():
                form.add_error('email', 'This email is already registered for this event')
            else:
                participant = form.save(commit=False)
                participant.eventId = event
                participant.save()
                messages.success(request, 'Successfully registered for the event!')
                return redirect('event_detail', event_id=event.id)
        
        context = {
            'event': event,
            'participants': participants,
            'form': form,
            'is_author': str(request.user.id) == event.authorId if request.user.is_authenticated else False,
            'author_name': author_name
        }
        
        return render(request, 'events/event_detail.html', context)
