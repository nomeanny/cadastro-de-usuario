# cadastro-de-usuario

## Estrutura do Código

## Lista de Cadastros:
cadastros = []: Inicializamos uma lista vazia para armazenar os cadastros dos usuários.

## Função cadastrar_usuario:
Recebe nome, idade e email como parâmetros.
Cria um dicionário usuario com essas informações.
Adiciona o dicionário à lista cadastros e imprime uma mensagem de sucesso.

## Função exibir_cadastros:
Verifica se a lista cadastros está vazia.
Se não estiver, itera sobre a lista e exibe as informações de cada usuário.

## Função main:
Controla o fluxo do programa com um loop que apresenta um menu.
Permite ao usuário escolher entre cadastrar um novo usuário, exibir os cadastros ou sair do programa.
Executa a ação correspondente com base na escolha do usuário.

## Execução do Programa:
O bloco if __name__ == "__main__": garante que a função main seja chamada ao executar o script.

## Resumo do Funcionamento
O usuário interage com um menu que permite cadastrar informações ou visualizar cadastros.
Os dados são armazenados em uma lista de dicionários, facilitando a manipulação e exibição.
O programa continua em execução até que o usuário escolha sair.
