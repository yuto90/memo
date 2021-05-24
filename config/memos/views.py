from django.shortcuts import render, get_object_or_404, redirect
from .models import Memo
from .forms import MemoForm

# Create your views here.


def index(request):
    # メモのクエリセットを全て降順に取得
    memos = Memo.objects.order_by('-created_datetime')
    return render(request, 'memos/index.html', {'memos': memos})


def detail(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    return render(request, 'memos/detail.html', {'memo': memo})


def new(request):
    if request.method == "POST":
        # request.POSTの中にはフォームに入力した情報が含まれている
        # 情報をもとに新しいMemoインスタンスを生成する
        form = MemoForm(request.POST)
        if form.is_valid():
            # データベースに保存
            form.save()
            # redirect : urlパスを指定
            return redirect('memos:index')
    else:
        form = MemoForm
        return render(request, 'memos/new.html', {'form': form})
