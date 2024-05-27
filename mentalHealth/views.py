from django.shortcuts import render , redirect
from django.http import HttpResponse
from .student_mental_state import predict_lifestyle
from .models import LifestyleData

# Create your views here.
def mentalHealth(request):
    return render(request, 'mental.html')

def dashboard(request):
    if request.method == 'POST':
        
        anxiety_level = float(request.POST['anxiety_level'])
        mental_health_history = float(request.POST['mental_health_history'])
        depression = float(request.POST['depression'])
        headache = float(request.POST['headache'])
        sleep_quality = float(request.POST['sleep_quality'])
        safety = float(request.POST['safety'])
        academic_performance = float(request.POST['academic_performance'])
        future_career_concerns = float(request.POST['future_career_concerns'])
        social_support = float(request.POST['social_support'])
        peer_pressure = float(request.POST['peer_pressure'])
        extracurricular_activities = float(request.POST['extracurricular_activities'])
        bullying = float(request.POST['bullying'])

        print(bullying)
        prediction = predict_lifestyle(
            anxiety_level, mental_health_history, depression, headache,
            sleep_quality, safety, academic_performance, future_career_concerns,
            social_support, peer_pressure, extracurricular_activities, bullying
        )

        if prediction == 0:
            result = "Perfect lifestyle"
        elif prediction == 1:
            result = "Lifestyle change needed"
        else:
            result = "Therapy needed"



        lifestyle_data = LifestyleData(
           
            anxiety_level=anxiety_level,
            mental_health_history=mental_health_history,
            depression=depression,
            headache=headache,
            sleep_quality=sleep_quality,
            safety=safety,
            academic_performance=academic_performance,
            future_career_concerns=future_career_concerns,
            social_support=social_support,
            peer_pressure=peer_pressure,
            extracurricular_activities=extracurricular_activities,
            bullying=bullying,
            prediction=result
        )
        lifestyle_data.save()

        user = request.user
        latest_data = LifestyleData.objects.latest('id')
        

        # Get data for the chart
        chart_data = {
            'labels': list(latest_data.__dict__.keys())[2:-1],  # Exclude id and prediction fields
            'values': list(latest_data.__dict__.values())[2:-1]  # Exclude id and prediction values
        }

        newresult =latest_data.prediction
        print('newresult', newresult)

        

        return render(request, 'dashboard.html', {'chart_data': chart_data, 'result': newresult})

       
    return redirect('/mentalhealth/')