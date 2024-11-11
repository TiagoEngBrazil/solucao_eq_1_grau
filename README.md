# Equação Linear Solver

Este projeto implementa um solucionador de equações lineares de primeiro grau em Python usando a biblioteca SymPy. O código permite inserir uma equação linear, processá-la e determinar a solução para a variável `x`.

## Funcionalidades

- Interpreta e resolve equações lineares de primeiro grau.
- Suporta operações matemáticas básicas, frações e raízes quadradas.
- Verifica a validade da equação e se contém apenas a variável `x`.
- Identifica equações sem solução ou com infinitas soluções.

## Requisitos

- Python 3.x
- Biblioteca SymPy

## Instalação

1. **Clone o repositório:**
    ```sh
    git clone https://github.com/seu-usuario/repositorio.git
    cd repositorio
    ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
    ```sh
    python -m venv env
    source env/bin/activate  # No Windows, use `env\Scripts\activate`
    ```

3. **Instale a biblioteca SymPy:**
    ```sh
    pip install sympy
    ```

## Uso

1. **Execute o script `equacao_linear_solver.py`:**
    ```sh
    python equacao_linear_solver.py
    ```

2. **Digite a equação linear quando solicitado:**
    ```sh
    Digite a equação do 1º grau (exemplo: 4x - 1 + x = 8x + 4 + 2x ou 2/3*x + raiz(5) = 3): 
    ```

3. **Aguarde a solução da equação:**
    - Se a equação for válida, a solução será exibida.
    - Se a equação for inválida ou tiver uma sintaxe incorreta, uma mensagem de erro será exibida.

## Exemplo

### Entrada:
```plaintext
4x - 1 + x = 8x + 4 + 2x
```

### Saída:
```plaintext
A solução é x = -5/7
```

## Estrutura do Código

- **Importações e Definições**:
    - Importa bibliotecas necessárias como `symbols`, `Eq`, `solve`, `Rational`, `sqrt`, `parse_expr`, e `SympifyError` do SymPy.
    - Define a função `resolver_equacao_linear(equacao)`.

- **Função `resolver_equacao_linear`**:
    - Define a variável simbólica `x`.
    - Remove espaços em branco da equação.
    - Substitui 'raiz' por `sqrt`.
    - Divide a equação nos lados esquerdo e direito.
    - Analisa as expressões matemáticas usando `parse_expr`.
    - Verifica se há variáveis diferentes de `x`.
    - Cria a equação simbólica com `Eq`.
    - Resolve a equação e retorna a solução ou uma mensagem de erro.

- **Execução do Script**:
    - Solicita ao usuário a entrada da equação linear.
    - Chama a função `resolver_equacao_linear` e imprime o resultado.

## Tratamento de Erros

- **SympifyError**:
    - Retorna uma mensagem de erro específica se houver problemas na interpretação da equação.
- **Outros Erros**:
    - Captura exceções gerais e retorna uma mensagem de erro genérica.

## Contribuição

1. Faça um fork do repositório.
2. Crie um branch para sua feature (`git checkout -b feature/AmazingFeature`).
3. Commit suas alterações (`git commit -m 'Add some AmazingFeature'`).
4. Push para o branch (`git push origin feature/AmazingFeature`).
5. Abra um Pull Request.
