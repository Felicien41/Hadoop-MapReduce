# coding: utf8
import sys
import re
import collections

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

#Additionne les nombres du tableau
def countOccurence(array):
	sum = 0
	for i in array:
        	sum += i
	return sum

def reduce(list):
	dict = {}
	for map in list:
    		for key in map:
			if(key in dict):
            			dict[key] = dict[key] + countOccurence(map[key])
        		else:
            			dict[key] = countOccurence(map[key])

	return dict


#Ouverture et lecture du fichier
text = open(sys.argv[1], 'r').read()

#Suppression des caractères spéciaux et des majuscules
text = text.lower()
text = re.sub('\W+',' ', text )

#Map phase
mapList = map(text)

#REDUCE phase
dictionnary = reduce(mapList)

#Tri et affichage du résultat
d = collections.OrderedDict(sorted(dictionnary.items()))
for k, v in d.items():
     print k, v
