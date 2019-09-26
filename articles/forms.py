from django import forms


# 사용자에게 입력받는 field 만 작성
class ArticleForm(forms.Form):
    title = forms.CharField(
        max_length=20,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '혜련이의 모든 것',
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'placeholder': '혜련이 얘기 하자!',
                'rows': 5,
                'cols': 50,
            }
        )
    )
