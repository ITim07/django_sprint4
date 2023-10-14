from django.shortcuts import render


def about(request):
    return render(request, 'pages/about.html', {})


def rules(request):
    return render(request, 'pages/rules.html', {})


def page_not_found(request):
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request):
    return render(request, 'pages/403csrf.html', status=403)


def internal_server_error(request):
    return render(request, 'pages/500.html', status=500)
