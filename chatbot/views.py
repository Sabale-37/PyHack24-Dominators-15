from django.shortcuts import render
from .gemini_utility import load_gemini_pro_model , gemini_pro_vision_response
from .models import ChatMessage
from PIL import Image
from io import BytesIO



# Load Gemini-Pro model
model = load_gemini_pro_model()
chat_session = model.start_chat(history=[])

def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        
        # Send user's message to Gemini-Pro and get the response
        gemini_response = chat_session.send_message(user_message)

        # Save user message and Gemini response to database with logged-in user
        if request.user.is_authenticated:
            ChatMessage.objects.create(user=request.user, user_message=user_message, gemini_response=gemini_response.text)
        
            # Retrieve all messages from database
            all_messages = ChatMessage.objects.filter(user=request.user)

            return render(request, 'chatbot/index.html',{ 'all_messages':all_messages})

        
        return render(request, 'chatbot/index.html', {'user_message': user_message, 'gemini_response': gemini_response.text })
    else:
        if request.user.is_authenticated:
            all_messages = ChatMessage.objects.filter(user=request.user)
        
            return render(request, 'chatbot/index.html',{'all_messages':all_messages })

        return render(request, 'chatbot/index.html')
    


   
def image_captioning(request):
    if request.method == 'POST':
        prompt = 'Write a short caption for this image'
        # image_file = Image.open(r'C:\Users\Dell\Desktop\Django\AIBot\chatbot\static\images\robo.jpg')
        image_file = request.FILES['image']
        print(Image.open(image_file))
       
        # Call the gemini_pro_vision_response function with the prompt and image bytes
        caption = gemini_pro_vision_response(prompt, Image.open(image_file))

        return render(request, 'chatbot/image-captioning.html', {'caption': caption})
    else:
        return render(request, 'chatbot/image-captioning.html')