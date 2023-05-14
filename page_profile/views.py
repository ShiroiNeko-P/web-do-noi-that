from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def register(request):
    form = RegistrationForm()
    # Nếu bấm nút đăng kí sẽ đưa dữ liệu vào 
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # gọi các hàm ở forms.py nếu hợp lệ
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'register.html', {'form': form})