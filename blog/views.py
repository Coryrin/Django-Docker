from django.shortcuts import render

def index(request):
    return {
        "test": "hello, world"
    }
