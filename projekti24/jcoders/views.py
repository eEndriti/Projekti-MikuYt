from django.shortcuts import render
from .models import animacionet
from django.template import RequestContext
from .models import animacionet, categorite
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from jcoders.forms import ContactForm


# Create your views here.
def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['fidelbandoy622@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')

def homepage(request):
    animations = animacionet.objects.all()
    return render(request, 'home.html', {'animations': animations})


def handleSearch(request, keyword):
    if keyword:
        results = animacionet.objects.get(emriianimacionit=keyword)

    similar = animacionet.objects.filter(categoryId=results.categoryId)

    return render(request, 'animacioni.html', {'results': results, 'similar': similar})


def animactioni(request, emri):
    return handleSearch(request, emri)

def kategorite (request):
    kategorite = categorite.objects.all()
    items = animacionet.objects.all()
    return render(request, 'kategorite.html', { 'kategorite': kategorite, 'items': items })

def search(request):
    query = request.GET.get('q')
    return handleSearch(request, query)
    # return render_to_response('results.html', {"results": results,}, context_instance=context)
def kontakti(request):
    return render(request,'kontakti.html')

def rrethne (request):
    return render(request, 'rrethne.html')
