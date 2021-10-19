from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome):
    return HttpResponse(f'<h1>hello {nome}</h1>')

def soma(request, num1, num2):
    return HttpResponse(f'<h1>A soma de {num1} e {num2} é igual a {num1 + num2}</h1>')

def mult(request, num1, num2):
    return HttpResponse(f'<h1>A multiplicação de {num1} e {num2} é igual a {num1 * num2}</h1>')

def sub(request, num1, num2):
    return HttpResponse(f'<h1>A subtracão de {num1} e {num2} é igual a {num1 - num2}</h1>')

def divi(request, num1, num2):
    return HttpResponse(f'<h1>A divisao de {num1} e {num2} é igual a {num1 / num2}</h1>')