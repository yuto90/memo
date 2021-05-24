from django.shortcuts import render
from .models import Memo

# Create your views here.


def index(request):
    # メモのクエリセットを全て降順に取得
    memos = Memo.objects.order_by('-created_datetime')
    return render(request, 'memos/index.html', {'memos': memos})


def detail(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    return render(request, 'memos/detail.html', {'memo': memo})
