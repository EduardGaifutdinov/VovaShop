from django.shortcuts import render

def test_view(request):
    return render(request, 'FAQ.html', {})