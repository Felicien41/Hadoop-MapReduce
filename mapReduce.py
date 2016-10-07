import sys
import re 

#Verification des arguments
if(len(sys.argv) < 2):
	print "Usage : "+sys.argv[0]+" FILE where FILE contains the words to count"
	exit()


#Ouverture et lecture du fichier
text = open(sys.argv[1], 'r').read()

#Suppression des caractères spéciaux et des majuscules
text = text.lower()
text = re.sub('\W+',' ', text )

print cleanString
#Map phase
mapList = map
