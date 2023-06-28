from django.shortcuts import render


# Create your views here.
def gallery(request):
    return render(request, 'Photos/gallery.html')


def viewPhoto(request, pk):
    return render(request, 'Photos/photo.html')


def addPhoto(request):
    return render(request, 'Photos/add.html')
