from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

class Calculator(App):

    def update(self):
        self.l.text = self.string
    def get(self, instance):
        if self.string =='0':
            self.string = ''
        self.string += str(instance.text)
        self.update()
    def get_operation(self, instance):
        ops = '+-/*%'
        if self.string[len(self.string) - 1] in ops:
            self.update()
        else:
            self.string += str(instance.text)
            self.update()

    def calc(self, instance):
        self.string = str(eval(f'{self.string}'))
        self.update()
    def clear(self, instance):
        self.string='0'
        self.update()

    def build(self):
        self.string = '0'
    #layouts
        mainlayout = BoxLayout(orientation='vertical')
        sublayout = BoxLayout(orientation='horizontal')
        lbl = AnchorLayout(anchor_x='right', anchor_y='bottom')
        ops = GridLayout(cols=2, rows=4)
        btn = GridLayout(cols=3, rows=4)
    #screen
        self.l = Label(text='0', font_size=52, font_name='Bahnschrift', halign='right')
        lbl.add_widget(self.l)
        mainlayout.add_widget(lbl)
    #numbers buttons
        btn.add_widget(Button(text='9', on_press=self.get))
        btn.add_widget(Button(text='8', on_press=self.get))
        btn.add_widget(Button(text='7', on_press=self.get))
        btn.add_widget(Button(text='6', on_press=self.get))
        btn.add_widget(Button(text='5', on_press=self.get))
        btn.add_widget(Button(text='4', on_press=self.get))
        btn.add_widget(Button(text='3', on_press=self.get))
        btn.add_widget(Button(text='2', on_press=self.get))
        btn.add_widget(Button(text='1', on_press=self.get))
        btn.add_widget(Button(text='.', on_press=self.get))
        btn.add_widget(Button(text='0', on_press=self.get))
        btn.add_widget(Button(text='Enter', background_color= [4, 2, 0, 1], on_press=self.calc))
    #operation buttons
        ops.add_widget(Button(text='+', background_color= [4, 2, 0, 1], on_press=self.get_operation))
        ops.add_widget(Button(text='-', background_color= [4, 2, 0, 1], on_press=self.get_operation))
        ops.add_widget(Button(text='*', background_color= [4, 2, 0, 1], on_press=self.get_operation))
        ops.add_widget(Button(text='/', background_color= [4, 2, 0, 1], on_press=self.get_operation))
        ops.add_widget(Button(text='Clear', background_color=[4, 2, 0, 1], on_press=self.clear))
        ops.add_widget(Button(text='%', background_color=[4, 2, 0, 1], on_press=self.get_operation))
    #merging layouts
        sublayout.add_widget(btn)
        sublayout.add_widget(ops)
        mainlayout.add_widget(sublayout)
        return mainlayout

if __name__ == '__main__':
    calc = Calculator()
    calc.run()