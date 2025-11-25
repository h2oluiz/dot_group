### Questão 1:

**criar virtual environment**

> python3 -m venv .env

> source .env/bin/activate

**Download do projeto**
> git clone https://github.com/h2oluiz/dot_group.git
> 
> cd teste/teste_dot

**instalar requirements**
> pip install -r requirements.txt

**criar banco de dados**
> python manage.py migrate

**roda dataload**
> python manage.py gera_livros

**roda projeto**
> python manage.py runserver

**documentacao api**
http://localhost:8000 - swagger doc

**executar testes **
> python manage.py test
> coverage run --source='.' manage.py test -v 2 && coverage report

### Questões 2: 
>Notebook questao_2.ipynb

### Questões 3:
>Notebook questao_3.ipynb








