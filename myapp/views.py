from django.shortcuts import render
from django.http import HttpResponse
from joblib import load

model = load('./savedModels/model.joblib')

def welcome(request):
    return render(request, 'sample.html')

def get_data(request):
    if request.method == 'POST':

        print("hello")

        sepal_length = request.POST['sepal_length']
        sepal_width = request.POST['sepal_width']
        petal_length = request.POST['petal_length']
        petal_width = request.POST['petal_width']

        y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        if y_pred[0] == 0:
            y_pred = 'setosa'
        
        elif y_pred[0] == 1:
            y_pred = 'Versicolor'

        else:
            y_pred = 'Virginica'

        print(y_pred)

        return render(request, 'prediction.html', {'result': y_pred})




    return render(request, 'prediction.html')



    
#4.7, 3.2, 1.3, 0.2
    


    
