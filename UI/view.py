import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab06"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_anno = None
        self.dd_brand = None
        self.dd_retailer = None
        self.btn_top_vendite = None
        self.btn_analizza_vendite = None
        self.lw_output = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #Row1
        self.dd_anno = ft.Dropdown(
            label="anno",
            width=200,
            options=[ft.dropdown.Option(key=None, text="Nessun filtro", on_click=self._controller.read_anno)]
        )
        self.dd_brand = ft.Dropdown(
            label="brand",
            width=200,
            options=[ft.dropdown.Option(key=None, text="Nessun filtro", on_click=self._controller.read_brand)]
        )
        self.dd_retailer = ft.Dropdown(
            label="retailer",
            expand=True,
            options=[ft.dropdown.Option(key=None, text="Nessun filtro", data=None, on_click=self._controller.read_retailer)]
        )

        row1 = ft.Row([self.dd_anno, self.dd_brand, self.dd_retailer])
        self._controller.populate_dd()

        #Row2
        self.btn_top_vendite = ft.ElevatedButton(
            text="Top vendite",
            on_click=self._controller.handle_top_vendite
        )
        self.btn_analizza_vendite = ft.ElevatedButton(
            text="Analizza vendite",
            on_click=self._controller.handle_analizza_vendite
        )
        row2 = ft.Row([self.btn_top_vendite, self.btn_analizza_vendite], alignment=ft.MainAxisAlignment.CENTER)

        #Output
        self.lw_output = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._page.controls.append(self.lw_output)

        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
