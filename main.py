




dados  = {}



print('Cadastre-se:  ')


login = input('Login: ')
senha  = input('Senha: ') 


dados['login'] = login
dados['senha'] = senha  


print('dados cadastrados>>>', dados)




login_cad = input('Login: ')
senha_cad  = input('Senha: ') 


if login_cad == login and senha_cad == senha:
    print('Seja bem vindo  ao sistema Z')
    produtos = ['a','b','c']
    valores = [10.55,20.0,30.0]
else:
    print('Digite os dados corretamente...')    
    