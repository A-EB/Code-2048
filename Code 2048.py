#Ali El Boukili
#Asmar MOHAMED

#1 Partie Guidée : Le Tic-Tac-Toe

CaseT = str
# les elements de CaseT sont soit " " soit "O" soit "X"
PlateauT = List[List[CaseT]]
# les elements de PlateauT sont des matrices 3x3

#Question 1

def plateau_vide() -> PlateauT :
    '''Renvoie un plateau de morpion vide'''
    plt_vide : PlateauT = [[" "," "," "],
                           [" "," "," "],
                           [" "," "," "]]
    return plt_vide

pla1 : PlateauT = plateau_vide()
assert plateau_vide()[1][1] == " "
assert pla1[0][2] == " "

#Question 2

def videt(plateau : PlateauT,i:int,j:int) -> bool:
    '''Précondition : (0<=i and i<=2) and (0<=j and j<=2)
    Renvoie True si la case de coordonnées (i,j) est vide,
    False sinon.'''
    return plateau[i][j] == " "

assert videt(pla1 , 1, 1) == True
assert videt(pla1 , 0, 2) == True
assert videt ([["X"," "," "],[" "," "," "],[" "," "," "]] , 0, 0) == False


#Question 3

def jouex(pla : PlateauT,i:int,j:int) -> None :
    '''***Procedure***
    Précondition : (0<=i and i<=2) and (0<=j and j<=2)
    Inscris le symbole "X" dans la case de coordonnées (i,j)'''
    pla[i][j] = "X"

def joueo(pla : PlateauT,i:int,j:int) -> None :
    '''***Procedure***
    Précondition : (0<=i and i<=2) and (0<=j and j<=2)
    Inscris le symbole "X" dans la case de coordonnées (i,j)'''
    pla[i][j] = "O"

assert videt(pla1, 0,2)
assert jouex(pla1,1,1) == None
assert joueo(pla1,0,2) == None
assert not videt(pla1, 0,2)

#Question 4

def dessine_plateaut(pla : PlateauT) ->str :
    '''Précondition : pla un plateau de morpion (matrice 3*3).
    Renvoie une chaine de caractère correspondant
    à un affichage du plateau, la case (0,0) étant en bas à gauche.'''
    return ("/---\\\n" +
            "|"+str(pla[0][2])+str(pla[1][2])+str(pla[2][2])+"|\n" +                                #[[(0,2),(1,2),(2,2)]
            "|"+str(pla[0][1])+str(pla[1][1])+str(pla[2][1])+"|\n" +                                #,[(0,1),(1,1),(2,1)]
            "|"+str(pla[0][0])+str(pla[1][0])+str(pla[2][0])+"|\n" +                                #,[(0,0),(1,0),(2,0)]]
            "\---/")
assert dessine_plateaut(pla1) == '/---\\\n|O  |\n| X |\n|   |\n\\---/'

#Question 5

def gagnet(pla : PlateauT, s : CaseT) -> bool :
    '''Précondition : s == "X" or s == "O"
                      pla un plateau de morpion (matrice 3*3).
    Décide si le plateau est gagnat pour s.'''
    i : int
    for i in range(0,3) :
        if pla[i] == [s,s,s] :
            return True
        if pla[0][i]+pla[1][i]+pla[2][i] == s+s+s :
            return True
    if pla[0][0]+pla[1][1]+pla[2][2] == s+s+s or pla[0][2]+pla[1][1]+pla[2][0] == s+s+s :
        return True
    return False

assert gagnet ([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "X") == True
assert gagnet ([["O", " ", "X"], ["O", "X", " "], ["X", " ", " "]], "O") == False
assert gagnet ([["X", " ", "O"], ["X", "O", " "], ["X", " ", " "]], "X") == True
assert gagnet ([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]], "X") == False
assert gagnet ([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]], "O") == True

#Question 6

def pleint(pla:PlateauT) -> bool :
    '''Précondition : pla un plateau de morpion (matrice 3*3).
    Renvoie True si pla est pleint, False sinon.'''
    i:List[str]
    for i in pla :
        j:str
        for j in i :
            if j == " " :
                return False
    return True

assert pleint([["X", " ", "O"], ["O", "X", " "], ["X", " ", " "]]) == False
assert pleint([["O", "X", "O"], ["X", "O", "X"], ["O", "X", "O"]]) == True

#Question 7
import random

def tourt(pla:PlateauT,i:int,j:int) -> None:
    '''***Procedure***
    Précondition : (0<=i and i<=2) and (0<=j and j<=2)
                   pla un plateau de morpion (matrice 3*3).
    Joue un tour entier de morpion sur le plateau pla contre
    l'ordinateur jouant au hasard, où le symbole
    "X" du joueur sera inscris dans la case de coordonnées (i,j)
    à ce tour.'''
    #Tour du joueur
    if pla[i][j] == " " :
        jouex(pla,i,j)
        print("Joueur joue en ("+str(i)+" , "+str(j)+")")
        print(dessine_plateaut(pla))
    else :
        print("ILLEGAL")
        return None
    #Vérifie si le joueur gagne
    if gagnet(pla,'X') :
        print('Tu a gagné !')
        return None

    #Tour de l'ordi
    k : int = int(random.random()*3)
    l : int = int(random.random()*3)
    while pla[k][l] != " " :
        k : int = int(random.random()*3)
        l : int = int(random.random()*3)
    joueo(pla,k,l)
    print("=============================")
    print("l'ordinateur  joue en ("+str(k)+" , "+str(l)+")")
    print(dessine_plateaut(pla))
    #Vérifie si l'ordi gagne
    if gagnet(pla,'O') :
        print('Tu as perdu !')
        return None
    
    #Vérifie si il y a égalité
    if pleint(pla) :
        print("=============================")
        print("ÉGALITÉ")
        return None
    #Fin du tour
    return None

plat_essai : PlateauT = plateau_vide()


#Question 9(Suggestion)

      
def croix(x:float,y:float) -> Image:
    '''Précondition : (x >= -1 and x <= 1) and (y >= -1 and y <= 1)
    Dessine une croix où son centre se trouve dans les coordonnées
    (x,y) de l'image)'''
    return overlay(draw_line(x-1/3,y-1/3, x+1/3,y+1/3),draw_line(x-1/3,y+1/3, x+1/3,y-1/3))

def rond(x:float,y:float) -> Image:
    '''Précondition : (x >= -1 and x <= 1) and (y >= -1 and y <= 1)
    Dessine un cercle où son centre se trouve dans les coordonnées
    (x,y) de l'image)'''
    return overlay(draw_ellipse(x-1/3,y-1/3, x+1/3,y+1/3))


# x: 0 -> -2/3
# x: 1 -> 0
# x: 2 -> 2/3

# y: 0 -> -2/3
# y: 1 -> 0
# y: 2 -> 2/3

def conv(n : int) -> float :
    '''Précondition : n>=0 and n<=2
    convertis les coordonnées d'un PlateauT
    de morpion pour les coordonnées d'une image
    représentant un plateau de morpion'''
    if n == 0 :
        return -2/3
    elif n == 1 :
        return 0
    elif n == 2 :
        return 2/3
assert conv(0) == -2/3
assert conv(1) == 0
assert conv(2) == 2/3



def dessine_plateaut_im(pla : PlateauT) -> Image:
    '''Précondition : pla un plateau de morpion (matrice 3*3)
    Renvoie une image représentant le plateau pla.'''
    res : Image = overlay(draw_line(-1,-1/3,1,-1/3),draw_line(-1,1/3,1,1/3),draw_line(-1/3,1,-1/3,-1),draw_line(1/3,1,1/3,-1))
    i : int
    for i in range(len(pla)):
        j : int
        for j in range(len(pla[i])):
            if pla[i][j] == 'X' :
                res = overlay(res,croix(conv(i),conv(j)))
            if pla[i][j] == 'O' :
                res = overlay(res,rond(conv(i),conv(j)))
    return res
    




def tourt_im(pla:PlateauT,i:int,j:int) -> None:
    '''***Procedure***
    Précondition : (0<=i and i<=2) and (0<=j and j<=2)
                   pla un plateau de morpion (matrice 3*3).
    Joue un tour entier de morpion sur le plateau pla contre
    l'ordinateur jouant au hasard, où le symbole
    "X" du joueur sera inscris dans la case de coordonnées (i,j)
    à ce tour.'''
    #Tour du joueur
    if pla[i][j] == " " :
        jouex(pla,i,j)
        print("Joueur joue en ("+str(i)+" , "+str(j)+")")
    else :
        print("ILLEGAL")
        return None
    #Vérifie si le joueur gagne
    if gagnet(pla,'X') :
        show_image(dessine_plateaut_im(pla))
        print('Tu a gagné !')
        return None

    #Tour de l'ordi
    k : int = int(random.random()*3)
    l : int = int(random.random()*3)
    while pla[k][l] != " " :
        k = int(random.random()*3)
        l = int(random.random()*3)
    joueo(pla,k,l)
    print("=============================")
    print("l'ordinateur  joue en ("+str(k)+" , "+str(l)+")")
    show_image(dessine_plateaut_im(pla))
    #Vérifie si l'ordi gagne
    if gagnet(pla,'O') :
        print('Tu as perdu !')
        return None
    
    #Vérifie si il y a égalité
    if pleint(pla) :
        show_image(dessine_plateaut_im(pla))
        print("=============================")
        print("ÉGALITÉ")
        return None
    #Fin du tour
    return None



#3 Suggestion : 2048
Case = int
# les elements de CaseT sont des puissances de 2 de 2 à 2048, et 0.
#Une case ayant comme valeur 0 est considérée comme une case 'vide'.
Pl2 = List[List[Case]]
# les elements de Pl2 sont des matrices 4x4


#Initialisation du début de la partie
def plat2048_ini() -> Pl2 :
    '''Initialise un plateau de 2048.
    Plus précisement, place deux chiffres
    choisi aléatoirement entre 2 ou 4 dans
    deux cases au hasard dans une matrice 4*4
    remplie initialement de 0'''
    plt_vide : Pl2 = [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
    
    i : int = int(random.random()*3)
    j : int = int(random.random()*3)
    plt_vide[i][j] = [2,2,2,4][int((random.random()*4))]
    k : int = int(random.random()*3)
    l : int = int(random.random()*3)
    while (i,j) == (k,l) :
        k = int(random.random()*3)
        l = int(random.random()*3)
    plt_vide[k][l] = [2,2,2,4][int((random.random()*4))]
    return plt_vide

pla2 : Pl2 = plat2048_ini() 



#Générer un 2 ou un 4 sur une case aléatoire
def generation(pla:Pl2) -> None :
    '''***Procedure***
    Precondition : pla un plateau de 2048 (matrice 4*4)
    Ajoute dans une case au hasard 'vide' du plateau
    un 2 ou un 4.'''
    i : int = int(random.random()*3)
    j : int = int(random.random()*3)
    while pla[i][j] != 0 :
        i : int = int(random.random()*3)
        j : int = int(random.random()*3)
    pla[i][j] = [2,2,2,4][int((random.random()*4))]


def plamvt(pla : Pl2, dir : str) -> None :
    '''***Procedure***
    Precondition : dir == 'h' or dir == 'b' or dir == 'g' or dir == 'd'
                   pla un plateau de 2048 (matrice 4*4)
    Déplace toutes les cases non-'vides' dans la direction choisie.
    Si deux nombres identiques se rencontrent, la case d'arrivée de vient
    la somme de ces deux nombres.'''
    n : int = 0
    
    if dir == "h" :
        i : int
        j : int
        for i in range(len(pla)):
            for j in range(len(pla[i])):
                if i != 0 :
                    if pla[i-n][j] == 0 :
                        pla[i-n][j] = pla[i][j]
                        pla[i][j] = 0
                    elif pla[i-n][j] == pla[i][j] :
                        pla[i-n][j] = pla[i][j]*2
                        pla[i][j] = 0
                        
                    elif pla[i-n+1][j] == 0 and i >= 2 and i-n+1 != i :
                        pla[i-n+1][j] = pla[i][j]
                        pla[i][j] = 0
                    elif pla[i-n+1][j] == pla[i][j] and i >= 2 and i-n+1 != i :
                        pla[i-n+1][j] = pla[i][j]*2
                        pla[i][j] = 0
                        
                    elif pla[i-n+2][j] == 0 and i == 3 and i-n+2 != i :
                        pla[i-n+2][j] = pla[i][j]
                        pla[i][j] = 0
                    elif pla[i-n+2][j] == pla[i][j] and i == 3 and i-n+2 != i :
                        pla[i-n+2][j] = pla[i][j]*2
                        pla[i][j] = 0
                    
            n = n+1
            
    elif dir == "b" :
        k : int
        l : int
        for k in range(-1,-len(pla)-1,-1):
            for l in range(-1,-len(pla[k])-1,-1):
                if k != -1 :
                    if pla[k+n][l] == 0 :
                        pla[k+n][l] = pla[k][l]
                        pla[k][l] = 0
                    elif pla[k+n][l] == pla[k][l] :
                        pla[k+n][l] = pla[k][l]*2
                        pla[k][l] = 0   
                        
                    elif pla[k+n-1][l] == 0 and k <= -3 and k+n-1 != k :
                        pla[k+n-1][l] = pla[k][l]
                        pla[k][l] = 0
                    elif pla[k+n-1][l] == pla[k][l] and k <= -3 and k+n-1 != k :
                        pla[k+n-1][l] = pla[k][l]*2
                        pla[k][l] = 0
                    
                    elif pla[k+n-2][l] == 0 and k == -4 and k+n-2 != k :
                        pla[k+n-2][l] = pla[k][l]
                        pla[k][l] = 0
                    elif pla[k+n-2][l] == pla[k][l] and k == -4 and k+n-2 != k :
                        pla[k+n-2][l] = pla[k][l]*2
                        pla[k][l] = 0
                    
            n = n+1

    elif dir == "g" :
        di : int
        dj : int
        for di in range(len(pla)):
            for dj in range(len(pla[di])):
                if dj != 0 :
                    if pla[di][dj-n] == 0 :
                        pla[di][dj-n] = pla[di][dj]
                        pla[di][dj] = 0
                    elif pla[di][dj-n] == pla[di][dj] :
                        pla[di][dj-n] = pla[di][dj]*2
                        pla[di][dj] = 0
                        
                    elif pla[di][dj-n+1] == 0 and dj >= 2 and dj-n+1 != dj :
                        pla[di][dj-n+1] = pla[di][dj]
                        pla[di][dj] = 0
                    elif pla[di][dj-n+1] == pla[di][dj] and dj >= 2 and dj-n+1 != dj :
                        pla[di][dj-n+1] = pla[di][dj]*2
                        pla[di][dj] = 0
                        
                    elif pla[di][dj-n+2] == 0 and dj == 3 and dj-n+2 != dj :
                        pla[di][dj-n+2] = pla[di][dj]
                        pla[di][dj] = 0
                    elif pla[di][dj-n+2] == pla[di][dj] and dj == 3 and dj-n+2 != dj :
                        pla[di][dj-n+2] = pla[di][dj]*2
                        pla[di][dj] = 0
                    
                n = n+1
            n = 0

    elif dir == "d" :
        dk : int
        dl : int
        for dk in range(-1,-len(pla)-1,-1):
            for dl in range(-1,-len(pla[dk])-1,-1):
                if dl != -1 :
                    if pla[dk][dl+n] == 0 :
                        pla[dk][dl+n] = pla[dk][dl]
                        pla[dk][dl] = 0
                    elif pla[dk][dl+n] == pla[dk][dl] :
                        pla[dk][dl+n] = pla[dk][dl]*2
                        pla[dk][dl] = 0
                        
                    elif pla[dk][dl+n-1] == 0 and dk <= -3 and dl+n-1 != dl :
                        pla[dk][dl+n-1] = pla[dk][dl]
                        pla[dk][dl] = 0
                    elif pla[dk][dl+n-1] == pla[dk][dl] and dk <= -3 and dl+n-1 != dl :
                        pla[dk][dl+n-1] = pla[dk][dl]*2
                        pla[dk][dl] = 0
                        
                    elif pla[dk][dl+n-2] == 0 and dk == -4 and dl+n-2 != dl :
                        pla[dk][dl+n-2] = pla[dk][dl]
                        pla[dk][dl] = 0
                    elif pla[dk][dl+n-2] == pla[dk][dl] and dk == -4 and dl+n-2 != dl :
                        pla[dk][dl+n-2] = pla[dk][dl]*2
                        pla[dk][dl] = 0
                        
                n = n+1
            n = 0

pla3 : Pl2 = [[0,0,0,2],[0,0,0,0],[0,0,0,0],[2,0,0,2]]
pla4 : Pl2 = [[0,4,0,2],[0,0,0,0],[0,0,0,0],[0,0,0,2]]
pla5 : Pl2 = [[0,0,0,0],[2,0,0,2],[0,0,8,2],[0,0,0,0]]
pla6 : Pl2 = [[0,4,4,0],[0,0,0,0],[0,0,0,0],[16,0,0,0]]

assert plamvt(pla3,'h') == None
assert pla3 == [[2,0,0,4],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

assert plamvt(pla4,'b') == None
assert pla4 == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,4,0,4]]

assert plamvt(pla5,'g') == None
assert pla5 == [[0,0,0,0],[4,0,0,0],[8,2,0,0],[0,0,0,0]]

assert plamvt(pla6,'d') == None
assert pla6 == [[0,0,0,8],[0,0,0,0],[0,0,0,0],[0,0,0,16]]



def dessine_plateau2048(pla : Pl2) ->str :
    '''Précondition : pla un plateau de 2048 (matrice 4*4).
    Renvoie une chaine de caractère correspondant
    à un affichage du plateau, les 0 étant représentés par des cases vides.'''
    res : str = "-----------------\n"
    i : List[Case]
    for i in pla :
        res = res + "|   |   |   |   |\n"
        j : Case
        for j in i :
            if j != 0 :
                res = res +"| " +str(j)+" "
            else :
                res = res + "|   "
        res = res +"|\n"+"|   |   |   |   |\n"
        res = res + "\n"+"-----------------\n"
    return res

assert dessine_plateau2048([[0, 0, 0, 0], [0, 4, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0]]) == '-----------------\n|   |   |   |   |\n|   |   |   |   |\n|   |   |   |   |\n\n-----------------\n|   |   |   |   |\n|   | 4 |   |   |\n|   |   |   |   |\n\n-----------------\n|   |   |   |   |\n| 2 |   |   |   |\n|   |   |   |   |\n\n-----------------\n|   |   |   |   |\n|   |   |   |   |\n|   |   |   |   |\n\n-----------------\n'

    
def rempli2048(pla:Pl2) -> bool :
    '''Précondition : pla un plateau de 2048 (matrice 4*4).
    Renvoie True si plus aucun mouvement n'est possible
    dans le plateau pla.'''
    i : int
    for i in range(len(pla))  :
        j : int
        for j in range(len(pla[i])) :
            if pla[i][j] == 0 :
                return False
            
    platest : Pl2 = [[e for e in a] for a in pla]
    plamvt(platest,'h')
    if platest != pla :
        return False
    plamvt(platest,'b')
    if platest != pla :
        return False
    plamvt(platest,'g')
    if platest != pla :
        return False
    plamvt(platest,'d')
    if platest != pla :
        return False
    
    return True

pla7 : Pl2 = [[2,4,64,16],[4,512,1024,8],[32,64,128,256],[64,32,256,128]]
assert rempli2048(pla7)
assert not rempli2048(pla2)



def gagne2048(pla : Pl2) -> bool :
    '''Précondition : pla un plateau de 2048 (matrice 4*4).
    Renvoie True si la valeur d'au moins une case est égale
    à 2048, False sinon.'''
    i : List[Case]
    for i in pla :
        j : Case
        for j in i :
            if j == 2048 :
                return True
    return False

assert gagne2048([[0,0,0,2048],[0,512,0,0],[0,0,16,0],[8,0,0,2]])
assert not gagne2048([[1024,0,0,2],[0,0,128,0],[0,1024,0,0],[2,16,0,2]])



def tour2048(pla : Pl2, dir : str) -> None :
    '''Precondition : dir == 'h' or dir == 'b' or dir == 'g' or dir == 'd' or dir == ""
                      pla un plateau de 2048 (matrice 4*4).
    Réalise un tour de jeu de 2048 sur le plateau pla.
    Mettre en argument le caractère vide "" pour initialisé une partie.'''
    if dir == '' :
        print(dessine_plateau2048(pla))
        return None
    if dir == "h" :
        plamvt(pla,'h')
        generation(pla)
        print(dessine_plateau2048(pla))
        if gagne2048(pla) :
            print("GAGNE")
            return None
        elif rempli2048(pla) :
            print("PERDU")
            return None

    elif dir == "b" :
        plamvt(pla,'b')
        generation(pla)
        print(dessine_plateau2048(pla))
        if gagne2048(pla) :
            print("GAGNE")
            return None
        elif rempli2048(pla) :
            print("PERDU")
            return None

    elif dir == "g" :
        plamvt(pla,'g')
        generation(pla)
        print(dessine_plateau2048(pla))
        if gagne2048(pla) :
            print("GAGNE")
            return None
        elif rempli2048(pla) :
            print("PERDU")
            return None

    elif dir == "d" :
        plamvt(pla,'d')
        generation(pla)
        print(dessine_plateau2048(pla))
        if gagne2048(pla) :
            print("GAGNE")
            return None
        elif rempli2048(pla) :
            print("PERDU")
            return None

plat_essai2 : Pl2 = plat2048_ini()
