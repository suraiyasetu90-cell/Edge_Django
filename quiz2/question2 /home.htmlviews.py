<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
    <p>Your age is {{ age }} years old.</p>
</body>
</html>from django.shortcuts import render

def home(request):
    name = "Abdur Rahim"
    age = 22
    return render(request, 'home.html', {'name': name, 'age': age})
