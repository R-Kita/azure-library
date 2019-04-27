from django.shortcuts import render

def novel_list(request):
    return render(request, 'azure/novel_list.html', {})
