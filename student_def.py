from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, END, ttk
from tkinter.ttk import Combobox

from tkcalendar import DateEntry
from student_base import *
from student import *

class studentUI:
    def __init__(self, window, controller):
        self.root = window
        self.controller = controller
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\DELL\Desktop\projet BD\school_managment\assets\student")

        self.window = Tk()
        self.window.geometry("900x500")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=500,
            width=900,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        # Store references to images
        self.images = {}

        self.setup_ui()

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def add_image(self, file_name, x, y):
        image_path = self.relative_to_assets(file_name)
        if image_path.exists():
            image = PhotoImage(file=image_path)
            self.images[file_name] = image  # Store reference
            self.canvas.create_image(x, y, image=image)
        else:
            print(f"Image file {file_name} not found at {image_path}")

    def add_date_entry(self, x, y, width, height, image_file, bg_x, bg_y):
        """
        Ajoute un champ de saisie de date avec un arrière-plan et un format de date.
        """
        self.add_image(image_file, bg_x, bg_y)
        date_entry = DateEntry(
            self.window,
            width=int(width / 10),  # Ajuste la largeur
            background='white',
            foreground='black',
            borderwidth=0,
            date_pattern='yyyy-mm-dd',  # Modifiez selon le format souhaité
            state="readonly"

        )
        date_entry.place(x=x, y=y, width=width, height=height)

    def add_combobox(self, x, y, width, height, image_file, bg_x, bg_y, values, default_index=0):
        """
        Ajoute un champ déroulant (Combobox) à la fenêtre.

        Args:
            x (float): Position x du Combobox.
            y (float): Position y du Combobox.
            width (float): Largeur du Combobox.
            height (float): Hauteur du Combobox.
            values (list): Liste des options à afficher dans le Combobox.
            default_index (int): Index de l'option par défaut sélectionnée.

        Returns:
            Combobox: L'instance de Combobox créée.
        """
        self.add_image(image_file, bg_x, bg_y)
        combobox = Combobox(
            self.window,
            values=values,
            state="readonly"
        )
        combobox.place(x=x, y=y, width=width, height=height)
        combobox.current(default_index)  # Définit la sélection par défaut
        return combobox

    def add_entry(self, x, y, width, height, image_file, bg_x, bg_y):
        self.add_image(image_file, bg_x, bg_y)
        entry = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry.place(x=x, y=y, width=width, height=height)

    def add_button(self, x, y, width, height, image_file, command_text):
        self.add_image(image_file, x + width / 2, y + height / 2)
        button = Button(
            image=self.images[image_file],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print(command_text),
            relief="flat"
        )
        button.place(x=x, y=y, width=width, height=height)
    def setup_ui(self):
        # Adding images
        self.add_image("image_1.png", 450.0, 253.0)
        self.add_image("image_2.png", 505.0, 70.0)
        self.add_image("image_3.png", 391.0, 407.0)

        self.choices = ["Choix 1", "Choix 2", "Choix 3"]

        # Adding entries
        self.filiereF = self.add_combobox(524.0, 454.0, 135.0, 14.0, "entry_1.png", 591.5, 462.0, self.choices, default_index=0)
        self.nivF = self.add_combobox(524.0, 426.0, 135.0, 14.0, "entry_2.png", 591.5, 434.0, self.choices, default_index=0)
        self.mailF = self.add_entry(524.0, 398.0, 135.0, 13.0, "entry_3.png", 591.5, 405.5)
        self.numF = self.add_entry(524.0, 369.0, 135.0, 14.0, "entry_4.png", 591.5, 377.0)
        self.dateF = self.add_date_entry(524.0, 341.0, 135.0, 14.0, "entry_5.png", 591.5, 349.0)

        self.prenomF = self.add_entry(141.0, 454.0, 135.0, 14.0, "entry_6.png", 208.5, 462.0)
        self.nomF = self.add_entry(141.0, 426.0, 135.0, 14.0, "entry_7.png", 208.5, 434.0)
        self.cneF = self.add_entry(141.0, 398.0, 135.0, 13.0, "entry_8.png", 208.5, 405.5)
        self.cinF = self.add_entry(141.0, 369.0, 135.0, 14.0, "entry_9.png", 208.5, 377.0)
        self.idF = self.add_entry(141.0, 341.0, 135.0, 14.0, "entry_10.png", 208.5, 349.0)

        self.rechercheF = self.add_entry(111.0, 141.0, 676.0, 22.0, "entry_11.png", 449.0, 153.0)

        # Adding buttons
        #ajout
        self.add_button(784.0, 348.0, 87.0, 22.0, "button_1.png", "button_1 clicked")
        #modif
        self.add_button(784.0, 387.0, 87.0, 22.0, "button_2.png", "button_2 clicked")
        #suppression
        self.add_button(783.0, 433.0, 87.0, 22.0, "button_3.png", "button_3 clicked")
        #rechercher
        self.add_button(792.0, 141.0, 87.0, 23.0, "button_4.png", "button_4 clicked")
        #menu
        self.add_button(13.0, 12.0, 80.0, 25.0, "button_5.png", "button_5 clicked")
        #id_filtre
        self.add_button(16.0, 141.0, 94.0, 23.0, "button_6.png", "button_6 clicked")

        self.window.resizable(False, False)

    def displaydata(self):
        self.loadStudents()

    def loadStudents(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        students = self.controller.getAllStudents()
        for etudiant in students:
            self.tree.insert("", "end", values=etudiant)

    # Fonction d'ajout d'un étudiant (à personnaliser selon votre logique)
    def addStudent(self):
        print("Ajouter un étudiant")
        # Code pour ajouter un étudiant, par exemple :
        student = etudiant(None, self.cinF.get(), self.cneF.get(),self.nomF.get(), self.prenomF.get(), self.dateF.get(),
                           self.numF.get(), self.mailF.get(), self.filiereF.get(), self.nivF)
        self.controller.addStudent(student)
        self.loadStudents()
        self.clearForm()

    def updateStudent(self):
        selected_item = self.tree.selection()
        if not selected_item:
            print("Aucun étudiant sélectionné")
            messagebox.showinfo("Erreur", "Aucun étudiant sélectionné")
            return
        cin_etd = self.cinF.get()
        cne_etd = self.cneF.get()
        nom_etd = self.nomF.get()
        prenom_etd = self.prenomF.get()
        date_n_etd = self.dateF.get()
        num_etd = self.numF.get()
        mail_etd = self.mailF.get()
        filiere = self.filiereF.get()
        id_niv = self.nivF.get()
        values = self.tree.item(selected_item, 'values')
        id_etd = values[0]
        if not (cin_etd and cne_etd and nom_etd and prenom_etd and date_n_etd and num_etd and mail_etd and filiere and id_niv):
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        student = etudiant(
            id_etd=int(id_etd),
            cin_etd=cin_etd,
            cne_etd=cne_etd,
            nom_etd=nom_etd,
            prenom_etd=prenom_etd,
            date_n_etd=date_n_etd,
            num_etd=int(num_etd),
            mail_etd=mail_etd,
            filiere=filiere,
            id_niv=id_niv
        )

        self.controller.updateStudent(student)

        # Recharger la liste des étudiants et effacer le formulaire
        self.loadStudents()
        self.clearForm()
        messagebox.showinfo("Succès", "Étudiant modifié avec succès.")


    def deletestudent(self):
        print("delete student")
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_etd = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deleteStudent(id_etd)
            self.loadStudents()
            self.clearForm()



        else:
            print("No student selected")
            messagebox.showinfo("Error", "No student selected")

    def fillForm(self, student):
        self.clearForm()
        self.cinF.insert(0, student.cin)
        self.cneF.insert(0, student.cne)
        self.nomF.insert(0, student.nom)
        self.prenomF.insert(0, student.prenom)
        self.dateF.insert(0, student.date_naissance)
        self.numF.insert(0, student.numero)
        self.mailF.insert(0, student.email)
        self.filiereF.insert(0, student.filiere)
        self.nivF.insert(0, student.niv)


    def clearForm(self):
        self.cinF.delete(0, END)
        self.cneF.delete(0, END)
        self.nomF.delete(0, END)
        self.prenomF.delete(0, END)
        self.dateF.delete(0, END)
        self.numF.delete(0, END)
        self.mailF.delete(0, END)
        self.filiereF.delete(0, END)
        self.nivF.delete(0, END)
        self.idF = None


    def Table(self):
        """
        Initialise le tableau des étudiants avec colonnes et barre de défilement.
        """
        # Création du Treeview
        self.tree = ttk.Treeview(self.root, columns=(
            "id_etd", "cin_etd", "cne_etd", "nom_etd", "prenom_etd", "date_n_etd", "num_etd", "mail_etd", "filiere", "id_niv"
        ), show="headings", height=5)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_etd", text="ID étudiant")
        self.tree.heading("cin_etd", text="CIN")
        self.tree.heading("cne_etd", text="CNE")
        self.tree.heading("nom_etd", text="Nom")
        self.tree.heading("prenom_etd", text="Prénom")
        self.tree.heading("date_n_etd", text="Date de naissance")
        self.tree.heading("num_etd", text="Numéro Tel")
        self.tree.heading("mail_etd", text="Mail")
        self.tree.heading("filiere", text="Filière")
        self.tree.heading("id_niv", text="ID niveau")


        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_etd", width=80, anchor="center")
        self.tree.column("cin_etd", width=90, anchor="center")
        self.tree.column("cne_etd", width=90, anchor="center")
        self.tree.column("nom_etd", width=90, anchor="center")
        self.tree.column("prenom_etd", width=90, anchor="center")
        self.tree.column("date_n_etd", width=90, anchor="center")
        self.tree.column("num_etd", width=100, anchor="center")
        self.tree.column("mail_etd", width=100, anchor="center")
        self.tree.column("filiere", width=90, anchor="center")
        self.tree.column("id_niv", width=80, anchor="center")


        # Ajout d'une barre de défilement verticale
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Placement du Treeview et de la barre de défilement
        self.tree.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=10)

        # Définition des styles pour les lignes
        self.tree.tag_configure("evenrow", background="#ffffff")
        self.tree.tag_configure("oddrow", background="#f0f0f0")

        # Placement dans un canvas si nécessaire
        if self.canvas:
            self.canvas.create_window(450.0, 266.0, window=self.tree)

        # Liaison de l'événement de clic sur une ligne
        self.tree.bind("<ButtonRelease-1>", self.onRowClick)

    def onRowClick(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0])
            student_data = item_data["values"]
            student_id = student_data[0]
            student = self.controller.getStudentById(student_id)
            print("Étudiant sélectionné :", student_data)
            self.fillForm(student)
