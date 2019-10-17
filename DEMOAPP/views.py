from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import PredictionForm
from . import machine_learning
from .machine_learning import ModelTraining
from . import graphsPLot
from . import statistics


def load_dashboard(request):
    if not ModelTraining.model_trained:
        ModelTraining.model_xr = machine_learning.ModelTraining.train_model()
        ModelTraining.model_trained = True
    #graphsPLot.plot_graph()
    stats = statistics.get_stats()
    args = {'no_of_apps': stats[0], 'rating': stats[1], 'version': stats[2], 'zero_ratio': stats[3], 'non_zero_ratio': stats[4]}
    return render(request, 'DEMOAPP/dashboard.html',args)


class PredictorView(TemplateView):
    template_name = 'DEMOAPP/predictor.html'


    def get(self, request, **kwargs):
        form = PredictionForm()
        if not ModelTraining.model_trained:
            ModelTraining.model_xr = machine_learning.ModelTraining.train_model()
            ModelTraining.model_trained = True
        stats = ModelTraining.get_stats()
        apps = statistics.get_stats()
        apps = apps[0]
        return render(request, self.template_name, {'no_of_apps': apps, 'form': form,'accuracy': stats[0] , 'train_ratio': int(stats[1]), 'test_ratio': int(stats[2])})

    def post(self, request):
        if not ModelTraining.model_trained:
            ModelTraining.model_xr = machine_learning.ModelTraining.train_model()
            ModelTraining.model_trained = True
        form = PredictionForm(request.POST)
        if form.is_valid():
            app_name = form.cleaned_data['appName']
            size = float(form.cleaned_data['size'])
            android_version = float(form.cleaned_data['androidVersion'])
            category = float(form.cleaned_data['category'])
            price = float(form.cleaned_data['price'])
            content = float(form.cleaned_data['content'])
            genre = float(form.cleaned_data['genre'])
            reviews = float(100)
            installs = float(1000)
            values = [category, reviews, size, installs, price, content, genre, android_version]
            message = ModelTraining.rating_prediction(values)

        form = PredictionForm()
        predicted_rating = "The expected rating for "+app_name+" is : " + str(round(message[0][0],1))
        stats=ModelTraining.get_stats()
        apps=statistics.get_stats()
        apps=apps[0]
        args = {'no_of_apps': apps, 'form': form, 'rating': predicted_rating, 'accuracy': stats[0] , 'train_ratio': int(stats[1]), 'test_ratio': int(stats[2]) }

        return render(request, self.template_name, args)



