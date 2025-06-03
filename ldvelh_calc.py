import ldvelh_gui as gui
import random

def monkeypatch():
    """gui.LDVELH_gui.instances = []
    def __init__(self, *args, **kwargs):
        gui.LDVELH_gui.instances.append(self)
        print("\nLDVELH_gui instances n°"+str(len(gui.LDVELH_gui.instances)))
        print(gui.LDVELH_gui.instances)
        if not 'editing_mode' in kwargs.keys():
            super(gui.LDVELH_gui, self).__init__(*args, static_file_path={'my_res':'./res/'})
    gui.LDVELH_gui.__init__=__init__"""
    
    def get_widget(self):
        # dictionnaire pour accès simple aux widgets
        self.widget={"textinput_habilte":self.vbox0.children["hbox0"].children["textinput_habilte"],
                     "textinput_endurance":self.vbox0.children["hbox0"].children["textinput_endurance"],
                     "textinput_chance":self.vbox0.children["hbox0"].children["textinput_chance"],
                     "textinput_habilte_monstre":self.vbox0.children["hbox1"].children["textinput_habilte_monstre"],
                     "textinput_endurance_monstre":self.vbox0.children["hbox1"].children["textinput_endurance_monstre"],
                     "console":self.vbox0.children["listview_console"] 
            }
    gui.LDVELH_gui.get_widget=get_widget
    
    def main(self):
        ret=gui.LDVELH_gui.construct_ui(self)
        global joueur
        joueur=Joueur(name="joueur",gui=self)
        global monstre
        monstre=Monstre(name="monstre",gui=self)
        self.get_widget()
        self.console=[]
        self.vainqueur=None
        self._HAB=2 #constantes magiques pour & binaire (cf write_gui)
        self._END=4
        self._CHA=8
        return ret
    gui.LDVELH_gui.main=main
    
    def console_write(self,text:str):
        # écrit dans le widget console texte en haut en vidant et recréant
        self.console.insert(0,text)
        self.widget["console"].empty()
        for item in self.console:
            self.widget["console"].append(item)
    gui.LDVELH_gui.console_write=console_write
    
    # definir les signaux dans l'éditeur (App -> signal nom du widget)
    # puis définir ici la fonction qui capte le signal et l'ajouter à la classe LDVELH_gui
    
    def onclick_button_exit(self,widget):
        self.execute_javascript("window.close();")
        self.close()
    gui.LDVELH_gui.onclick_button_exit=onclick_button_exit
    
    def onclick_button_combatre(self, emitter):
        try:
            monstre.read_gui()
            joueur.read_gui()
        except:
            print("onclic read error")
            return
        test_vie:bool=monstre.test_life() #si on fait un test normal ça ne teste pas les éléments après false.
        test_vie2:bool=joueur.test_life()
        if not (test_vie and test_vie2): #si l'un au moins est DCD
            return
        monstre.init_FA()
        joueur.init_FA()
        if joueur.FA > monstre.FA:
            self.console_write(f"{joueur.name} (FA:{joueur.FA}={joueur.habilete}+{joueur.dernier_de}) blesse le {monstre.name} (FA:{monstre.FA}={monstre.habilete}+{monstre.dernier_de})")
            self.console_write(f"{monstre.name} perd 2 d'endurance : {monstre.endurance} -> {monstre.endurance-2}")
            monstre.endurance-=2
            monstre.write_gui(self._END)
            self.vainqueur=joueur
        elif joueur.FA < monstre.FA:
            self.console_write(f"{monstre.name} (FA:{monstre.FA}={monstre.habilete}+{monstre.dernier_de}) blesse {joueur.name} (FA:{joueur.FA}={joueur.habilete}+{joueur.dernier_de})")
            self.console_write(f"{joueur.name} perd 2 d'endurance : {joueur.endurance} -> {joueur.endurance-2}")
            joueur.endurance-=2
            joueur.write_gui(self._END)
            self.vainqueur=monstre
        elif joueur.FA == monstre.FA:
            self.console_write(f"Esquive mutuelle ! (FA:{joueur.FA})")
            self.vainqueur=None
    gui.LDVELH_gui.onclick_button_combatre=onclick_button_combatre

    def onclick_button_chance(self, emitter):
        if self.vainqueur==None:
            return
        if joueur.de_2D6() <= joueur.chance:
            self.console_write(f"Vous êtes chanceux ! ({joueur.dernier_de} <= {joueur.chance})")
            if self.vainqueur == joueur:
                self.console_write(f"La blessure infligée était grave (endurance de {monstre.name} {monstre.endurance}->{monstre.endurance-2})")
                monstre.endurance-=2
                monstre.write_gui(self._END)
            else:
                self.console_write(f"Vous avez réussi à atténuer le coup reçu (endurance de {joueur.name} {joueur.endurance}->{joueur.endurance+1})")
                joueur.endurance+=1
                joueur.write_gui(self._END)
        else:
            self.console_write(f"Vous êtes malchanceux !({joueur.dernier_de} > {joueur.chance}")
            if self.vainqueur == joueur:
                self.console_write(f"La blessure infligée était une écorchure (endurance de {monstre.name} {monstre.endurance}->{monstre.endurance+1})")
                monstre.endurance+=1
                monstre.write_gui(self._END)
            else:
                self.console_write(f"Le coup reçu était vraiment grave (endurance de {joueur.name} {joueur.endurance}->{joueur.endurance-1})")
                joueur.endurance-=1
                joueur.write_gui(self._END)
        self.vainqueur=None #sert à désactiver le bouton chance
        joueur.chance-=1
        joueur.write_gui(self._CHA)
    gui.LDVELH_gui.onclick_button_chance=onclick_button_chance
    
    def onclick_button_raz(self, emitter):
        print("console effacée")
        self.widget["console"].empty()
        self.console=[]
    gui.LDVELH_gui.onclick_button_raz=onclick_button_raz
    
    
class Monstre():
    __slots__='habilete','endurance','FA','g','name','dernier_de'
    def __init__(self,name,gui):
        self.habilete:int = 0
        self.endurance:int = 0
        self.FA:int = 0
        self.dernier_de:int=0
        self.name=name
        self.g=gui #g instance of gui
    def read_gui(self):
        try:
            self.habilete=int(self.g.widget["textinput_habilte_monstre"].get_text())
            self.endurance=int(self.g.widget["textinput_endurance_monstre"].get_text())
        except ValueError:
            self.g.console_write(f"{self.name}:erreur de saisie")
            raise ValueError
    def de_2D6(self)->int:
        a=random.randrange(1,6)
        b=random.randrange(1,6)
        self.dernier_de=a+b
        self.g.console_write(f"{self.name}: 2D6={self.dernier_de} ({a}+{b})")
        return self.dernier_de
    def init_FA(self):
        self.FA=self.habilete+self.de_2D6()
    def write_gui(self,cible =6):
        if 2 & cible :
            self.g.widget["textinput_habilte_monstre"].set_text(str(self.habilete))
        if 4 & cible :
            self.g.widget["textinput_endurance_monstre"].set_text(str(self.endurance))
    def test_life(self)->bool:
        if self.endurance <=0:
            self.g.console_write(f"{self.name} est mort.")
            return False
        else:
            return True
        
class Joueur(Monstre):
    __slots__="chance"
    def __init__(self,name,gui):
        super().__init__(name,gui)
        self.chance:int=0
    def read_gui(self):
        try:
            self.habilete=int(self.g.widget["textinput_habilte"].get_text())
            self.endurance=int(self.g.widget["textinput_endurance"].get_text())
            self.chance=int(self.g.widget["textinput_chance"].get_text())
        except ValueError:
            self.g.console_write(f"{self.name}:erreur de saisie")
            raise ValueError
    def write_gui(self, cible =14):
        if 2 & cible:
            self.g.widget["textinput_habilte"].set_text(str(self.habilete))
        if 4 & cible:
            self.g.widget["textinput_endurance"].set_text(str(self.endurance))
        if 8 & cible:
            self.g.widget["textinput_chance"].set_text(str(self.chance))


def main():
    monkeypatch()
    
    gui.start(gui.LDVELH_gui,
              address=gui.configuration['config_address'],
              port=gui.configuration['config_port'], 
              multiple_instance=gui.configuration['config_multiple_instance'], 
              enable_file_cache=gui.configuration['config_enable_file_cache'],
              start_browser=gui.configuration['config_start_browser'])

main()

