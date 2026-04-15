import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._retailer = None

    def handleTopVendite(self, e):
        pass

    def handleAnalizzaVendite(self, e):
        pass

    def fill_ddAnni(self):

        anni = self._model.getAnni()

        for anno in anni:
            self._view.ddAnno.options.append(
                ft.dropdown.Option(key=anno, text=anno)
            )
        self._view.update_page()

    def fill_ddBrand(self):

        brands = self._model.getBrands()

        for brand in brands:
            self._view.ddBrand.options.append(
                ft.dropdown.Option(key=brand, text=brand)
            )
        self._view.update_page()

    def fill_ddRetailer(self):

        retailers = self._model.getRetailers()

        for retailer in retailers:
            self._view.ddRetailer.options.append(
                ft.dropdown.Option(key=retailer.Retailer_code, text=retailer.Retailer_name,
                                   data=retailer, on_click=self.read_retailer)
            )
        self._view.update_page()

    def read_retailer(self, e):
        self._retailer = e.control.data