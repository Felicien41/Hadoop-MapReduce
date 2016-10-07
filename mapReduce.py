# coding: utf8
import sys
import re 


def map(text):
	#Creation d'un dictionnaire où la clef est le mot et la valeur est une liste de 1, chaque un représentant une occurence du mot
	list = []
	words = re.sub("[^\w]", " ",  text).split()
	map = dict()
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


#Ouverture et lecture du fichier
text = open(sys.argv[1], 'r').read()

#Suppression des caractères spéciaux et des majuscules
text = text.lower()
text = re.sub('\W+',' ', text )

#Map phase
mapList = map(text)
