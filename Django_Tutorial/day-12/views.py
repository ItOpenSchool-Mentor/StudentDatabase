from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def student_form(request):

    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        city = request.POST.get("city")
        context = {
            "name": name,
            "age": age,
            "city": city
        }
        return render(request, "success.html", context)

    return render(request, "form.html")