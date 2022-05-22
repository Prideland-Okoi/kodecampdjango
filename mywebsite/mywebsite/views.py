#class based view
#function view
from django.http import HttpResponse

def home_view(request):
    """
    Take in a request(Django send request)
    Return HTML as a response
    """
    name = "Welcome to Prideland Okoi website."
    number = random.randint(10, 475)
    HTML_STRING =f"""
    <h1>Hello Guest, you are {name} -{number}!</h1>
    """
    return HttpResponse(HTML_STRING)

def about_view(request):
    return HttpResponse("<h1> About page</h1>")

def contact_view(request):
    return HttpResponse("<h1> Twitter.com/pridemyhero</h1>")
