from src.models.cliente import Cliente
from src.repositories.cliente_repository import inserir, procurar_por_id, listar, atualizar, remover


def menu():
    print("\n*** TechService - Gestão de Clientes ***")
    print("1. Listar clientes")
    print("2. Inserir cliente")
    print("3. Procurar cliente por ID")
    print("4. Atualizar cliente")
    print("5. Remover cliente")
    print("0. Sair")


def opcao_listar():
    clientes = listar()

    if not clientes:
        print("\nNão há clientes ativos na base de dados.")
        return

    print(f"\n{len(clientes)} cliente(s) ativo(s):")
    for item in clientes:
        print(item["id_cliente"], "-", item["nome"], "-", item["email"], "-", item["telefone"])


def opcao_inserir():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email (opcional): ") or None
    nif = input("NIF (opcional): ") or None

    cliente = Cliente(nome=nome, telefone=telefone, email=email, nif=nif)
    cliente = inserir(cliente)

    print("Cliente inserido com sucesso. ID:", cliente.id_cliente)


def opcao_procurar():
    id_cliente = input("ID do cliente: ")
    cliente = procurar_por_id(id_cliente)

    if cliente is None:
        print("Cliente não encontrado.")
        return

    cliente.mostrar()


def opcao_atualizar():
    id_cliente = input("ID do cliente a atualizar: ")
    cliente = procurar_por_id(id_cliente)

    if cliente is None:
        print("Cliente não encontrado.")
        return

    novo_telefone = input(f"Novo telefone (atual: {cliente.telefone}, Enter para manter): ")
    novo_email = input(f"Novo email (atual: {cliente.email}, Enter para manter): ")

    if novo_telefone:
        cliente.telefone = novo_telefone
    if novo_email:
        cliente.email = novo_email

    atualizar(cliente)
    print("Cliente atualizado com sucesso.")


def opcao_remover():
    id_cliente = input("ID do cliente a remover: ")
    remover(id_cliente)
    print("Cliente removido com sucesso.")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            opcao_listar()
        elif opcao == "2":
            opcao_inserir()
        elif opcao == "3":
            opcao_procurar()
        elif opcao == "4":
            opcao_atualizar()
        elif opcao == "5":
            opcao_remover()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()