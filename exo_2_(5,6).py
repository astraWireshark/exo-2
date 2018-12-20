def compter_mots_total(str):
    dico = {}
    CompteurMots = 0
    for mot in str.split():
        maj_dico_compte(dico, mot)
        CompteurMots += 1
    '''print('le nombre de mots est :', CompteurMots)
    print(dico)'''
    return(dico)

def maj_dico_compte(dico, mot):
    dico[mot] = dico.get(mot, 0)
    dico[mot] +=1
    return dico
    
    
print(compter_mots_total('jaime beaucoup les arbres et les avions'))