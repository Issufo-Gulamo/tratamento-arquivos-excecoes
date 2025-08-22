# Autor: Issufo Gulamo
# Desafio de Leitura e Grava��o de Arquivos

try:
    with open("entrada.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()

    # exemplo de modifica��o: deixar todo o texto em mai�sculas
    conteudo_modificado = conteudo.upper()

    with open("saida.txt", "w", encoding="utf-8") as f:
        f.write(conteudo_modificado)

    print("? Arquivo processado e salvo como 'saida.txt'.")

except FileNotFoundError:
    print("? O arquivo 'entrada.txt' n�o foi encontrado.")
