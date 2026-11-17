from datetime import date
from pessoa import Pessoa
from marca import Marca
from veiculo import Veiculo

#Criando uma instancia de Pessoa
pessoa1 = Pessoa(cpf = "12345678900", nome = "Raphael", nascimento = date(1984, 7, 26), oculos = True)

#Criando uma instancia de Marca
marca1 = Marca(id = 1, nome = "Fiat", sigla = "Fia")

#Criandop uma instancia de Veiculo
veiculo1 = Veiculo(placa = "RMS2288", cor = "Cinza", proprietario = pessoa1, marca = marca1)

