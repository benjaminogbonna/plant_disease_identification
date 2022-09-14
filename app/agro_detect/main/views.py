from django.shortcuts import render
import os
import math
import numpy as np
from django.core.files.storage import default_storage
import tensorflow as tf
from .helper_function import load_and_pred

cur_dir = os.path.dirname(__file__)
model = tf.keras.models.load_model(os.path.join(cur_dir, 'model', 'model_0.h5'))

# Create your views here.

class_names = ['anthracnose', 'cercospora_leaf_spot', 'phosphorus_deficiency']
food_names = {
    'anthracnose': 'Anthracnose',
    'cercospora_leaf_spot': 'Cercospora Leaf Spot',
    'phosphorus_deficiency': 'Phosphorus Deficiency',
}


def index(request):
    if request.method == 'POST':        
        file = request.FILES["image"]
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.path(file_name)     
        try:
            pred, prob = load_and_pred(model, file_url, class_names)             
        except ValueError as e:
            prediction = 'An error occured, try again!'
        else:
             prediction, probability = pred, prob
        context = {
            'pred': prediction,
            'prediction': food_names[prediction],
            'probability': probability,
            # 'prob': f'{math.ceil(pred.max()*100)}%'
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


def anthracnose(request):
    return render(request, 'diseases/anthracnose.html')


def cls(request):
    return render(request, 'diseases/cls.html')


def pd(request):
    return render(request, 'diseases/pd.html')


def camera(request):
    return render(request, 'camera.html')
