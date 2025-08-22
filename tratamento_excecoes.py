# Autor: Issufo Gulamo
# Laborat�rio de Tratamento de Erros

nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()
        print("\n?? Conte�do do arquivo:\n")
        print(conteudo)

except FileNotFoundError:
    print("? Erro: o arquivo n�o foi encontrado.")
except PermissionError:
    print("? Erro: voc� n�o tem permiss�o para ler este arquivo.")
except Exception as e:
    print(f"?? Ocorreu um erro inesperado: {e}")
