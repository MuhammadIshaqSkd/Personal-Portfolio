from django.shortcuts import render
from .models import Category, Portfolio, Messege


def portfolio_page(request):
    return render(request, 'portfolio/portfolio.html')

def portfolio_details(request, portfolio_id):
    item = Portfolio.objects.get(id=portfolio_id)
    context = {
        'item': item
    }
    return render(request, 'portfolio/portfolio-details.html', context)


def messages(request):
    if request.method == "POST":
        message = request.POST.get('message', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')

        msgs = Messege(message=message, name=name, email=email, subject=subject)
        msgs.save()
    return render(request, 'contact.html', {'name': name})
