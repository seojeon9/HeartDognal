from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def index(request):

    return render(request, 'accounts/index.html')

def about_us(request):

    return render(request, 'roaddog/about_us.html')

@csrf_exempt
def signup(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'accounts/signup.html', {'form': form})

    form = UserForm(request.POST)

    if form.is_valid():
        form.save()
        user_name = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=user_name, password=raw_password)
        auth_login(request, user)
        return redirect('/')

    print(form.errors)

    return render(request, 'accounts/signup.html', {'form': form})

def mypage(request):

    return render(request, 'accounts/mypage.html')

def user_info(request):

    return render(request, 'accounts/user_info.html')

def survey_info(request):

    return render(request, 'accounts/survey_info.html')

def inquiry(request):

    return render(request, 'accounts/inquiry.html')

def recommend(request):



    #1. 사용자가 전달한 별점 점수 가져오기
    #2. 별점점수를 군집화 모듈로 전송(함수호출)
    #3. 군집화모듈에서 군집레이블 결정후 몇번 레이블인지 반환
    #4. 반환된 레이블과 같은 군집의 강아지 정보를 파일이나 디비에서 얻어오기
    #5. 동일 군집 강아지 중 랜덤하게 선택
    #6. 디비에서 선택된 강아지 세부 정보 추출
    #7. 추출된 정보를 템플릿으로 전송

    return render(request, 'accounts/recommend.html')

def presurvey(request):

    return render(request, 'roaddog/presurvey.html')

def search(request):

    return render(request, 'roaddog/search.html')

def survey(request):

    return render(request, 'roaddog/survey.html')

def detail_info(request):
        # 선택된 강아지 아이디 얻어오기
        # 디비에서 해당 아이디 강아지 상세정보 가져오기
        # 유사도 테이블에서 선택된 강아지와 유사도가 놑은 강아지 아이디 찾기
        # 디비에서 유사도가 높은 강아지들 정보 얻어오기(10개) - 상세페이지 넘어가게
        # 템플릿에 강아지 정보 전송
    return render(request, 'roaddog/detail_info.html')




