from django.forms import ModelForm
from .models import Memo


class MemoForm(ModelForm):
    class Meta:
        # Memoモデルに対応したフォームを作成
        model = Memo
        # 表示する入力欄を定義
        fields = ['title', 'text']
