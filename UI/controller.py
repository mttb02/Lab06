import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self.anno = None
        self.brand = None
        self.retailer = None

    def handle_top_vendite(self, e):
        self._view.lw_output.controls.clear()
        if self.retailer is not None:
            vendite = self._model.top_vendite(self.anno, self.brand, self.retailer.retailer_code)
        else:
            vendite = self._model.top_vendite(self.anno, self.brand, self.retailer)
        for i in range(1, min(5, len(vendite)-1)):
            self._view.lw_output.controls.append(ft.Text(vendite[i]))
        if len(vendite) == 0:
            self._view.lw_output.controls.append(ft.Text("Nessuna vendita con i parametri selezionati"))
        self._view.update_page()

    #ATTENZIONE: ANDAVA MESSO NEL MODEL
    def handle_analizza_vendite(self, e):
        self._view.lw_output.controls.clear()
        if self.retailer is not None:
            vendite = self._model.top_vendite(self.anno, self.brand, self.retailer.retailer_code)
        else:
            vendite = self._model.top_vendite(self.anno, self.brand, self.retailer)
        giro_di_afari = 0
        numero_vendite = len(vendite)
        retailers = dict()
        prodotti = dict()
        for i in range(0, len(vendite)-1):
            giro_di_afari += (vendite[i].unit_sale_price * vendite[i].quantity)
            retailers[vendite[i].retailer_code] = 0
            prodotti[vendite[i].product_number] = 0
        self._view.lw_output.controls.append(ft.Text(f"Statistiche vendite:"))
        self._view.lw_output.controls.append(ft.Text(f"Giro di affari: {giro_di_afari}"))
        self._view.lw_output.controls.append(ft.Text(f"Numero vendite: {numero_vendite}"))
        self._view.lw_output.controls.append(ft.Text(f"Numero retailers coinvolti: {len(retailers)}"))
        self._view.lw_output.controls.append(ft.Text(f"Numero prodotti coinvolti: {len(prodotti)}"))
        self._view.update_page()

    def populate_dd(self):
        #popola anni
        for a in self._model.get_anni():
            self._view.dd_anno.options.append(ft.dropdown.Option(key=a, text=a, on_click=self.read_anno))
        # popola brand
        for b in self._model.get_brands():
            self._view.dd_brand.options.append(ft.dropdown.Option(key=b, text=b, on_click=self.read_brand))
        # popola retailer
        for r in self._model.get_retailers():
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=r.retailer_code, text=r.retailer_name, data=r, on_click=self.read_retailer))

    def read_anno(self, e):
        self.anno = e.control.key

    def read_brand(self, e):
        self.brand = e.control.key

    def read_retailer(self, e):
        self.retailer = e.control.data
        print(self.retailer.retailer_code)
