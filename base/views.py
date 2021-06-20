from django.shortcuts import render

import string

# Enter Your Code
def removepunctuations(text):
    punctuations = string.punctuation
    edited_text = ''
    for char in text:
        if char not in punctuations:
            edited_text += char
    return edited_text

def wordcount(text):
    words = text.split()
    count = len(words)
    return count

def capitalize(text):
    return text.title()

def uppercase(text):
    return text.upper()

def lowercase(text):
    return text.lower()

def trimwhitespace(text):
    return text.strip()

def newlineremove(text):
    edited_text= ''
    for char in text:
        if char != '\n' and char!='\r':
            edited_text += char
    return edited_text

def spaceremove(text):
    return " ".join(text.split())

def index(request):
    if request.POST:
        content = request.POST['content']
        action = request.POST['action']
        word_count = False
        if action == 'punctuation':
            edited_content = removepunctuations(content)
        elif action == 'wordcount':
            edited_content = content
            word_count = wordcount(content)
        elif action == 'capitalize':
            edited_content = capitalize(content)
        elif action == 'upper':
            edited_content = uppercase(content)
        elif action == 'lower':
            edited_content = lowercase(content)
        elif action == 'trim':
            edited_content = trimwhitespace(content)
        elif action == 'lineremove':
            edited_content = newlineremove(content)
        elif action =='extraspace':
            edited_content = spaceremove(content)
        
        context = {
            'edited_content' :edited_content,
            'word_count':word_count
        }
        return render(request,'base/index.html', context)
    return render(request, 'base/index.html')
