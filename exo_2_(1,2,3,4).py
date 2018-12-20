un_dico={'toto':3, 'titi':1, 'tutu':42}
un_dico['tata'] = 8
un_dico['titi'] += 1
print(un_dico, end = '\n')
def maj_dico_compte(dico, mot):
    dico[mot] = dico.get(mot, 0)
    #dico.get(mot,0) renvoie la valeur de mot s'il existe dans le dico ou l'ajoute comme clé puis lui affecte la valeur 0
    for mots in dico:
        if mots == mot:
            dico[mot] += 1 #le mot existe forcément dans le dico maintenant et la valeur de la dite clé incrémente de 1
    
    return dico

maj_dico_compte(un_dico, 'tata')
print(un_dico, end = '\n')
maj_dico_compte(un_dico, 'tatou')
print(un_dico, end = '\n')