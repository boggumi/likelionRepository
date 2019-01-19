from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

    # render 함수는 세개 받을 수 있음 (request 객체, 템플릿 이름, 사전형객체(dctionary 자료형))
def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    # 어떻게 표현되는지 우리강 입력한 값들이
    # text란 변수에 입력한 원문전체가 문자열로서 담김
    words = text.split
    # split = 많은 글 중에서 공백을 기준으로 단어들을 잘라서 리스트로 만드는 함수
    word_dictionary = {} #여기에는 단어: 몇번 단어: 몇번 이런식으로 저장이 되어있음
    
    for word in words:
        if word in word_dictionary:
            # increases
            word_dictionary[word]+=1
        else:
            # add to word_dictionary
            word_dictionary[word]=1

    return render(request, 'result.html', {'full': text, 'total':len(words), 'dictionary' : word_dictionary.items()})

    # 사전형 객체 왼편에는 key값(원문전체라는 의미에서 full이란 이름 붙여줌) / 오른쪽에는 value값
    #  items() = 쌍들을 넘겨줌