# coding: utf8
import sys
import re


def map(text):
	#Creation d'un dictionnaire où la clef est le mot et la valeur est une liste de 1, chaque un représentant une occurence du mot
	list = []
	#Séparation des mots
	words = re.sub("[^\w]", " ",  text).split()
	map = dict() #création du dictionnaire
	for word in words:
		if (word in map):
            		map[word].append(1) 
        	else:
            		map[word] = [1]
    	list.append(map)
	return list

#Verification des arguments
if(len(sys.argv) < 2):
	print "Usage : "+sys.argv[0]+" FILE where FILE contains the words to count"
	exit()

def reduce(list):
	dict = {}
	for map in list:
    		for key in map:
        		if(key in finalDict):
            			dict[key] = dict[key] + sumNumbersArray(map[key])
        		else:
            			dict[key] = sumNumbersArray(map[key])
	return dict

#Ouverture et lecture du fichier
text = open(sys.argv[1], 'r').read()

#Suppression des caractères spéciaux et des majuscules
text = text.lower()
text = re.sub('\W+',' ', text )

#Map phase
mapList = map(text)
print mapList

#Shuffle / Sort phase
#SORT HERE

#REDUCE phase
dictionnary = reduce(mapList)


#Affichage du résultat
for key in dictionnary:
	print key + " " + str(dictionnary[key])

