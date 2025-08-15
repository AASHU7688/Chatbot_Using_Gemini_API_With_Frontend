

# Create your views here.
from django.shortcuts import render
from google.generativeai import configure, GenerativeModel

# Configure Gemini API
configure(api_key="AIzaSyAsskJ6QKtwVlTVw3Von1IWMkGuzzCVw4k")  # Replace with your key
model = GenerativeModel('gemini-1.5-flash')

# Store chat history in memory (use DB later for persistence)
chat_history = []

def chat_view(request):
    global chat_history

    if request.method == "POST":
        question = request.POST.get("question")
        response = model.generate_content(question)
        answer = response.text

        # Save to history
        chat_history.append({'user': question, 'bot': answer})

    return render(request, 'chatbot/chat.html', {'chat_history': chat_history})
