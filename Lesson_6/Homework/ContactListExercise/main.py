from Contact import ControleContatos
from Contact_list import Contato

def main():
    # Instancia o controlador (ele gerencia o arquivo contatos.json automaticamente)
    controle = ControleContatos()

    while True:
        print("\n=== AGENDA DE CONTATOS (JSON) ===")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Buscar Contato")
        print("4. Remover Contato")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            print("\n--- Novo Contato ---")
            nome = input("Nome: ").strip()
            sobrenome = input("Sobrenome: ").strip()
            email = input("E-mail: ").strip()
            telefone = input("Telefone: ").strip()
            
            if nome and email:
                novo_contato = Contato(nome, sobrenome, email, telefone)
                controle.adicionar(novo_contato)
            else:
                print("Erro: Nome e e-mail são obrigatórios para cadastrar um contato.")

        elif opcao == "2":
            print("\n--- Lista de Contatos Cadastrados ---")
            contatos = controle.listar()
            if not contatos:
                print("Nenhum contato encontrado na agenda.")
            else:
                for i, c in enumerate(contatos, 1):
                    print(f"{i}. {c}")

        elif opcao == "3":
            termo = input("\nDigite parte do nome, sobrenome ou e-mail para buscar: ").strip()
            resultados = controle.buscar(termo)
            if not resultados:
                print("Nenhum contato corresponde à busca.")
            else:
                print(f"\n--- Resultados Encontrados ({len(resultados)}) ---")
                for c in resultados:
                    print(f"- {c}")

        elif opcao == "4":
            email = input("\nDigite o e-mail exato do contato que deseja remover: ").strip()
            if email:
                controle.remover(email)
            else:
                print("Erro: O e-mail não pode estar vazio.")

        elif opcao == "5":
            print("Saindo da agenda de contatos. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha um número entre 1 e 5.")

if __name__ == "__main__":
    main()