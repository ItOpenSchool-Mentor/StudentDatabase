from django.shortcuts import render

# Create your views here.

def calc():
    a = 5
    b = 6
    print(f"{a} x {b} = {a * b}")

def hello(request):
    print("Started `hello` function")
    print(f"Request Object : {request}")
    print(f"Path : {request.path}")

    calc()

    name = "Rohit"
    age = 25

    context = {
        "name" : name,
        "age" : age,
    }

    return render(request, "hello.html")
