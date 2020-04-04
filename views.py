from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from fastai.text import * 

#set path to local folder
path = Path('.')
learner = load_learner(path,'classifier.pkl')

def index(request):
    return HttpResponse("hello")

@api_view(['POST'])
def process_and_respond(request):
    #message = request.data['text']
    user_input = request.data['text']
    (judgement,_,tensors) = learner.predict(user_input)
    probability = "{:.2f}".format(torch.max(tensors).item()*100)
    message = "Judgement: " + judgement.obj
    return Response(data=message, status=status.HTTP_200_OK)
