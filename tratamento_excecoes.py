# Autor: Issufo Gulamo
# Laboratório de Tratamento de Erros

nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()
        print("\n?? Conteúdo do arquivo:\n")
        print(conteudo)

except FileNotFoundError:
    print("? Erro: o arquivo não foi encontrado.")
except PermissionError:
    print("? Erro: você não tem permissão para ler este arquivo.")
except Exception as e:
    print(f"?? Ocorreu um erro inesperado: {e}")
