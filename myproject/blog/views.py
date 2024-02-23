from django.shortcuts import render, redirect
from .forms import FileUploadForm

def index(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "File uploaded successfully."
            return redirect('index_with_message')  
    else:
        form = FileUploadForm()
    return render(request, 'index.html', {'form': form})

def index_with_message(request):
    message = "File uploaded successfully."
    form = FileUploadForm() 
    return render(request, 'index.html', {'form': form, 'message': message})
