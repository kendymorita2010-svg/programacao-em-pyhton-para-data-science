# # pe =  input('Deseja acessar o banco? ')


# # while pe  == 'sim':
# #     senha  =  input('Senha')
# #     if senha  == '123':
# #         print('banco X')
# #         print('''Menu:
            
# #             1 - saque
# #             2 - deposito
# #             3 - extrato
# #             4 -  sair 
            
            
            
# #             ''')
# #         op =  input('escolha a operação: ')
# #         if  op == '1':
# #             pe =  input('Deseja acessar o banco? ')
# #             pass
# #     else:
# #         print('Deseja coninuar?')            


# saldo = 1000.00

# print("=== SISTEMA DE BANCO ===")

# senha = input("Digite sua senha: ")

# if senha == "1234":
#     print("\nAcesso autorizado!")

#     print("\n1 - Ver extrato")
#     print("2 - Fazer depósito")
#     print("3 - Fazer saque")
#     print("4 - Sair")

#     opcao = input("\nEscolha uma opção: ")

#     if opcao == "1":
#         print(f"Seu saldo é: R$ {saldo:.2f}")

#     elif opcao == "2":
#         deposito = float(input("Digite o valor do depósito: R$ "))
#         saldo = saldo + deposito
#         print(f"Depósito realizado!")
#         print(f"Novo saldo: R$ {saldo:.2f}")

#     elif opcao == "3":
#         saque = float(input("Digite o valor do saque: R$ "))

#         if saque <= saldo:
#             saldo = saldo - saque
#             print("Saque realizado!")
#             print(f"Novo saldo: R$ {saldo:.2f}")
#         else:
#             print("Saldo insuficiente!")

#     elif opcao == "4":
#         print("Obrigado por utilizar o sistema. Até logo!")

#     else:
#         print("Opção inválida!")

# else:
#     print("Senha incorreta! Acesso negado.")



