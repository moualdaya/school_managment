
class etudiant:
    def __init__(self, id_etd, cin_etd, cne_etd, nom_etd, prenom_etd, date_n_etd, num_etd, mail_etd, filiere, id_niv):
        self.id = id_etd
        self.cin = cin_etd
        self.cne = cne_etd
        self.nom = nom_etd
        self.prenom = prenom_etd
        self.date_naissance = date_n_etd
        self.numero = num_etd
        self.email = mail_etd
        self.filiere = filiere
        self.niv = id_niv
    def getValues(self):
        return self.id, self.cin, self.cne, self.nom, self.prenom, self.date_naissance, self.numero, self.email, self.filiere, self.niv