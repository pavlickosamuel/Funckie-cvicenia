def rozsekaj(text: str, sirka: int) -> str:
    vystup = ""
    for i in range(0, len(text), sirka):
        vystup += text[i:i+sirka]
        vystup += "\n"
    return vystup

print(rozsekaj(text="Anicka dusicka, kde si bola", sirka=10))


def stvorec(n:int, znak:str) -> str:
    vystup = ""
    for i in range(0,n):
        if i == 0 or i == n-1:
            vystup += znak * n 
            vystup += "\n"
        else:
            vystup += znak + (n-2) *" " + znak + "\n"
    return vystup
        
print (stvorec(10,"$"))


def vyhod_duplikaty(retazec: str) -> str:
    vystup = retazec[0]
    for i in range (1, len(retazec)):
        if retazec[i] != vystup[-1]:
            vystup += retazec[i]    
    return vystup

print (vyhod_duplikaty("BBraatisssllavaaaaa"))


