from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        if form.is_valid():
            email = EmailMessage()
            return render(request, 'index.html')
        else:
            render(request, 'contact/contact.html')

    else:
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})
