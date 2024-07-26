print("====== DESAFIO 105 ======") 

def notas(*nota, sit=False):
      '''
            Regras... da função!!!
      '''
      if sit == True:
            dic = {"total": 0, "maior": 0, "menor": 0, "média": 0, "situação": ""}
      else:
            dic = {"total": 0, "maior": 0, "menor": 0, "média": 0}

      for c in range(len(nota)):
            dic["total"] += nota[c]
            if c == 0:
                  dic["maior"] = nota[c]
                  dic["menor"] = nota[c]

            if nota[c] > dic["maior"]:
                  dic["maior"] = nota[c]

            if nota[c] < dic["menor"]:
                  dic["menor"] = nota[c]
      
      dic["média"] = dic["total"] / len(nota)
      if sit == True:
            if dic["média"] < 6:
                  dic["situação"] = "RUIM"
            elif dic["média"] <= 7:
                  dic["situação"] = "RAZOÁVEL"
            elif dic["média"] <= 10:
                  dic["situação"] = "BOM"
      
      dic["total"] = len(dic)

      return dic.copy()


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)