import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  values = []

  # Procedimento original: Adiciona um novo elemento ao fim da lista
  def exposed_append(self, data):
    self.values = self.values + [data]
    return self.values

  # Procedimento original: Retorna o valor atual da lista
  def exposed_values(self):
    return self.values

  # NOVO PROCEDIMENTO: Pesquisa (exposed_search)
  # Retorna o índice da primeira ocorrência do valor ou -1 se não encontrado.
  def exposed_search(self, value):
    try:
      # Retorna o índice da primeira ocorrência do valor, se encontrado
      return self.values.index(value)
    except ValueError:
      # Retorna -1 se o valor não estiver na lista
      return -1

  # NOVO PROCEDIMENTO: Remoção (exposed_remove)
  # Remove a primeira ocorrência do valor. Retorna 0 em sucesso, -1 em falha.
  def exposed_remove(self, value):
    try:
      self.values.remove(value)
      return 0
    except ValueError:
      # Retorna -1 se o valor não estiver na lista
      return -1

  # NOVO PROCEDIMENTO: Inserção (exposed_insert)
  # Insere o valor em um índice específico. Retorna a lista completa em sucesso.
  def exposed_insert(self, index, value):
    # O método insert() do Python trata automaticamente índices fora do limite,
    # inserindo no início ou no fim, o que é robusto para RPC.
    self.values.insert(index, value)
    return self.values

  # NOVO PROCEDIMENTO: Ordenação (exposed_sort)
  # Ordena a lista in-place. O parâmetro 'reverse' é opcional.
  def exposed_sort(self, reverse=False):
    self.values.sort(reverse=reverse)
    # Retorna a lista ordenada
    return self.values

if __name__ == "__main__":
  # Inicia o servidor usando a porta definida em constRPYC.py
  server = ThreadedServer(DBList(), port = PORT)
  server.start()
