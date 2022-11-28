import random
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from testsite.models import *


def index(request):
    question = Questions.objects.all()
    key_i = []
    voprosy = {}
    i = 0
    while i < 9:
        keys = random.randint(0,8)
        keyz = str(keys)
        
        if keyz not in key_i:
            key_i.append(keyz)
            i += 1
        else: 
            continue

    for item in key_i:
        question = Questions.objects.filter(question_number = item)           
        voprosy[item] = question       
        
    print(key_i)
    print(voprosy)

    return render(request, 'testsite/questions_list.html', {'questions': voprosy })
                
   
           
    
        



# class HomeTests(ListView):
#     model = Questions
#     template_name = 'testsite/questions_list.html'
#     context_object_name = 'testsite'
    # paginate_by = 1
    #extra_context = { 'title': 'Главная' } 
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Главная страница'
    #     context['mixin_prop'] = self.get_prop()
    #     return context
    
    # def get_queryset(self):
    #     a = 1
    #     a = 10 * random.random()
    #     return Questions.objects.get(pk=1)
    #     return Questions.objects.select_related('question')


# class ChoiceView(ListView):
#     model = Choice
#     template_name = 'testsite/questions_list.html'
#     context_object_name = 'choice'
    
    # def get_queryset(self):
    #     # a = 1
    #     # a = 10 * random.random()
    #     # return Questions.objects.get(pk=1)
    #     return Choice.objects.select_related('question')
