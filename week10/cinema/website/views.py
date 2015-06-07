from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie, Reservation, Projection
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    projections = Projection.objects.all()
    # if request.method == "POST":
    #     projection_id = request.POST.get("projection_id")
    return render(request, 'index.html', locals())
    # return render(request, 'movies.html', locals())
    # return HttpResponse(str(movies[0].name))


def reserved(request):
    movies = Movie.objects.all()
    return render(request, "reserved.html")


def register(request):
    # return HttpResponce("responceee register")
    # return render(request, 'register.html')
    return render(request, "register.html", {"movies": Movie.objects.all(),
           "projections": Projection.objects.all()})


def reservation(request, projection_id):
    projection = Projection.objects.get(id=projection_id)
    if request.method == "POST":
        username = request.POST.get("username")
        row = request.POST.get("row")
        column = request.POST.get("column")

        return redirect("reserved")

    return render(request, "reservation.html", locals())


def show_projection(request):
    return render(request, 'movies.html', locals())
