from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Photo


# Create your views here.
def gallery(request):
    categories = Category.objects.all()

    if request.GET.get('category'):
        photos = Photo.objects.filter(
            category__name=request.GET.get('category'))
    else:
        photos = Photo.objects.all()
    context = {"categories": categories, "photos": photos}
    return render(request, 'Photos/gallery.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'Photos/photo.html', {'photo': photo})


def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['new_category'] != '':
            category, created = Category.objects.get_or_create(name=data['new_category'])
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )
        return redirect('gallery')
    return render(request, 'Photos/add.html', {'categories': categories})

def deletePhoto(request, pk):
    image = get_object_or_404(Photo, pk=pk)
    image.delete()
    return redirect('gallery')

