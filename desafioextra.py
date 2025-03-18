def menu(): # Def pode buscar códigos que podem ser reutilizados
 print("1-padrão\n2-Personalizado\n3-Agradecimento \n4-Sair")
def main():
    while True: # Laço de repetição, se a condição for verdadeira continuará lendo o código
        menu() # Chama a função menu para mostrar as opções
        escolha=input("Escolha:")
        if escolha =='1':
            print("oi, esta msg é padrão")
        elif escolha =='2':
            print(input(" msg personalizada"))
        elif escolha == '3':
            print("Obrigada por avisar")
        elif escolha == '4': #Verificar condicões adicionais após a instrução
            break # 
        else: # Else captura todas as entradas que não correspodem às opções válidas
            print("opção inválida.")
if __name__=="__main__":
 main()

 import pyautogui
 def msg():
    print('1 - Bom dia!')
    print('2- Boa tarde!')
    print('3 - ')