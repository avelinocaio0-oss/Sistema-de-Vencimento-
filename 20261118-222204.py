
print("===TECNOMART===")

produto=input("produto:")
quant=int(input("quantidade:"))
venc=int(input("dias para vencer:"))

print("===ANALISE===")

if venc<=7:
    print(" PROXIMO DO VENCIMENTO!")
    print(" SITUAÇÃO URGENTE! ")
    print(" REMOVA DO ESTOQUE!")
    
    
elif venc>=20:
     print("PRODUTO EM BOAS CONDIÇOES")
     print("SO SE ATENTE!")   
    