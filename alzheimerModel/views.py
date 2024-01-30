from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AlzheimerModel
from .models import Alzheimer
from django.http import JsonResponse
from fastai.vision.all import PILImage
from .model import model, neptune

import pathlib #you need all 3 requirements.txt
from fastai.learner import load_learner

plt = platform.system()
if plt == "Windows": pathlib.PosixPath = pathlib.PureWindowsPath

# Create your views here.
#@login_required
def myModel(request):
    
    # learner = model.load_learner("alzheimerModel/model/export.pkl")
    if request.method == 'POST':
        form = AlzheimerModel(request.POST, request.FILES) #once a request is POST we create an instance and the image will be stored under request.FILES and saved into the database
        if form.is_valid():
            form.save()
            # return redirect('success')
            return redirect('make_prediction')
    else:
        form = AlzheimerModel()
    return render(request, 'alzheimerModel/model.html', {'form': form})

# def success(request):
#     if request.method == 'GET':
#
#         #getting all the objects of image
#         image = Alzheimer.objects.all()
#
#         return render(request, 'alzheimerModel/success.html', {"images": image })


#@login_required
def make_prediction(request):
    """get the scoring parameters entered in the uploaded image and return the prediction"""
    print(neptune.model())
    path=neptune.model().download()
    print(path)
    learner = load_learner(path)
    print(learner)
    #learner = model.load_learner("alzheimerModel/model/export.pkl") #this might change location once we deploy
    object = Alzheimer.objects.last()
    img_url = object.main_img.path

    img = PILImage.create(img_url)
    pred, pred_idx, probs = learner.predict(img)
    result = probs[pred_idx]
    



    return render(request, 'alzheimerModel/prediction.html', {"prediction": str(pred), "probability": result, "image": object})
    #         #getting all the objects of image
    #         image = Alzheimer.objects.all()
    #         return render(request, 'alzheimerModel/success.html', {"images": image })
    #image_file = Alzheimer.objects.last()#get the last uploaded image




