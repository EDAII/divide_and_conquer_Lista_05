import time


class CountInversions:

    def __init__(self):
        self.numero_inversoes = 0

    # O(2T(n / 2))
    def merge_sort(self, vetor):
        [esquerda, direita] = self.divide(vetor)

        if len(vetor) > 1:
            esquerda = self.merge_sort(esquerda)
            direita = self.merge_sort(direita)
            merged = self.combina(esquerda, direita)

            return merged

        else:
            return vetor

    # O(1)
    def divide(self, vetor):
        meio = (len(vetor) / 2)
        esquerda = vetor[:int(meio)]
        direita = vetor[int(meio):]

        return [esquerda, direita]

    def combina(self, subvetor_esquerda, subvetor_direita):
        vetor = []
        i, j = 0, 0

        for k in range(len(subvetor_esquerda) + len(subvetor_direita) + 1):

            if subvetor_esquerda[i] <= subvetor_direita[j]:
                vetor.append(subvetor_esquerda[i])
                i += 1
                # Adiciona os elementos restantes do subvetor_direita
                if i == len(subvetor_esquerda) and j != len(subvetor_direita):
                    while j != len(subvetor_direita):
                        k += 1
                        vetor.append(subvetor_direita[j])
                        j += 1
                    break

            else:
                vetor.append(subvetor_direita[j])
                self.numero_inversoes += (len(subvetor_esquerda) - i)
                j += 1

                if j == len(subvetor_direita) and i != len(subvetor_esquerda):
                    while i != len(subvetor_esquerda):
                        k += 1
                        vetor.append(subvetor_esquerda[i])
                        i += 1
                    break

        return vetor

    def main(self):
        # [4, 3, 2, 1],[1, 20, 6, 4, 5], [1, 5, 4, 8, 10, 2, 9, 12, 11, 3, 7]
        vetor = [1, 20, 6, 4, 5]
        self.numero_inversoes = 0

        print('\nVetor original:\n')
        print(vetor)

        inicio = time.time()
        vetor_ordenado = self.merge_sort(vetor)
        fim = time.time()

        print ('\nVetor ordenado:\n')
        print(vetor_ordenado)
        print ('\nNumero de Inversoes:\n', self.numero_inversoes)
        print('Tempo para execucao: ', fim - inicio)

if __name__ == '__main__':
    CountInversions().main()
