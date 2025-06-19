from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image

# Регистрируем шрифт
LabelBase.register(name='MyFont', fn_regular='fonts/Symbola.ttf')

# Алфавит
custom_alphabet = {
    'а': '⫮', 'б': '⫱', 'в': '⫶', 'г': '⫰', 'д': '⫭', 'е': '⫪', 'ё': '⫕',
    'ж': '⫣', 'з': '⫦', 'и': '⫩', 'й': '⫠', 'к': '⫝', 'л': '⫚', 'м': '⫛',
    'н': '⪾', 'о': '⫀', 'п': '⩫', 'р': '⩜', 'с': '⩛', 'т': '⩚', 'у': '⩊',
    'ф': '⩖', 'х': '⩙', 'ц': '⩕', 'ч': '⩒', 'ш': '⩑', 'щ': '⨑', 'ъ': '⨎',
    'ы': '⨏', 'ь': '⨪', 'э': '⨫', 'ю': '⫏', 'я': '⫒'
}
reverse_alphabet = {v: k for k, v in custom_alphabet.items()}


class TranslatorApp(App):
    def build(self):
        self.is_custom = True
        self.dark_theme = True
        self.set_theme()

        root_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)

        # Верхняя панель
        top_bar = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, padding=[10, 10, 10, 10], spacing=10)

        # Логотип + название
        logo_layout = BoxLayout(orientation='horizontal', size_hint_x=0.25, spacing=10)
        icon = Image(source='icon.png', size_hint=(None, None), size=(40, 40))  # PNG иконка рядом с этим файлом

        # Сделали self.logo_text, чтобы менять цвет из других методов
        self.logo_text = Label(
            text='SHIFRA',
            font_name='MyFont',
            font_size=25,
            color=self.text_color,
            size_hint_y=None,
            height=40
        )
        logo_layout.add_widget(icon)
        logo_layout.add_widget(self.logo_text)

        # Тема (ползунок)
        self.theme_toggle = ToggleButton(
            text='🌙',
            size_hint=(None, None),
            size=(60, 40),
            background_color=self.button_bg,
            color=self.button_text_color,
            font_name='MyFont'
        )
        self.theme_toggle.bind(on_press=self.toggle_theme)

        top_bar.add_widget(logo_layout)
        top_bar.add_widget(BoxLayout())  # пустое пространство
        top_bar.add_widget(self.theme_toggle)

        # Поле ввода
        self.input_text = TextInput(
            hint_text="Введите текст...",
            multiline=True,
            font_name='MyFont',
            size_hint_y=0.3,
            background_color=self.input_bg,
            foreground_color=self.text_color,
            cursor_color=self.text_color,
            padding=[10, 10]
        )

        # Кнопки
        self.translate_button = Button(
            text="Перевести на шифр",
            font_name='MyFont',
            size_hint_y=0.1,
            background_color=self.button_bg,
            color=self.button_text_color
        )
        self.translate_button.bind(on_press=self.translate)

        self.switch_button = Button(
            text="🔁 Сменить направление",
            font_name='MyFont',
            size_hint_y=0.1,
            background_color=self.button_bg,
            color=self.button_text_color
        )
        self.switch_button.bind(on_press=self.switch_direction)

        # Поле вывода (копируемый текст)
        self.output_text = TextInput(
            text='',
            readonly=True,
            multiline=True,
            font_name='MyFont',
            font_size=20,
            size_hint_y=0.3,
            background_color=self.input_bg,
            foreground_color=self.text_color,
            cursor_color=(0, 0, 0, 0),
            cursor_width=0,
            padding=[10, 10]
        )

        # Добавляем элементы
        root_layout.add_widget(top_bar)
        root_layout.add_widget(self.input_text)
        root_layout.add_widget(self.translate_button)
        root_layout.add_widget(self.switch_button)
        root_layout.add_widget(self.output_text)

        return root_layout

    def on_start(self):
        self.root_window.clearcolor = self.bg_color

    def translate(self, instance):
        text = self.input_text.text
        if self.is_custom:
            translated = ''.join(custom_alphabet.get(c, c) for c in text.lower())
        else:
            translated = ''.join(reverse_alphabet.get(c, c) for c in text.lower())
        self.output_text.text = translated

    def switch_direction(self, instance):
        self.is_custom = not self.is_custom
        self.translate_button.text = (
            "Перевести на шифр" if self.is_custom else "Перевести на русский"
        )
        self.input_text.text = ""
        self.output_text.text = ""

    def toggle_theme(self, instance):
        self.dark_theme = not self.dark_theme
        self.set_theme()

        self.root_window.clearcolor = self.bg_color
        self.input_text.background_color = self.input_bg
        self.input_text.foreground_color = self.text_color
        self.input_text.cursor_color = self.text_color
        self.output_text.background_color = self.input_bg
        self.output_text.foreground_color = self.text_color

        self.theme_toggle.background_color = self.button_bg
        self.theme_toggle.color = self.button_text_color
        self.theme_toggle.text = '🌙' if self.dark_theme else '☀️'

        self.translate_button.background_color = self.button_bg
        self.translate_button.color = self.button_text_color
        self.switch_button.background_color = self.button_bg
        self.switch_button.color = self.button_text_color

        # Обновляем цвет надписи SHIFRA
        self.logo_text.color = self.text_color

    def set_theme(self):
        if self.dark_theme:
            self.bg_color = (0.1, 0.1, 0.1, 1)
            self.input_bg = (0.2, 0.2, 0.2, 1)
            self.text_color = (1, 1, 1, 1)
            self.button_bg = (0.4, 0.4, 0.8, 1)
            self.button_text_color = (1, 1, 1, 1)
        else:
            self.bg_color = (1, 1, 1, 1)
            self.input_bg = (0.95, 0.95, 0.95, 1)
            self.text_color = (0, 0, 0, 1)
            self.button_bg = (0.2, 0.4, 1, 1)
            self.button_text_color = (1, 1, 1, 1)


if __name__ == '__main__':
    TranslatorApp().run()







