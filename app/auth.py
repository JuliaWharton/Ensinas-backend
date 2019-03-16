from django.contrib.auth.hashers import make_password, check_password
from app.models import Estudante

def logout(request):
    request.session["estudante_id"] = None
    request.session["mentor_id"] = None    

def estudante_get(request):
    if request.session.get("estudante_id") is not None:
        id = request.session.get("estudante_id")
        if isinstance(id, int):
            id = int(id)
            try:
                estudante = Estudante.objects.get(pk=id)
                return estudante
            except Estudante.DoesNotExist:
                pass

    return None


def estudante_login(request, email, senha):
    try:
        estudante = Estudante.objects.get(email=email)

        if(check_password(senha, estudante.senha)):
            request.session["estudante_id"] = estudante.id
            return True
    except Estudante.DoesNotExist:
            pass

    return False
