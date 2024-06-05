
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import URL
import string
import random

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def redirect_to_original(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    print(f"Original URL: {url.original_url}, Clicks before increment: {url.clicks}")
    url.clicks += 1  # Increment the click counter
    url.save()  # Save the updated URL object
    print(f"Clicks after increment: {url.clicks}")
    return redirect(url.original_url)

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        custom_short_url = request.POST.get('custom_short_url', '').strip()

        if custom_short_url:
            if URL.objects.filter(short_url=custom_short_url).exists():
                return HttpResponse("Custom short URL already in use. Please try another one.")
            short_url = custom_short_url
        else:
            short_url = generate_short_url()
            while URL.objects.filter(short_url=short_url).exists():
                short_url = generate_short_url()

        url = URL(original_url=original_url, short_url=short_url)
        url.save()
        return render(request, 'index.html', {'short_url': request.build_absolute_uri('/') + short_url, 'url': url})
    return render(request, 'index.html')

