from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .forms import CadastroUsuarioForm

# Create your views here.

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/login/#')
        else:
            messages.success(request,"Usuário ou senha inválido! Tente novamente.")
    return redirect('/login/')


def cadastrar_user(request):
    if request.method == "POST":
        form_usuario = CadastroUsuarioForm(request.POST)
        if form_usuario.is_valid():
            try:
                criar_usuario(request, form_usuario)
                messages.success(request, 'Usuário cadastrado com sucesso.')
                return redirect('login.html')
            except ValidationError as e:
                form_usuario.add_error(None, e)
        else:
            messages.error(request, 'O formulário contém dados inválidos!')
    else:
        form_usuario = CadastroUsuarioForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})


def check_email(request, form_usuario):
    email = form_usuario.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
        msg = 'O e-mail informado já foi cadastrado!'
        messages.error(request, msg)
        form_usuario.add_error('email', msg)
        raise ValidationError("Email já existe!")

def criar_usuario(request, form_usuario):
    usuario = form_usuario.save(commit=False)

    # check_username(request, form_usuario)

    check_email(request, form_usuario)

    usuario.save()

   

