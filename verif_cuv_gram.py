def verificare(cuvant, gramatica, simbol_start):
    if not(cuvant) and '§' in gramatica[simbol_start]:
        return True
    for ramura in gramatica[simbol_start]:
        if cuvant and cuvant[0] == ramura[0]:
            if verificare(cuvant[1:], gramatica, ramura[1]):
                return True
    return False

gramatica = {'S':[('a', 'S'), ('§')]}

simbol_start = 'S'

cuvant = "aaaaaaaaaa"

if(verificare(cuvant, gramatica, simbol_start) == True):
    print(f"Cuvantul {cuvant} este acceptat.")
else:
    print(f"Cuvantul {cuvant} nu este acceptat.")