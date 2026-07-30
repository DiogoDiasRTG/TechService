from src.repositories.cliente_repository import listar


def main():
    print("=== TechService - Sistema de Gestão de Assistência Técnica ===")

    print("\nClientes ativos:")

    clientes = listar()

    for item in clientes:
        print(
            item["id_cliente"],
            item["nome"],
            item["email"],
            item["telefone"]
        )


if __name__ == "__main__":
    main()