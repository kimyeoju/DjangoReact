from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "회원가입 환영합니다.")
            # '/' -> url pattern name을 적어도됨
            next_url = request.GET.get('next', '/')
            return redirect("next_url")
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
        'form': form,
    })