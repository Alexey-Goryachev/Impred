from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ImageForm
from .models import Images

# Create your views here.
def main(request):
    return render(request, 'impred/index.html', context={'title': "Завантажте свою світлину і я спробую вгадати, що на ній зображено."})


def loadimage(request):
    # print(request)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('impred:predictimage')
    else:
        form = ImageForm()
    return render(request, 'impred/loadimage.html', {'image_form': form})


def predictimage(request):
    images = Images.objects.all()
    return render(request, 'impred/predictimage.html', {'images': images})
