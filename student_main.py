from tkinter import Tk
import mysql.connector
from student_base import StudentController
from student_def import studentUI


class StudentMain:
    def __init__(self):
        # Initialiser la connexion à la base de données MySQL
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Remplacez par votre utilisateur MySQL
            password="",  # Remplacez par votre mot de passe MySQL
            database="etudiant"  # Remplacez par le nom de votre base de données
        )
        self.controller = StudentController(self.connection)

        # Initialiser la fenêtre principale
        self.window = Tk()
        self.window.geometry("900x500")
        self.window.configure(bg="#FFFFFF")
        # Charger les ressources
        self.ui = studentUI(self.window, self.controller)

        # Initialiser l'interface utilisateur
        self.initialize_ui()

    def initialize_ui(self):
            # Charger les images et créer les éléments de l'interface

            # Ajoutez d'autres boutons et widgets similaires ici...

        self.ui.Table()
        self.ui.displaydata()
        self.ui.setup_ui()


    def run(self):
            # Lancer la boucle principale de l'application
            self.window.resizable(False, False)
            self.window.mainloop()

# Démarrer l'application
if __name__ == "__main__":
    app = StudentMain()
    app.run()
