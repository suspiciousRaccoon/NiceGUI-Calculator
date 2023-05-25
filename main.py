from nicegui import ui


class Calculator:
    def __init__(self):
        self.data = ''
        self.setup_gui()

    def add_data(self, data_to_add) -> None:
        self.data += data_to_add
        print(data_to_add, self.data)

    def setup_gui(self) -> None:
        with ui.card().classes('flex'):
            ui.input().props('outlined').tailwind('min-w-full')
            with ui.grid(columns=5):
                ui.button('\u221A')
                ui.button('MC')
                ui.button('MR')
                ui.button('M-')
                ui.button('M+')
                # ///////////////
                ui.button('%')
                ui.button('7', on_click=lambda: self.add_data('7'))
                ui.button('8', on_click=lambda: self.add_data('8'))
                ui.button('9', on_click=lambda: self.add_data('9'))
                ui.button('\u00F7')
                # ////////////
                ui.button('\u00B1')
                ui.button('4', on_click=lambda: self.add_data('4'))
                ui.button('5', on_click=lambda: self.add_data('5'))
                ui.button('6', on_click=lambda: self.add_data('6'))
                ui.button('X')
                # ////////////
                ui.button('C')
                ui.button('1', on_click=lambda: self.add_data('1'))
                ui.button('2', on_click=lambda: self.add_data('2'))
                ui.button('3', on_click=lambda: self.add_data('3'))
                ui.button('-', on_click=lambda: self.add_data('-'))
                # ////////////
                ui.button('CE')
                ui.button('0')
                ui.button('\u00B7')
                ui.button('=')
                ui.button('+', on_click=lambda: self.add_data('+'))


calculator = Calculator()

ui.run(title='Calculator', dark=True)
