from class_conto import Conto

conto1 = Conto()

conto1.addSoldi(30)
conto1.addSoldi(10)
conto1.addSoldi(30)
conto1.prelievo(10)
conto1.prelievo(10)
conto1.prelievo(10)
print(conto1)
print(conto1.movimenti[-5:])
print(conto1.getSaldo())