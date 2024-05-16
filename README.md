
mkdir projeto
cd projeto
python -m venv cliente1
cd cliente1
cd Scripts
activate
cd..
cd..
pip install django
django-admin startproject app .
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser

python manage.py startapp core
Adicione o aplicativo ao arquivo 
app\settings.py 
INSTALLED_APPS = 'core'

LANGUAGE_CODE = 'pt-br' # Idioma Pt Br

TIME_ZONE = 'America/Sao_Paulo' # Timezone Brasil

Crie a rota  para o core.urls no arquivo /app/urls.py

Tabela do Banco de Dados
core/models.py

Crie o arquivo core/urls.py

Arquivos alterados:
core/
urls.py
views.py

Crie os arquivos 
/core/templates/
index.html
update.html

Compila o conteúdo do models.py e gera a migração
python manage.py makemigrations

Aplica a migração gerada ao banco de dados
python manage.py migrate
