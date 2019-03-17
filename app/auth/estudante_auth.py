from django.contrib.auth.hashers import make_password, check_password
from app.models import Estudante

def logout(request):
    if request.session.get("estudante_id") is not None:
        del request.session["estudante_id"]

def initSession(request, estudante):
	request.session["estudante_id"] = estudante.id

def get(request):
    if request.session.get("estudante_id") is not None:
        id = request.session.get("estudante_id")
        if isinstance(id, int):
            try:
                return Estudante.objects.get(pk=int(id))
            except Estudante.DoesNotExist:
                pass

    return None
    
def login(request, email, senha):
	try:
		estudante = Estudante.objects.get(email=email)

		if(check_password(senha, estudante.senha)):
			initSession(request, estudante)
			return True
	except Estudante.DoesNotExist:
			pass

	return False

  