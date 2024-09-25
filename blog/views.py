from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('''<html>
    <title>Site NeDorazymenue</title>
    <h1>NeDorazymenue</h1>
    </html>''')
