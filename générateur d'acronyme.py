# On permet une intéraction avec l'utilisateur pour pouvoir écrire sa phrase
user_input = input("Entrer une phrase: ")

# Se débarrasser du mot 'of' en utilisant la méthode replace () et séparer l'entrée utilisateur en mots individuels en utilisant la méthode split ()
phrase = (user_input.replace('de', '')).split()
phrase = (user_input.replace('à', '')).split()
# Initialisation d'une chaîne vide pour ajouter l'acronyme
a = ""

# boucle pour ajouter l'acronyme
for word in phrase:
    a = a + word[0].upper()

print(f'Acronyme de {user_input} est {a}')

