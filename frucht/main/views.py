from django.shortcuts import render

# Create your views here.
def main_index(request):
    try:
        n1 = int(request.GET.get('son1', 0))
        n2 = int(request.GET.get('son2', 0))
        n = n1 + n2
    except:
        n = "Give only the numbers"

    print(request.META.get('REMOTE_ADDR'), ' - ',request.GET.get('son1'), ' - ',request.GET.get('son2'))
    return render(request, "main/index.html", {
         "ip": request.META.get('REMOTE_ADDR'),
         "wb": request.META.get('HTTP_USER_AGENT'),
         "n": n,
    })

def main_contacts(request):
    return render(request, "main/contacts.html", {
        "phone": "+998909990818",
        "wb": request.META.get('HTTP_USER_AGENT'),
    })

def main_about(reqauest):
    return render(reqauest, "main/about.html")
