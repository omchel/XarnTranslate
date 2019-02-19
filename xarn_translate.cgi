#!/usr/bin/python
import cgi
import cgitb
# Authors:
# 	Maria Paolini and Chelina Ortiz Montanez


def translation(theword, fromnative, newlanguage):
	check = False
	translate = "unknown"
	with open('xarn_language.txt', 'r') as xl:
		line = xl.readline()
		while line:
			language1,word1,language2,word2 = line.split(",")
			if (fromnative == language1 and theword == word1 and newlanguage == language2):
				translate = word2.strip()
				check = True
				break
			elif (fromnative == language2 and theword == word2.strip() and newlanguage == language1):
				translate = word1
				check = True
				break
			line = xl.readline()
		if (check == False):
			print ("Sorry, there is no translation for this. \n")
			print "<style>"
			print "div {color:red;}"
			print "</style>"
			return translate
		else:
			print "<style>"
			print "div {color:#00ff00;}"
			print "</style>"
			return translate

def checkInput(theword, fromnative, newlanguage):
	translate = " "
	if not theword or not fromnative or not newlanguage:
		print "Not a valid input. \n"
		translate = "invalid"
		return translate
	else:
		theword = theword.lower()
		fromnative = fromnative.lower()
		newlanguage = newlanguage.lower()
		translate = translation(theword, fromnative, newlanguage)
		return translate

def checkTranslate(theword, fromnative, newlanguage, translate):
	if translate == "unknown" or translate == "invalid":
		print "<style>"
		print "p {color:red;}"
		print "</style>"
	elif translate == "invalid":
		print "<style>"
		print "div {color:red;}"
		print "</style>"
	else:
		print "<style>"
		print "p {color:blue;}"
		print "</style>"

def printTranslation(theword, fromnative, newlanguage, translate):
	print "<p>"
	print "Origin Language: " 
	print "<span style='color:black'>"
	print fromnative
	print "</span>"
	print "<p>"
	print "Original Word: "
        print "<span style='color:black'>"
	print theword
	print "</span>"
	print "</p>"
	print "<p>"
	print "Requested Language: "
        print "<span style='color:black'>"
	print newlanguage
	print "</span>"
	print "</p>"
	print "<p>"
	print "Translation: "
	print "<div>"
	print  translate
	print "</div>"
	print "</p>"

def main():
	print "Content-Type:text/html\n\n"
	print "<html>"
	cgitb.enable()
	form = cgi.FieldStorage()
	theword = (form.getvalue("theword"))
	fromnative = (form.getvalue("fromnative"))
	newlanguage = (form.getvalue("newlanguage"))
	translate = checkInput(theword, fromnative, newlanguage)
	checkTranslate(theword, fromnative, newlanguage, translate)
	output = printTranslation(theword,fromnative,newlanguage,translate)
	print "</html>"

if __name__ == "__main__":
	main()


