from nicegui import ui
from simpleeval import simple_eval
import ast


class Calculator:
    def __init__(self):
        self.data = ''
        self.setup_gui()

    def add_data(self, data_to_add) -> None:
        self.data += data_to_add
        print(data_to_add, self.data)

    def remove_data(self, remove_all=None) -> None:
        if remove_all:
            self.data = ''
        else:
            self.data = self.data[:-1]

    def calculate(self):
        try:
            self.data = simple_eval(self.data)
        except SyntaxError:
            ui.notify('The operation is not possible')
        except Exception as error:
            ui.notify(f'error {error}')

    def setup_gui(self) -> None:
        with ui.card().classes('flex mx-auto mt-40'):
            ui.input().bind_value(self, 'data').props(
                'outlined input-style="text-align:right"').tailwind('min-w-full')
            with ui.grid(columns=5):
                # doesn't work yet, need to add custom operator
                ui.button('\u221A')
                ui.button('MC')
                ui.button('MR')
                ui.button('M-')
                ui.button('M+')
                # ///////////////
                ui.button('%', on_click=lambda: self.add_data('%'))
                ui.button('7', on_click=lambda: self.add_data('7'))
                ui.button('8', on_click=lambda: self.add_data('8'))
                ui.button('9', on_click=lambda: self.add_data('9'))
                # doesn't work yet, need to add custom operator
                ui.button('\u00F7')
                # ////////////
                ui.button('\u00B1')
                ui.button('4', on_click=lambda: self.add_data('4'))
                ui.button('5', on_click=lambda: self.add_data('5'))
                ui.button('6', on_click=lambda: self.add_data('6'))
                ui.button('X')  # doesn't work yet, need to add custom operator
                # ////////////
                ui.button('C', on_click=self.remove_data)
                ui.button('1', on_click=lambda: self.add_data('1'))
                ui.button('2', on_click=lambda: self.add_data('2'))
                ui.button('3', on_click=lambda: self.add_data('3'))
                ui.button('-', on_click=lambda: self.add_data('-'))
                # ////////////
                ui.button('CE', on_click=lambda: self.remove_data(True))
                ui.button('0', on_click=lambda: self.add_data('0'))
                ui.button('\u00B7', on_click=lambda: self.add_data('.'))
                ui.button('=', on_click=self.calculate)
                ui.button('+', on_click=lambda: self.add_data('+'))


calculator = Calculator()

ui.run(title='Calculator', dark=True)
