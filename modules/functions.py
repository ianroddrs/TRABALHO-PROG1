import sqlite3

from flet import Text, AlertDialog
# Criação banco de dados

def create_DB():
    conexao = sqlite3.connect('usuarios.db')
    conexao = sqlite3.connect('usuarios.db')
    c = conexao.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_cadastro(
    c.execute('''CREATE TABLE user_cadastro (
            username text,
            email text,
            senha text
@@ -13,59 +14,95 @@ def create_DB():
    conexao.commit()
    conexao.close()

# Importação das variáveis

def init(c, p):
    global components, page
    components = c
    page = p

# Cadastro de usuário
def verificar_email():
        emails_cadastrados = []
        conexao = sqlite3.connect('usuarios.db')
        c = conexao.cursor()
        c.execute("SELECT email from user_cadastro")
        email_bd = c.fetchall()
        for i in email_bd:
            emails_cadastrados.append(i[0])
        conexao.commit()
        conexao.close()
        return emails_cadastrados
def verificar_user():
        users_cadastrados = []
        conexao = sqlite3.connect('usuarios.db')
        c = conexao.cursor()
        c.execute("SELECT username from user_cadastro")
        users_bd = c.fetchall()
        for i in users_bd:
            users_cadastrados.append(i[0])
        conexao.commit()
        conexao.close()
        return users_cadastrados
def cadastrar_usuario(e):
        cadastro = {
            'username': components['username'].current.value,
            'email':  components['email'].current.value,
            'senha':  components['senha'].current.value
        }
        conexao = sqlite3.connect('usuarios.db')

        c = conexao.cursor()

        c.execute(" INSERT INTO user_cadastro VALUES(:username, :email, :senha)",
            {
                'username':cadastro['username'],
                'email':cadastro['email'],
                'senha':cadastro['senha']
            }
        )
        conexao.commit()
        conexao.close()



#  Login de usuário
        if cadastro['username'] in verificar_user() and cadastro['email'] in verificar_email():
          dlg = AlertDialog(title=Text("username e email ja cadastrado no sistema"),on_dismiss=lambda e: print("Dialog dismissed!"))
          page.dialog = dlg
          dlg.open = True
          page.update()
        elif cadastro['username'] in verificar_user():
          dlg = AlertDialog(title=Text("username ja cadastrado no sistema"),on_dismiss=lambda e: print("Dialog dismissed!"))
          page.dialog = dlg
          dlg.open = True
          page.update()
        elif cadastro['email'] in verificar_email():
          dlg = AlertDialog(title=Text("email ja cadastrado no sistema"),on_dismiss=lambda e: print("Dialog dismissed!"))
          page.dialog = dlg
          dlg.open = True
          page.update()                    
        else:
            conexao = sqlite3.connect('usuarios.db')
            c = conexao.cursor()
            c.execute(" INSERT INTO user_cadastro VALUES(:username, :email, :senha)",
                {
                    'username':cadastro['username'],
                    'email':cadastro['email'],
                    'senha':cadastro['senha']
                }
            )
            conexao.commit()
            conexao.close()

def login_sistema(e):
        from flet import Text, AlertDialog
        '''
            Autenticar Login
        '''
        login = {
            'username': components['l_user'].current.value,
            'senha': components['l_senha'].current.value
        }
        conexao = sqlite3.connect('usuarios.db')      
        conexao = sqlite3.connect('usuarios.db')      

        c = conexao.cursor()
        c.execute("SELECT senha FROM user_cadastro WHERE username = '{}'".format(login['username']))
        senha_bd = c.fetchall()
        conexao.close()

        if login['senha'] == senha_bd[0][0]:
          dlg = AlertDialog(title=Text(f"Hello {login['username']}!"),on_dismiss=lambda e: print("Dialog dismissed!"))
          page.dialog = dlg
          dlg.open = True
          page.update()
        else: 
          dlg = AlertDialog(title=Text("Senha Incorreta!"), on_dismiss=lambda e: print("Dialog dismissed!"))
          page.dialog = dlg
          dlg.open = True
          page.update()
        try:
            c.execute("SELECT senha FROM user_cadastro WHERE username = '{}'".format(login['username']))
            senha_bd = c.fetchall()
            conexao.close()
            if login['senha'] == senha_bd[0][0]:
                dlg = AlertDialog(title=Text(f"Hello {login['username']}!"),on_dismiss=lambda e: print("Dialog dismissed!"))
                page.dialog = dlg
                dlg.open = True
                page.update()
            else: 
                dlg = AlertDialog(title=Text("Senha Incorreta!"), on_dismiss=lambda e: print("Dialog dismissed!"))
                page.dialog = dlg
                dlg.open = True
                page.update()
        except:
           dlg = AlertDialog(title=Text("Usuario não cadastrado"), on_dismiss=lambda e: print("Dialog dismissed!"))
           page.dialog = dlg
           dlg.open = True
           page.update()