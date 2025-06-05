
# -*- coding: utf-8 -*-

from remi.gui import *
from remi import start, App


class LDVELH_gui(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(LDVELH_gui, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return LDVELH_gui.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        vbox0 = VBox()
        vbox0.attr_class = "VBox"
        vbox0.attr_editor_newclass = False
        vbox0.css_align_items = "flex-start"
        vbox0.css_display = "flex"
        vbox0.css_flex_direction = "column"
        vbox0.css_height = "100%"
        vbox0.css_justify_content = "space-around"
        vbox0.css_left = "1px"
        vbox0.css_position = "absolute"
        vbox0.css_top = "0px"
        vbox0.css_width = "100%"
        vbox0.variable_name = "vbox0"
        label0 = Label()
        label0.attr_class = "Label"
        label0.attr_editor_newclass = False
        label0.css_font_weight = "bolder"
        label0.css_height = "3%"
        label0.css_order = "-1"
        label0.css_position = "static"
        label0.css_top = "20px"
        label0.css_width = "5%"
        label0.text = "joueur"
        label0.variable_name = "label0"
        vbox0.append(label0,'label0')
        hbox0 = HBox()
        hbox0.attr_class = "HBox"
        hbox0.attr_editor_newclass = False
        hbox0.css_align_items = "center"
        hbox0.css_display = "flex"
        hbox0.css_flex_direction = "row"
        hbox0.css_height = "5%"
        hbox0.css_justify_content = "space-around"
        hbox0.css_order = "-1"
        hbox0.css_position = "static"
        hbox0.css_top = "20px"
        hbox0.css_width = "100%"
        hbox0.variable_name = "hbox0"
        label1 = Label()
        label1.attr_class = "Label"
        label1.attr_editor_newclass = False
        label1.css_height = "30px"
        label1.css_order = "-1"
        label1.css_position = "static"
        label1.css_top = "20px"
        label1.css_width = "10%"
        label1.text = "habileté"
        label1.variable_name = "label1"
        hbox0.append(label1,'label1')
        textinput_habilte = Input(input_type="number")
        textinput_habilte.attr_class = "Input"
        textinput_habilte.attr_editor_newclass = False
        textinput_habilte.attr_maxlength = "3"
        textinput_habilte.css_height = "20px"
        textinput_habilte.css_order = "-1"
        textinput_habilte.css_position = "static"
        textinput_habilte.css_top = "20px"
        textinput_habilte.css_width = "10%"
        textinput_habilte.text = ""
        textinput_habilte.variable_name = "textinput_habilte"
        hbox0.append(textinput_habilte,'textinput_habilte')
        label2 = Label()
        label2.attr_class = "Label"
        label2.attr_editor_newclass = False
        label2.css_height = "30px"
        label2.css_order = "-1"
        label2.css_position = "static"
        label2.css_top = "20px"
        label2.css_width = "15%"
        label2.text = "endurance"
        label2.variable_name = "label2"
        hbox0.append(label2,'label2')
        textinput_endurance = Input(input_type="number")
        textinput_endurance.attr_class = "Input"
        textinput_endurance.attr_editor_newclass = False
        textinput_endurance.attr_maxlength = "3"
        textinput_endurance.css_height = "20px"
        textinput_endurance.css_order = "-1"
        textinput_endurance.css_position = "static"
        textinput_endurance.css_top = "20px"
        textinput_endurance.css_width = "10%"
        textinput_endurance.text = ""
        textinput_endurance.variable_name = "textinput_endurance"
        hbox0.append(textinput_endurance,'textinput_endurance')
        label3 = Label()
        label3.attr_class = "Label"
        label3.attr_editor_newclass = False
        label3.css_height = "30px"
        label3.css_order = "-1"
        label3.css_position = "static"
        label3.css_top = "20px"
        label3.css_width = "10%"
        label3.text = "chance"
        label3.variable_name = "label3"
        hbox0.append(label3,'label3')
        textinput_chance = Input(input_type="number")
        textinput_chance.attr_class = "Input"
        textinput_chance.attr_editor_newclass = False
        textinput_chance.attr_maxlength = "3"
        textinput_chance.css_height = "20px"
        textinput_chance.css_order = "-1"
        textinput_chance.css_position = "static"
        textinput_chance.css_top = "20px"
        textinput_chance.css_width = "10%"
        textinput_chance.text = ""
        textinput_chance.variable_name = "textinput_chance"
        hbox0.append(textinput_chance,'textinput_chance')
        vbox0.append(hbox0,'hbox0')
        label4 = Label()
        label4.attr_class = "Label"
        label4.attr_editor_newclass = False
        label4.css_font_weight = "bolder"
        label4.css_height = "3%"
        label4.css_order = "-1"
        label4.css_position = "static"
        label4.css_top = "20px"
        label4.css_width = "5%"
        label4.text = "monstre"
        label4.variable_name = "label4"
        vbox0.append(label4,'label4')
        hbox1 = HBox()
        hbox1.attr_class = "HBox"
        hbox1.attr_editor_newclass = False
        hbox1.css_align_items = "center"
        hbox1.css_display = "flex"
        hbox1.css_flex_direction = "row"
        hbox1.css_height = "5%"
        hbox1.css_justify_content = "space-around"
        hbox1.css_order = "-1"
        hbox1.css_position = "static"
        hbox1.css_top = "20px"
        hbox1.css_width = "100%"
        hbox1.variable_name = "hbox1"
        label5 = Label()
        label5.attr_class = "Label"
        label5.attr_editor_newclass = False
        label5.css_height = "30px"
        label5.css_order = "-1"
        label5.css_position = "static"
        label5.css_top = "20px"
        label5.css_width = "10%"
        label5.text = "habileté"
        label5.variable_name = "label5"
        hbox1.append(label5,'label5')
        textinput_habilte_monstre = Input(input_type="number")
        textinput_habilte_monstre.attr_class = "Input"
        textinput_habilte_monstre.attr_editor_newclass = False
        textinput_habilte_monstre.attr_maxlength = "3"
        textinput_habilte_monstre.css_height = "20px"
        textinput_habilte_monstre.css_order = "-1"
        textinput_habilte_monstre.css_position = "static"
        textinput_habilte_monstre.css_top = "20px"
        textinput_habilte_monstre.css_width = "10%"
        textinput_habilte_monstre.text = ""
        textinput_habilte_monstre.variable_name = "textinput_habilte_monstre"
        hbox1.append(textinput_habilte_monstre,'textinput_habilte_monstre')
        label6 = Label()
        label6.attr_class = "Label"
        label6.attr_editor_newclass = False
        label6.css_height = "30px"
        label6.css_order = "-1"
        label6.css_position = "static"
        label6.css_top = "20px"
        label6.css_width = "10%"
        label6.text = "endurance"
        label6.variable_name = "label6"
        hbox1.append(label6,'label6')
        textinput_endurance_monstre = Input(input_type="number")
        textinput_endurance_monstre.attr_class = "Input"
        textinput_endurance_monstre.attr_editor_newclass = False
        textinput_endurance_monstre.attr_maxlength = "3"
        textinput_endurance_monstre.css_height = "20px"
        textinput_endurance_monstre.css_order = "-1"
        textinput_endurance_monstre.css_position = "static"
        textinput_endurance_monstre.css_top = "20px"
        textinput_endurance_monstre.css_width = "10%"
        textinput_endurance_monstre.text = ""
        textinput_endurance_monstre.variable_name = "textinput_endurance_monstre"
        hbox1.append(textinput_endurance_monstre,'textinput_endurance_monstre')
        vbox0.append(hbox1,'hbox1')
        hbox2 = HBox()
        hbox2.attr_class = "HBox"
        hbox2.attr_editor_newclass = False
        hbox2.css_align_items = "center"
        hbox2.css_display = "flex"
        hbox2.css_flex_direction = "row"
        hbox2.css_height = "5%"
        hbox2.css_justify_content = "space-around"
        hbox2.css_order = "-1"
        hbox2.css_position = "static"
        hbox2.css_top = "20px"
        hbox2.css_width = "100%"
        hbox2.variable_name = "hbox2"
        button_combatre = Button()
        button_combatre.attr_class = "Button"
        button_combatre.attr_editor_newclass = False
        button_combatre.css_height = "30px"
        button_combatre.css_order = "-1"
        button_combatre.css_position = "static"
        button_combatre.css_top = "20px"
        button_combatre.css_width = "20%"
        button_combatre.text = "combatre"
        button_combatre.variable_name = "button_combatre"
        hbox2.append(button_combatre,'button_combatre')
        button_chance = Button()
        button_chance.attr_class = "Button"
        button_chance.attr_editor_newclass = False
        button_chance.css_height = "30px"
        button_chance.css_order = "-1"
        button_chance.css_position = "static"
        button_chance.css_top = "20px"
        button_chance.css_width = "20%"
        button_chance.text = "chance"
        button_chance.variable_name = "button_chance"
        hbox2.append(button_chance,'button_chance')
        button_raz = Button()
        button_raz.attr_class = "Button"
        button_raz.attr_editor_newclass = False
        button_raz.css_height = "30px"
        button_raz.css_order = "-1"
        button_raz.css_position = "static"
        button_raz.css_top = "20px"
        button_raz.css_width = "10%"
        button_raz.text = "RAZ"
        button_raz.variable_name = "button_raz"
        hbox2.append(button_raz,'button_raz')
        vbox0.append(hbox2,'hbox2')
        listview_console = ListView()
        listview_console.attr_class = "ListView"
        listview_console.attr_editor_newclass = False
        listview_console.css_height = "76%"
        listview_console.css_order = "547045974800"
        listview_console.css_position = "static"
        listview_console.css_top = "20px"
        listview_console.css_width = "100%"
        listview_console.variable_name = "listview_console"
        vbox0.append(listview_console,'listview_console')
        button_exit = Button()
        button_exit.attr_class = "Button"
        button_exit.attr_editor_newclass = False
        button_exit.css_height = "30px"
        button_exit.css_order = "547585659856"
        button_exit.css_position = "static"
        button_exit.css_top = "3%"
        button_exit.css_width = "15%"
        button_exit.text = "exit"
        button_exit.variable_name = "button_exit"
        vbox0.append(button_exit,'button_exit')
        vbox0.children['hbox2'].children['button_combatre'].onclick.do(self.onclick_button_combatre)
        vbox0.children['hbox2'].children['button_chance'].onclick.do(self.onclick_button_chance)
        vbox0.children['hbox2'].children['button_raz'].onclick.do(self.onclick_button_raz)
        vbox0.children['button_exit'].onclick.do(self.onclick_button_exit)
        

        self.vbox0 = vbox0
        return self.vbox0
    
    def onclick_button_combatre(self, emitter):
        pass
    def onclick_button_chance(self, emitter):
        pass
    def onclick_button_raz(self, emitter):
        pass
    def onclick_button_exit(self, emitter):
        pass


#Configuration
configuration = {'config_project_name': 'LDVELH_gui', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(LDVELH_gui, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
