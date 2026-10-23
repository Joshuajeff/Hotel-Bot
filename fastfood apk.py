import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text='Name'))
        self.info = TextInput()
        self.add_widget(self.info)

        self.add_widget(Label(text='Age'))
        self.age_details = TextInput()
        self.add_widget(self.age_details)

        self.add_widget(Label(text='Language'))
        self.language_info = TextInput()
        self.add_widget(self.language_info)

        self.press = Button(text = 'click me')
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    def click_me(self, instance):
        print("Name is " +self.info.text)
        print(f"Age is " +self.age_details.text)
        print(f"Language is " +self.language_info.text)
        print("")

class parentApp(App):
    def build(self):
        return childApp()


if __name__ == "__main__":
    parentApp().run()
