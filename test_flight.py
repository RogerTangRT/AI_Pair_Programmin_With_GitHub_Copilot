"""test_flight.py

Exemplos e utilitários simples:

- mapeia uma lista de nomes para idades usando um comprehension;
- calcula a média das idades;
- demonstra duas versões de Fibonacci: recursiva (ineficiente) e com cache (eficiente).

Arquivo didático — funções são intencionais para aprendizado.
"""

# Imports utilizados para demonstrações (memorização em `fibonacci_cached`).
from functools import lru_cache


# Lista de nomes (cada elemento corresponde à mesma posição em `AGES`)
FIVE_NAMES = ["John", "Jane", "Jack", "Jill", "Joe"]

# Lista de sobrenomes (cada sobrenome corresponde ao nome na mesma posição
# em `FIVE_NAMES`). Usada por `get_last_name` para mapear `nome -> sobrenome`.
LAST_NAMES = ["Doe", "Smith", "Johnson", "Williams", "Brown"]

# Lista de idades — mantenha a ordem correspondente a `FIVE_NAMES`.
AGES = [25, 30, 22, 28, 35]


# Função utilitária: retorna o sobrenome associado a um `name`.
# - Cria um dicionário a partir de `FIVE_NAMES` e `LAST_NAMES` usando `zip`.
# - Retorna `None` se o `name` não for encontrado.
def get_last_name(name):
    """Retorna o sobrenome correspondente ao nome fornecido.

    - Usa `zip` para emparelhar `FIVE_NAMES` e `LAST_NAMES`.
    - Retorna `None` se o nome não estiver na lista.
    """
    name_to_last_name = dict(zip(FIVE_NAMES, LAST_NAMES))
    return name_to_last_name.get(name)

# Dicionário que associa `nome -> idade` usando comprehension.
# Observações:
# - `zip(FIVE_NAMES, AGES)` emparelha até o comprimento da menor lista;
# - nomes duplicados em `FIVE_NAMES` resultarão em sobrescrita pelo último valor.
MAP_NAME_TO_AGE = {name: age for name, age in zip(FIVE_NAMES, AGES)}

def avarage_age():
    """Retorna a média aritmética das idades em `AGES`.

    - Retorna `0` se a lista `AGES` estiver vazia (evita divisão por zero).
    - Complexidade: O(n) pela soma dos elementos.
    """
    if not AGES:
        return 0
    return sum(AGES) / len(AGES)

def fibonacci(n):
    """Calcula o n-ésimo número da sequência de Fibonacci (recursivo).

    Observações:
    - Implementação recursiva simples; tem complexidade exponencial O(2^n).
    - Para `n` maiores, prefira `fibonacci_cached` ou uma versão iterativa.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache(maxsize=None)
def fibonacci_cached(n):
    """Calcula o n-ésimo número da sequência de Fibonacci com memorização.

    - Usa `functools.lru_cache` para armazenar resultados intermediários.
    - Complexidade aproximada: O(n) e O(n) memória adicional para cache.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)



# Exemplos de uso (executados quando o arquivo é executado como script)
if __name__ == "__main__":
    # Mostra o dicionário nome->idade
    print("Mapeamento nome->idade:", MAP_NAME_TO_AGE)

    # Calcula a idade média
    print("Idade média:", avarage_age())

    # Fibonacci recursivo (ineficiente para n grande)
    print("Fibonacci recursivo (n=10):", fibonacci(10))

    # Fibonacci com memorização — recomendado para n maiores
    print("Fibonacci com cache (n=35):", fibonacci_cached(35))

    # Exemplo de uso da nova função `get_last_name`
    print("Sobrenome de Jane:", get_last_name("Jane"))

