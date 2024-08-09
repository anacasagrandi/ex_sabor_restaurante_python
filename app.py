#import da biblioteca os 
import os

#lista de dicionário representando os restaurantes
restaurantes = [{'nome':'Praça', 'categoria': 'Japonesa','ativo': False},
               {'nome':'Pizza', 'categoria': 'Pizza','ativo': True}, 
               {'nome':'Cantina', 'categoria': 'Italiano','ativo': False}]

def exibir_nome_do_programa():
    print("""
          Sᴀʙoʀ ᴇxᴘʀᴇss 
          """) 

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app\n')

    def voltar_ao_menu_principal():
        input('\nDigite uma tecla para voltar ao menu principal')
        main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls') # limpa a tela (funfa so no windows)
    linha = '*' (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def main():
    """
    Função principal que inicia o programa
    """
    os.system('cls') 
    exibir_nome_do_programa()
    exibir_opcoes()
    # escolher_opcao()

if __name__ == '__main__':
    main()
