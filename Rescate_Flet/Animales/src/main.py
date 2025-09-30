import flet as ft

ANIMALES = {
    "Perro": {
        "descripcion": "Animal doméstico, leal y juguetón.",
        "imagen": "https://cdn2.thedogapi.com/images/-HgpNnGXl.jpg"
    },
    "Gato": {
        "descripcion": "Curioso, independiente y dormilón.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/320px-Cat03.jpg"
    },
    "Elefante": {
        "descripcion": "Mamífero grande con trompa, muy inteligente.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/African_Bush_Elephant.jpg/320px-African_Bush_Elephant.jpg"
    }
}

def main(page: ft.Page):
    page.title = "Diccionario de Animales"
    page.window_width = 850
    page.window_height = 550

    dd = ft.Dropdown(label="Selecciona animal",
                     options=[ft.dropdown.Option(k) for k in ANIMALES.keys()])
    desc = ft.Text("")
    img = ft.Image(width=320, height=240, fit=ft.ImageFit.CONTAIN)

    def actualizar(_):
        nombre = dd.value
        if not nombre: return
        data = ANIMALES.get(nombre, {})
        desc.value = data.get("descripcion", "")
        img.src = data.get("imagen", None)
        page.update()

    dd.on_change = actualizar
    first = next(iter(ANIMALES.keys()))
    dd.value = first
    actualizar(None)

    page.add(ft.Column([
        ft.Text("Diccionario de Animales", size=24, weight=ft.FontWeight.BOLD),
        dd,
        img,
        ft.Text("Descripción", size=18, weight=ft.FontWeight.BOLD),
        desc
    ], expand=True, scroll=ft.ScrollMode.AUTO))

if __name__ == "__main__":
    ft.app(target=main)
