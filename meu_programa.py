from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button1 = Button(text='Botão 1')
        button2 = Button(text='Botão 2')
        layout.add_widget(button1)
        layout.add_widget(button2)
        return layout

if __name__ == '__main__':
    MeuApp().run()
