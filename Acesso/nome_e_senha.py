import getpass

#1 Coletando os dados do usuário
usuario = input("\nDigite o nome de usuário: ").strip() #Remove espaços em branco
senha = getpass.getpass("""\n Digite a \n
█▀▀ █▀▀ █▀▀▄ █░░█ █▀▀█ 
▀▀█ █▀▀ █░░█ █▀▀█ █▄▄█ 
▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ▀░░▀:""")

#2 Verificando as credenciais
if usuario.lower() == "admin" and senha == "12345":
    print(f"\n Bem-vinda de volta,{usuario.title()}!")
    print("Mais um membro no jogo!")
elif usuario.lower() == "admin" and senha == "admin123":
    print(f"\n Modo Adiministrador ativado.Olá,{usuario.upper()}!")
else:
    print("""\n 
▄▀█ █▀▀ █▀▀ █▀ █▀ █▀█   █▄░█ █▀▀ █▀▀ ▄▀█ █▀▄ █▀█
█▀█ █▄▄ ██▄ ▄█ ▄█ █▄█   █░▀█ ██▄ █▄█ █▀█ █▄▀ █▄█.
         
 Nome de usuário ou senha incorretos.\n""")