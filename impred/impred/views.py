from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import ImageForm
from .models import Images, NetModels, Labels



# Create your views here.
def main(request):
    return render(request, 'impred/index.html', context={'title': "Завантажте свою світлину і я спробую вгадати, що на ній зображено."})


def loadimage(request):
    # print(request)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            new_image = form.save(commit=False)
            #new_image.user = request.user  # предварительно для будущего usera
            new_image.save()

            # # Предварительно код для анализа images моделью и привязки к классу.
            # image_path = new_image.imagepath.path
            # prediction = model_function(image_path)  # предварительно функция для предсказания класса
            # # Получение или создание соответствующей метки (label)
            # label, created = Labels.objects.get_or_create(name=prediction, netmodel=new_image.netmodel)

            # # Привязка к модели и предсказанию
            # new_image.predict = label
            # new_image.save()
            return redirect('impred:predictimage')
    else:
        form = ImageForm()
    return render(request, 'impred/loadimage.html', {'image_form': form})


def predictimage(request):
    images = Images.objects.all()
    return render(request, 'impred/predictimage.html', {'images': images})
