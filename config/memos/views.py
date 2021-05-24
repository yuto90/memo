from django.shortcuts import render
from .models import Memo

# Create your views here.


def index(request):
    memos = Memo.objects.order_by('-created_datetime')
    return render(request, 'memos/index.html', {'memos': memos})
