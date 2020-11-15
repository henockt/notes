from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from django.contrib import messages
from .forms import TextForm
from .models import Notes
import string, random

# homepage
def homepage(request):
    return render(request, "main/homepage.html")

# create a new note
def new(request):
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            print(text)
            if text == "<p>Write your notes here...</p>":
                messages.error(request, "Invalid note. Please try again.")
                return redirect("main:new")
            title = form.cleaned_data.get('title')
            if Notes.objects.count() > 1000:
                messages.error(request, "We ran out of memory. Please try again later.")
                return redirect("main:homepage")
            id = generate_id()
            note = Notes(note_id=id, note=text, note_title=title, pub_date=timezone.now())
            note.save()
            return redirect(f"/shared/{id}")
        else:
            messages.error(request, "Invalid note. Please try again.")
            return redirect("main:new")
    else:
        return render(request, "main/new.html")

# Show shared notes
def shared(request, note_id):
    notes = Notes.objects.all()
    text = None
    text_pub = None
    title = None
    for item in notes:
        if note_id == item.note_id:
            text = item.note
            text_pub = item.pub_date
            title = item.note_title
            break
    return render(request, "main/show.html", context={'text': text, 'text_pub': text_pub, 'text_id': note_id, 'text_title': title})

# Generate unique id for every note
def generate_id():
    notes = Notes.objects.all()
    note_ids = [note.note_id for note in notes]
    letters = string.ascii_lowercase
    while True:
        new_id = ''.join(random.choice(letters) for i in range(10))
        if new_id not in note_ids:
            break
    return new_id
    

# handle 404
def error_404(request, exception):
    error = {"error_404": True, "error_500": False}
    return render(request, "main/error.html", error)

# handle 500
def error_500(request):
    error = {"error_404": False, "error_500": True}
    return render(request, "main/error.html", error)