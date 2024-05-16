
<code>mkdir projeto</code><br/>
<code>cd projeto</code><br/>
<code>python -m venv cliente1</code><br/>
<code>cd cliente1</code><br/>
<code>cd Scripts</code><br/>
<code>activate</code><br/>
<code>cd..</code><br/>
<code>cd..</code><br/>
<code>pip install django</code><br/>
<code>django-admin startproject app .</code><br/>
<code>python manage.py runserver</code><br/>
<code>python manage.py migrate</code><br/>
<code>python manage.py createsuperuser</code><br/>

<code>python manage.py startapp core</code><br/>
<h4>Adicione o aplicativo ao arquivo </h4>
app\settings.py <br/>
INSTALLED_APPS = 'core' # Local onde os aplicativos são adicionados ao sistema<br/>
LANGUAGE_CODE = 'pt-br' # Idioma Pt Br<br/>
TIME_ZONE = 'America/Sao_Paulo' # Timezone Brasil<br/>

<h4>Crie a rota  para o core.urls no arquivo /app/urls.py</h4>

<h4>Tabela do Banco de Dados</h4>
core/models.py

<h4>Crie o arquivo </h4>
core/urls.py

<h4>Arquivos alterados:</h4>
core/<br/>
urls.py<br/>
views.py<br/>

<h4>Crie os arquivos </h4>
/core/templates/<br/>
index.html<br/>
update.html

<h4>Compila o conteúdo do models.py e gera a migração</h4>
<br/><code>python manage.py makemigrations</code><br/>

<h4>Aplica a migração gerada ao banco de dados</h4>
<br/><code>python manage.py migrate</code><br/>
