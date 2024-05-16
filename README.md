<h4>Cria um diretório de nome projeto</h4>
<code>mkdir projeto</code><br/>

<h4>entra no diretório</h4>
<code>cd projeto</code><br/>

<h4>Cria um  virtual environments de nome cliente1</h4>
<code>python -m venv cliente1</code><br/>

<h4>Entra no diretório</h4>
<code>cd cliente1</code><br/>

<h4>Entra no diretório</h4>
<code>cd Scripts</code><br/>

<h4>Ativa o ambiente de nome cliente1</h4>
<code>activate</code><br/>

<h4>Volta no diretório</h4>
<code>cd..</code><br/>

<h4>Volta no diretório</h4>
<code>cd..</code><br/>

<h4>Instala o Django</h4>
<code>pip install django</code><br/>

<h4>Cria o projeto do Django em um diretório separado</h4>
<code>django-admin startproject app .</code><br/>

<h4>Cria um aplictivo de nome core</h4>
<code>python manage.py startapp core</code><br/>

<h4>Configurações do sistema</h4>
app\settings.py <br/>
INSTALLED_APPS = 'core' # Local onde os aplicativos são adicionados ao sistema<br/>
LANGUAGE_CODE = 'pt-br' # Idioma Pt Br<br/>
TIME_ZONE = 'America/Sao_Paulo' # Timezone Brasil<br/>

<h4>Crie a rota  para o core.urls no arquivo /app/urls.py</h4>

<h4>Tabela do Banco de Dados</h4>
core/models.py
<h4>Link para definições e modelos de tabela</h4>
<a href="https://docs.djangoproject.com/en/5.0/ref/forms/fields/">Link Django Fields</a>


<h4>Arquivo de rotas do aplicativo core</h4>
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

<h4>Cria o administrador para o banco de dados</h4>
<code>python manage.py createsuperuser</code><br/>

<h4>Roda o servidor</h4>
<code>python manage.py runserver</code><br/>
