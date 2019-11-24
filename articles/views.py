from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm


# 모든 article 을 보여주는 페이지
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


# GET 으로 들어오면? 생성하는 페이지 rendering
# POST 로 들어오면? 생성하는 로직 수행
def create(request):
    if request.method == 'POST':
        # 사용자의 모든 입력 form 통해 받는다.
        form = ArticleForm(request.POST)
        # 처음 함수처럼 Raw Data 를 바로 꺼내는 것은 위험
        # title = request.POST.get('title') (위험)
        # content = request.POST.get('content') (위험)

        # 사용자가 입력한(보낸) 데이터가 유효한지 확인
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article(title=title, content=content)
            article.save()
            return redirect('articles:index')
        # form.is_valid() 가 False 인 경우
        # valid 하지 않은 값 들어있는 form 을 그대로 담아서 사용자에게 다시 보냄
        # 수정해서 다시 입력하라고!
        # else:
        #     context = {'form': form}
        #     return render(request, 'articles/create.html', context)

    else:  # GET 요청으로 들어왔을 때
        form = ArticleForm()

    # if ~ else~ 동시에 걸리게 indent 앞으로 조정
    context = {'form': form}
    return render(request, 'articles/create.html', context)


def detail(request, article_pk):  # variable routing 이라 두번째 인자 존재
    # 그 번호에 맞는 article 1개만 꺼내서 저장
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}  # 넘김
    return render(request, 'articles/detail.html', context)
