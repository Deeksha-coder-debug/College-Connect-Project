from django.shortcuts import render,redirect
# renders html templates with data
from django.contrib.auth.decorators import login_required
# ensures only logged in users can access dashboard (security layer)
from django.contrib.auth.forms import UserCreationForm
from .models import Announcement,StudyMaterial

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@login_required
# protected by @login_required so if someone isn't logged in , they get
# get redirected to login page
def dashboard(request):
    user=request.user
    # fetches currently logged in user ohj 
    # from this we can access user.username, user.email,etc
    latest_announcements = Announcement.objects.order_by('-date_posted')[:3]  # Get latest 3
    context = {
        'username': user.username,
        'materials_count': 12,
        'attendance_percent': 87,
        'upcoming_events': 3,
        'announcements': latest_announcements,  # Pass to template
    }
    # context dictionary holds data we’ll send to the HTML template.
    # These are placeholders for now (materials_count, attendance_percent, etc.)
    # In future: fetch these dynamically from database (e.g., from models).

    return render(request, 'core/dashboard.html', context)
    # Loads the template dashboard.html inside the core app’s templates folder.
    # Passes the context so that values like {{ username }} work inside the HTML.

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # name from urls.py
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def materials_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')
        if title and file:
            StudyMaterial.objects.create(user=request.user, title=title, file=file)
            return redirect('materials')

    materials = StudyMaterial.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'core/materials.html', {'materials': materials})

@login_required
def attendance_view(request):
    return render(request, 'core/attendance.html')

@login_required
def events_view(request):
    return render(request, 'core/events.html')

@login_required
def announcements(request):
    all_announcements = Announcement.objects.order_by('-date_posted')
    return render(request, 'core/announcements.html', {
        'announcements': all_announcements
    })
