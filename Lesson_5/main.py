import Contato
from controle_contatos import ControleContatos

def main():
    controle = ControleContatos()

    while True:
        print("\n=== AGENDA DE CONTATOS ===")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Buscar Contato")
        print("4. Remover Contato")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            print("\n--- Novo Contato ---")
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            email = input("E-mail: ")
            telefone = input("Telefone: ")
            
            if nome and email:
                novo_contato = Contato(nome, sobrenome, email, telefone)
                controle.adicionar(novo_contato)
            else:
                print("Erro: Nome e e-mail são obrigatórios.")

        elif opcao == "2":
            print("\n--- Lista de Contatos ---")
            contatos = controle.listar()
            if not contatos:
                print("Nenhum contato cadastrado.")
            else:
                for i, c in enumerate(contatos, 1):
                    print(f"{i}. {c}")

        elif opcao == "3":
            termo = input("\nDigite parte do nome ou e-mail para buscar: ").strip()
            resultados = controle.buscar(termo)
            if not resultados:
                print("Nenhum contato encontrado.")
            else:
                print(f"\n--- Resultados ({len(resultados)}) ---")
                for c in resultados:
                    print(c)

        elif opcao == "4":
            email = input("\nDigite o e-mail exato do contato que deseja remover: ").strip()
            controle.remover(email)

        elif opcao == "5":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida! Escolha um número entre 1 e 5.")

if __name__ == "__main__":
    main()