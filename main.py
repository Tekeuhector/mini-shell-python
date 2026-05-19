import subprocess
import os

while True :
    cmd = input(os.getcwd() + " > ")

    # Pour terminer le programme
    if cmd == "exit" :
        break

    # Pour pouvoir changer de répertoire
    cmd_split = cmd.split(" ")
    if len(cmd_split) == 2 and cmd_split[0] == "cd" :
        try :
            os.chdir(cmd_split[1])
        except :
            print("Répertoire invalide")
    else :
        resultat = subprocess.run(cmd, shell=True, capture_output=True, universal_newlines=True)
        print(resultat.stdout) # Pour afficher le resultat
        print(resultat.stderr) # Pour afficher le message d'erreur s'il y'en a

