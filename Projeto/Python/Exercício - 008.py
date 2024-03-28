print("====== DESAFIO 008 ======")
m = float(input("Digite um valor em metros: "))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print("{} metros equivale: \n{} centimetros e {} milimetros. ".format(m, cm, mm))
print("{} km e {} hm. ".format(km, hm))
print("{} dam e {} dm. ".format(dam, dm))
