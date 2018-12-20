def affiche_mots(nom_fichier):
    f = open(nom_fichier)
    dict   = {}
    dict_2 = {}
    Lst_Motdifférent = []
    CompteurMot_différent = 0
    CompteurMot_total = 0
    
    for line in f:
        line = line.strip()
        line = line.replace("."," ")
        line = line.replace(","," ")
        line = line.replace("'"," ")
        line = line.replace('"'," ")
        line = line.replace(";"," ")
        line = line.replace("—"," ")
        line = line.replace("-"," ")
        line = line.replace("("," ")
        line = line.replace(")"," ")
        line = line.replace("!"," ")
        words = line.split()
        for word in words:
            word = word.lower()
            if dict.get(word, 0) == 0:
                dict[word] = 1
                CompteurMot_différent += 1
                
            else:
                dict[word] += 1
                
            CompteurMot_total += 1
            
        min_ = (2.5*CompteurMot_différent)/100
        max_ = (7*CompteurMot_différent)/100
            
        
    for word in dict:
        if dict[word] > min_: #si la valeur soit le nombre d'occurences dans le texte est supérieur au seuil on l'ajoute dans le deuxième dict
            dict_2[word] = dict[word]
        
    
#fction d'internet renvoyant une liste ou chaque élément est un tuple avec tous les éléments ranges par ordre croissant en fonction de la valeur associée à la clé
    import operator
    sorted_dict_2 = sorted(dict_2.items(), key=operator.itemgetter(1)) 
    ''', reverse = True)'''
#la fonction reverse permet d'inverser le sens de classement cad croissant (par défaut) et décroissant: sorted(dict_2.items(), key=operator.itemgetter(1), reverse = True///False)
    
    print(CompteurMot_total)
    print(CompteurMot_différent)
    
    for each in enumerate(sorted_dict_2):
        print(each[1][0],':', each[1][1])

affiche_mots('..\..\swag.txt')
