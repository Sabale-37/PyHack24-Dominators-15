from django.shortcuts import render , redirect
from django.http import HttpResponse
from .student_mental_state import predict_lifestyle
from .models import LifestyleData

# Create your views here.
def mentalHealth(request):
    if request.method == 'POST':
        # Retrieve the form data
        question_values = {}
        for key in request.POST:
            if key.startswith('question'):
                question_values[key] = int(request.POST[key])

        # Calculate averages for each category
        anxiety_level = (question_values['question1'] + question_values['question2'] + question_values['question3']) / 3
        mental_health_history = (question_values['question4'] + question_values['question5'] + question_values['question6']) / 3
        depression = (question_values['question7'] + question_values['question8'] + question_values['question9']) / 3
        headache = (question_values['question10'] + question_values['question11'] + question_values['question12']) / 3
        sleep_quality = (question_values['question13'] + question_values['question14'] + question_values['question15']) / 3
        safety = (question_values['question16'] + question_values['question17'] + question_values['question18']) / 3
        academic_performance = (question_values['question19'] + question_values['question20'] + question_values['question21']) / 3
        future_career_concerns = (question_values['question22'] + question_values['question23'] + question_values['question24']) / 3
        social_support = (question_values['question25'] + question_values['question26'] + question_values['question27']) / 3
        peer_pressure = (question_values['question28'] + question_values['question29'] + question_values['question30']) / 3
        extracurricular_activities = (question_values['question31'] + question_values['question32'] + question_values['question33']) / 3
        bullying = (question_values['question34'] + question_values['question35'] + question_values['question36']) / 3

        # Store the results in variables
        # You can perform further actions with these variables, such as saving them to a database
        # or displaying them in the response
        
        return render(request, 'mental.html', {
            'anxiety_level':int( anxiety_level),
            'mental_health_history':int( mental_health_history),
            'depression':int( depression),
            'headache':int( headache),
            'sleep_quality':int( sleep_quality),
            'safety':int( safety),
            'academic_performance':int( academic_performance),
            'future_career_concerns':int( future_career_concerns),
            'social_support':int( social_support),
            'peer_pressure':int( peer_pressure),
            'extracurricular_activities':int( extracurricular_activities),
            'bullying':int( bullying)
        })
    else:
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

       

        

        return render(request, 'dashboard.html', {'chart_data': chart_data, 'result': result})

       
    return redirect('/mentalhealth/')



def calculateMental(request):
    return render(request, 'calculateMentalHealth.html')