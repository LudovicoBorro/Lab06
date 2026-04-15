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
        self.ddAnno = None
        self.ddBrand = None
        self.ddRetailer = None
        self.btnTopVendite = None
        self.btnAnalizzaVendite = None
        self.list_view = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.add(self._title)

        #ROW with some controls
        self.ddAnno = ft.Dropdown(label="anno", width=250, options=[ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro")])
        self._controller.fill_ddAnni()
        self.ddBrand = ft.Dropdown(label="brand", width=250, options=[ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro")])
        self._controller.fill_ddBrand()
        self.ddRetailer = ft.Dropdown(label="retailer", width=650, options=[ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro")])
        self._controller.fill_ddRetailer()

        row1 = ft.Row(controls=[self.ddAnno, self.ddBrand, self.ddRetailer], alignment=ft.MainAxisAlignment.CENTER)

        # buttons

        self.btnTopVendite = ft.ElevatedButton(text="Top vendite", on_click=self._controller.handleTopVendite, width=200)
        self.btnAnalizzaVendite = ft.ElevatedButton(text="Analizza vendite", on_click=self._controller.handleAnalizzaVendite, width=200)

        row2 = ft.Row(controls=[self.btnTopVendite, self.btnAnalizzaVendite], alignment=ft.MainAxisAlignment.CENTER)

        # List View where the reply is printed
        self.list_view = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.add(row1, row2, self.list_view)
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
