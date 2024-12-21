import csv

def salvar_dados(dados):
    try:
        with open("cadastros.txt", "a") as arquivo:
            for chave, valor in dados.items():
                arquivo.write(f"{chave}: {valor}\n")
            arquivo.write("-" * 30 + "\n")
        return True
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")
        return False

def exibir_cadastros():
    try:
        with open("cadastros.txt", "r") as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Nenhum cadastro encontrado.")

def exportar_para_csv():
    try:
        with open("cadastros.txt", "r") as arquivo_txt, open("cadastros.csv", "w", newline="") as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(["Nome", "Email", "Telefone", "CPF", "Data de Nascimento"])  # Cabeçalhos
            dados = []
            for linha in arquivo_txt:
                if linha.strip():
                    dados.append(linha.split(":")[1].strip())
                if len(dados) == 5:  # Assumindo 5 campos
                    writer.writerow(dados)
                    dados = []
        print("Dados exportados para cadastros.csv com sucesso!")
    except Exception as e:
        print(f"Erro ao exportar dados: {e}")
        
def editar_cadastro():
    try:
        with open("cadastros.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        print("\nCadastros existentes:")
        for i, linha in enumerate(linhas):
            if "Nome:" in linha:
                print(f"{i // 6 + 1}. {linha.strip()}")

        escolha = int(input("\nDigite o número do cadastro que deseja editar: ")) - 1
        registro_inicio = escolha * 6

        novo_nome = input("Novo nome (ou Enter para manter o atual): ").strip()
        novo_email = input("Novo email (ou Enter para manter o atual): ").strip()
        novo_telefone = input("Novo telefone (ou Enter para manter o atual): ").strip()

        if novo_nome:
            linhas[registro_inicio] = f"Nome: {novo_nome}\n"
        if novo_email:
            linhas[registro_inicio + 1] = f"Email: {novo_email}\n"
        if novo_telefone:
            linhas[registro_inicio + 2] = f"Telefone: {novo_telefone}\n"

        with open("cadastros.txt", "w") as arquivo:
            arquivo.writelines(linhas)

        print("Cadastro atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao editar cadastro: {e}")

def excluir_cadastro():
    try:
        with open("cadastros.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        print("\nCadastros existentes:")
        for i, linha in enumerate(linhas):
            if "Nome:" in linha:
                print(f"{i // 6 + 1}. {linha.strip()}")

        escolha = int(input("\nDigite o número do cadastro que deseja excluir: ")) - 1
        registro_inicio = escolha * 6

        del linhas[registro_inicio:registro_inicio + 6]

        with open("cadastros.txt", "w") as arquivo:
            arquivo.writelines(linhas)

        print("Cadastro excluído com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir cadastro: {e}")
