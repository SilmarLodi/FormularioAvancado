from validacoes import validar_email, validar_cpf, validar_telefone, validar_data
from utils import salvar_dados, exibir_cadastros, exportar_para_csv

def coletar_dados():
    nome = input("Digite seu nome: ").strip()
    email = input("Digite seu email: ").strip()
    while not validar_email(email):
        print("Email inválido! Tente novamente.")
        email = input("Digite seu email: ").strip()
    
    telefone = input("Digite seu telefone: ").strip()
    while not validar_telefone(telefone):
        print("Telefone inválido! Tente novamente.")
        telefone = input("Digite seu telefone: ").strip()

    cpf = input("Digite seu CPF: ").strip()
    while not validar_cpf(cpf):
        print("CPF inválido! Certifique-se de inserir 11 dígitos numéricos.")
        cpf = input("Digite seu CPF (apenas números): ").strip()

    data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ").strip()
    while not validar_data(data_nascimento):
        print("Data inválida! Use o formato DD/MM/AAAA.")
        data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ").strip()

    return {
        "Nome": nome,
        "Email": email,
        "Telefone": telefone,
        "CPF": cpf,
        "Data de Nascimento": data_nascimento
    }

def menu():
    while True:
        print("\nMenu:")
        print("1. Preencher Formulário")
        print("2. Exibir Cadastros")
        print("3. Exportar para CSV")
        print("4. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            dados = coletar_dados()
            if salvar_dados(dados):
                print("Dados salvos com sucesso!")
        elif opcao == "2":
            exibir_cadastros()
        elif opcao == "3":
            exportar_para_csv()
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
