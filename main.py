from src.models.cliente import Cliente
from src.models.equipamento import Equipamento
from src.repositories import cliente_repository
from src.repositories import equipamento_repository


def menu():
    print("\n*** TechService - Gestão de Assistência Técnica ***")
    print()
    print("=== Clientes ===")
    print("1. Listar clientes")
    print("2. Inserir cliente")
    print("3. Procurar cliente por ID")
    print("4. Atualizar cliente")
    print("5. Remover cliente")
    print()
    print("=== Equipamentos ===")
    print("6. Listar equipamentos")
    print("7. Inserir equipamento")
    print("8. Procurar equipamento por ID")
    print("9. Atualizar equipamento")
    print("10. Remover equipamento")
    print()
    print("0. Sair")

# Clientes
def opcao_listar_clientes():
    clientes = cliente_repository.listar()

    if not clientes:
        print("\nNão há clientes ativos na base de dados.")
        return

    print(f"\n{len(clientes)} cliente(s) ativo(s):")
    for item in clientes:
        print(item["id_cliente"], "-", item["nome"], "-", item["email"], "-", item["telefone"])


def opcao_inserir_cliente():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email (opcional): ") or None
    nif = input("NIF (opcional): ") or None

    cliente = Cliente(nome=nome, telefone=telefone, email=email, nif=nif)
    cliente = cliente_repository.inserir(cliente)

    print("Cliente inserido com sucesso. ID:", cliente.id_cliente)


def opcao_procurar_cliente():
    id_cliente = input("ID do cliente: ")
    cliente = cliente_repository.procurar_por_id(id_cliente)

    if cliente is None:
        print("Cliente não encontrado.")
        return

    cliente.mostrar()


def opcao_atualizar_cliente():
    id_cliente = input("ID do cliente a atualizar: ")
    cliente = cliente_repository.procurar_por_id(id_cliente)

    if cliente is None:
        print("Cliente não encontrado.")
        return

    novo_telefone = input(f"Novo telefone (atual: {cliente.telefone}, Enter para manter): ")
    novo_email = input(f"Novo email (atual: {cliente.email}, Enter para manter): ")

    if novo_telefone:
        cliente.telefone = novo_telefone
    if novo_email:
        cliente.email = novo_email

    cliente_repository.atualizar(cliente)
    print("Cliente atualizado com sucesso.")


def opcao_remover_cliente():
    id_cliente = input("ID do cliente a remover: ")
    cliente_repository.remover(id_cliente)
    print("Cliente removido com sucesso.")

# Equipamentos
def opcao_listar_equipamentos():
    equipamentos = equipamento_repository.listar()

    if not equipamentos:
        print("\nNão há equipamentos ativos na base de dados.")
        return

    print(f"\n{len(equipamentos)} equipamento(s) ativo(s):")
    for item in equipamentos:
        print(item["id_equipamento"], "- Cliente", item["id_cliente"], "-",
              item["tipo"], item["marca"], item["modelo"], "- Série:", item["numero_serie"])


def opcao_inserir_equipamento():
    id_cliente = input("ID do cliente dono do equipamento: ")

    cliente = cliente_repository.procurar_por_id(id_cliente)
    if cliente is None:
        print("Esse cliente não existe. Cria o cliente primeiro.")
        return

    tipo = input("Tipo (ex: Notebook, Impressora): ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    numero_serie = input("Número de série: ")
    observacoes = input("Observações (opcional): ") or None

    equipamento = Equipamento(id_cliente=id_cliente, tipo=tipo, marca=marca,
                               modelo=modelo, numero_serie=numero_serie,
                               observacoes=observacoes)
    equipamento = equipamento_repository.inserir(equipamento)

    print("Equipamento inserido com sucesso. ID:", equipamento.id_equipamento)


def opcao_procurar_equipamento():
    id_equipamento = input("ID do equipamento: ")
    equipamento = equipamento_repository.procurar_por_id(id_equipamento)

    if equipamento is None:
        print("Equipamento não encontrado.")
        return

    equipamento.mostrar()


def opcao_atualizar_equipamento():
    id_equipamento = input("ID do equipamento a atualizar: ")
    equipamento = equipamento_repository.procurar_por_id(id_equipamento)

    if equipamento is None:
        print("Equipamento não encontrado.")
        return

    novas_observacoes = input(
        f"Novas observações (atual: {equipamento.observacoes}, Enter para manter): "
    )

    if novas_observacoes:
        equipamento.observacoes = novas_observacoes

    equipamento_repository.atualizar(equipamento)
    print("Equipamento atualizado com sucesso.")


def opcao_remover_equipamento():
    id_equipamento = input("ID do equipamento a remover: ")
    equipamento_repository.remover(id_equipamento)
    print("Equipamento removido com sucesso.")

# Menu principal
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            opcao_listar_clientes()
        elif opcao == "2":
            opcao_inserir_cliente()
        elif opcao == "3":
            opcao_procurar_cliente()
        elif opcao == "4":
            opcao_atualizar_cliente()
        elif opcao == "5":
            opcao_remover_cliente()
        elif opcao == "6":
            opcao_listar_equipamentos()
        elif opcao == "7":
            opcao_inserir_equipamento()
        elif opcao == "8":
            opcao_procurar_equipamento()
        elif opcao == "9":
            opcao_atualizar_equipamento()
        elif opcao == "10":
            opcao_remover_equipamento()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()