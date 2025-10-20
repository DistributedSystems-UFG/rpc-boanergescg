import rpyc
from constRPYC import *

class Client:
  # Conecta-se ao servidor usando as constantes definidas em constRPYC.py
  conn = rpyc.connect(SERVER, PORT)

  print("--- LISTA INICIAL ---")
  print("Lista atual:", conn.root.exposed_values())

  # 1. Teste de exposed_append (como no original)
  print("\n--- 1. Teste de APPEND ---")
  value = int(input("Valor para adicionar (append): "))
  conn.root.exposed_append(value)
  print("Lista após append:", conn.root.exposed_values())

  # 2. Teste de exposed_insert
  print("\n--- 2. Teste de INSERT ---")
  insert_value = int(input("Valor para inserir: "))
  insert_index = int(input("Índice para inserir: "))
  conn.root.exposed_insert(insert_index, insert_value)
  print("Lista após insert:", conn.root.exposed_values())

  # 3. Teste de exposed_search
  print("\n--- 3. Teste de SEARCH ---")
  search_value = int(input("Valor para pesquisar: "))
  result_index = conn.root.exposed_search(search_value)
  if result_index != -1:
    print(f"Valor {search_value} encontrado no índice: {result_index}")
  else:
    print(f"Valor {search_value} não encontrado.")

  # 4. Teste de exposed_sort
  print("\n--- 4. Teste de SORT ---")
  conn.root.exposed_sort() # Ordena crescentemente
  print("Lista após sort (crescente):", conn.root.exposed_values())
  conn.root.exposed_sort(True) # Ordena decrescentemente
  print("Lista após sort (decrescente):", conn.root.exposed_values())

  # 5. Teste de exposed_remove
  print("\n--- 5. Teste de REMOVE ---")
  remove_value = int(input("Valor para remover: "))
  result_remove = conn.root.exposed_remove(remove_value)
  if result_remove == 0:
    print(f"Valor {remove_value} removido com sucesso.")
  else:
    print(f"Erro: Valor {remove_value} não encontrado para remoção.")
  print("Lista após remove:", conn.root.exposed_values())

  print("\n--- FIM DOS TESTES ---")
