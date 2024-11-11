from sympy import symbols, Eq, solve, Rational, sqrt
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from sympy.core.sympify import SympifyError

def resolver_equacao_linear(equacao):
    try:
        # Definindo a variável simbólica
        x = symbols('x')
        transformations = (standard_transformations + (implicit_multiplication_application,))

        # Remover espaços em branco
        equacao = equacao.replace(' ', '')

        # Substituir 'raiz' por 'sqrt'
        equacao = equacao.replace('raiz', 'sqrt')

        # Dividir a equação nos lados
        lados = equacao.split('=')
        if len(lados) != 2:
            return "Equação inválida. Certifique-se de que há apenas um sinal de igual '='."

        lado_esquerdo, lado_direito = lados

        # Analisar as expressões, permitindo frações com Rational
        expr_esquerdo = parse_expr(lado_esquerdo, transformations=transformations, local_dict={'x': x, 'Rational': Rational})
        expr_direito = parse_expr(lado_direito, transformations=transformations, local_dict={'x': x, 'Rational': Rational})

        # Verificar se há variáveis diferentes de 'x'
        for var in expr_esquerdo.free_symbols.union(expr_direito.free_symbols):
            if var != x:
                return f"A equação deve conter apenas a variável 'x'. Variável inválida: {var}"

        # Criar a equação simbólica
        equacao_simbolica = Eq(expr_esquerdo, expr_direito)

        # Resolver a equação
        solucao = solve(equacao_simbolica, x)

        # Verificar a solução
        if not solucao:
            diferenca = expr_esquerdo - expr_direito
            if diferenca == 0:
                return "Infinitas soluções."
            else:
                return "Sem solução."
        else:
            valor = solucao[0]
            return f"A solução é x = {valor.simplify()}"

    except SympifyError as e:
        return f"Erro na interpretação da equação: {e}. Verifique a sintaxe."
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"

if __name__ == "__main__":
    equacao = input("Digite a equação do 1º grau (exemplo: 4x - 1 + x = 8x + 4 + 2x ou 2/3*x + raiz(5) = 3): ")
    resultado = resolver_equacao_linear(equacao)
    print(resultado)