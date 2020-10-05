from django.http import JsonResponse
from django.shortcuts import render
from .models import PredictionHistory
from pathlib import Path
import pandas as pd
import os

BASE_DIR = Path(__file__).resolve().parent.parent


# Create your views here.
def index(request):
	return render(request, 'index.html')


def make_prediction(request):
	if request.POST.get('action') == 'POST':
		# Get values from form
		sepal_length = float(request.POST.get('sepal_length'))
		sepal_width = float(request.POST.get('sepal_width'))
		petal_length = float(request.POST.get('petal_length'))
		petal_width = float(request.POST.get('petal_width'))

		# Load ml model(pickle file)
		model = pd.read_pickle(os.path.join(BASE_DIR, 'iris_model.pickle'))

		# Making prediction
		pred = model.predict([[
			sepal_length, sepal_width,
			petal_length, petal_width
		]])
		prediction = pred[0]

		PredictionHistory.objects.create(
			sepal_length=sepal_length, sepal_width=sepal_width,
			petal_length=petal_length, petal_width=petal_width,
			prediction=prediction
		)

		return JsonResponse({
			'prediction': prediction,
			'sepal_length': sepal_length, 'sepal_width': sepal_width,
			'petal_length': petal_length, 'petal_width': petal_width
		}, safe=False)


def show_history(request):
	data = {'data': PredictionHistory.objects.all()}
	return render(request, 'history.html', data)
