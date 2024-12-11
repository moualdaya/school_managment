from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

class App:
    def __init__(self):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\ayamo\OneDrive\Bureau\student_1\student_1\assets\student")

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

    def setup_ui(self):
        # Adding images
        self.add_image("image_1.png", 450.0, 253.0)
        self.add_image("image_2.png", 505.0, 70.0)
        self.add_image("image_3.png", 391.0, 407.0)

        # Adding entries
        self.add_entry(524.0, 454.0, 135.0, 14.0, "entry_1.png", 591.5, 462.0) #id filiere
        self.add_entry(524.0, 426.0, 135.0, 14.0, "entry_2.png", 591.5, 434.0) #id niveau
        self.add_entry(524.0, 398.0, 135.0, 13.0, "entry_3.png", 591.5, 405.5) #email
        self.add_entry(524.0, 369.0, 135.0, 14.0, "entry_4.png", 591.5, 377.0) #numero
        self.add_entry(524.0, 341.0, 135.0, 14.0, "entry_5.png", 591.5, 349.0) #date de naissance

        self.add_entry(141.0, 454.0, 135.0, 14.0, "entry_6.png", 208.5, 462.0) #prenom
        self.add_entry(141.0, 426.0, 135.0, 14.0, "entry_7.png", 208.5, 434.0) #nom
        self.add_entry(141.0, 398.0, 135.0, 13.0, "entry_8.png", 208.5, 405.5) #cne
        self.add_entry(141.0, 369.0, 135.0, 14.0, "entry_9.png", 208.5, 377.0) #cin
        self.add_entry(141.0, 341.0, 135.0, 14.0, "entry_10.png", 208.5, 349.0)  #id

        self.add_entry(111.0, 141.0, 676.0, 22.0, "entry_11.png", 449.0, 153.0) #barre de recherche

        # Adding buttons
        self.add_button(784.0, 348.0, 87.0, 22.0, "button_1.png", "button_1 clicked") #ajouter
        self.add_button(784.0, 387.0, 87.0, 22.0, "button_2.png", "button_2 clicked") #modifier
        self.add_button(783.0, 433.0, 87.0, 22.0, "button_3.png", "button_3 clicked") #supprimer
        self.add_button(792.0, 141.0, 87.0, 23.0, "button_4.png", "button_4 clicked") #rechercher
        self.add_button(13.0, 12.0, 80.0, 25.0, "button_5.png", "button_5 clicked")  #menu
        self.add_button(16.0, 141.0, 94.0, 23.0, "button_6.png", "button_6 clicked") #id

        self.window.resizable(False, False)

    def add_image(self, file_name, x, y):
        image_path = self.relative_to_assets(file_name)
        if image_path.exists():
            image = PhotoImage(file=image_path)
            self.images[file_name] = image  # Store reference
            self.canvas.create_image(x, y, image=image)
        else:
            print(f"Image file {file_name} not found at {image_path}")

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

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
