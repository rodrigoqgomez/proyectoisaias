from django.shortcuts import render,HttpResponse
from openai import OpenAI
import openai
import os
from django.conf import settings

# Create your views here.


client = OpenAI()




def home(request):
  chatbot_response = None

  if request.method =='POST':
    user_input = request.POST.get("user_input")

    response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "eres el mejor guia turistico y me diras donde es,un resumen de los atractivos turisticos ,fechas para visitar y sí es un destino ficticio da curiosidades de esta y si no da la informacion como real"},
    {"role": "user", "content": user_input}
  ]
)

    print(response.choices[0].message)


    
    return   render(request,'main.html',{'response':response.choices[0].message.content})
  
  return render(request, 'main.html', {'response': ""})
