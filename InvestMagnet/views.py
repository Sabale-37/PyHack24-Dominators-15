from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Company
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Message
from django.contrib.auth.decorators import login_required



# Create your views here.
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company_list.html', {'companies': companies})

def company_detail(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    
    # Convert JSONField data to Python dictionaries
    yearwise_revenue_data = company.yearwise_revenue
    yearwise_growth_data = company.yearwise_growth
    digital_marketing_data =company.digital_marketing
    financial_graph_data = company.financial_graph
   

    # Pass the data to the template
    context = {
        'company': company,
        'yearwise_revenue_data': yearwise_revenue_data,
        'yearwise_growth_data': yearwise_growth_data,
        'digital_marketing_data': digital_marketing_data,
        'financial_graph_data': financial_graph_data,
    }

    return render(request, 'company_detail.html', context)
   





def add_company(request):
    if request.method == 'POST':
        data_file = request.FILES.get('data_file')
        image = request.FILES.get('image')  # Assuming image is still uploaded separately

        if data_file:
            try:
                file_content = data_file.read().decode('utf-8')
                data = json.loads(file_content)
                
                # Extract data from JSON
                username = request.user
                start_year = data.get('start_year')
                company_name = data.get('company_name')
                problem_statement = data.get('problem_statement')
                solution = data.get('solution')
                market_opportunity = data.get('market_opportunity')
                team = data.get('team')
                description = data.get('description')
                revenue = data.get('revenue')
                founder = data.get('founder')
                investment_round = data.get('investment_round')
                yearwise_revenue = data.get('yearwise_revenue')  # This should be an array
                yearwise_growth = data.get('yearwise_growth')    # This should be an array
                digital_marketing = data.get('digital_marketing')  # This should be an array or object
                financial_data = data.get('financial_graph')

                # Validate required fields
                if not all([start_year, problem_statement, solution, market_opportunity, team, description, revenue, founder, investment_round, yearwise_revenue, yearwise_growth, digital_marketing, company_name, financial_data]):
                    return render(request, 'add_company.html', {'error': 'Missing required fields in JSON file'})

                # Additional validation if needed
                if not isinstance(team, int) or team < 0:
                    return render(request, 'add_company.html', {'error': 'Team must be a non-negative integer'})

                # Create and save the company instance
                company = Company(
                    username=username,
                    start_year=start_year,
                    problem_statement=problem_statement,
                    solution=solution,
                    market_opportunity=market_opportunity,
                    team=team,
                    description=description,
                    image=image,
                    revenue=revenue,
                    founder=founder,
                    company_name = company_name,
                    financial_graph = financial_data,
                    investment_round=investment_round,
                    yearwise_revenue=yearwise_revenue,  # Save the JSON data
                    yearwise_growth=yearwise_growth,    # Save the JSON data
                    digital_marketing=digital_marketing  # Save the JSON data
                )
                company.save()

                return redirect('/invest/')
            except json.JSONDecodeError:
                return render(request, 'add_company.html', {'error': 'Invalid JSON file'})
            except Exception as e:
                return render(request, 'add_company.html', {'error': str(e)})
    
    return render(request, 'add_company.html')


def pitch(request):
    if request.method =="POST":
        username = request.POST.get('username')

        return render(request, 'pitch.html', {'username': username})
    
    return redirect('/invest/')


@login_required
def create_message(request):
    if request.method == 'POST':
        to_username = request.POST.get('to')
        message_content = request.POST.get('letter')

        try:
            to_user = User.objects.get(username=to_username)
            message = Message.objects.create(
                to_user=to_user,
                from_user=request.user,
                message=message_content
            )
            message.save()  # Save the message object
            return redirect('/invest/')
        except User.DoesNotExist:
            return JsonResponse({'error': 'Recipient user does not exist'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=405)