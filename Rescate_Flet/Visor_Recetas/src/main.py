import flet as ft

RECETAS = [
    {
        "nombre": "Sándwich clásico",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Sandwich.png/320px-Sandwich.png",
        "ingredientes": ["Pan", "Jamón", "Queso", "Lechuga", "Tomate"],
        "pasos": ["Tostar pan", "Colocar ingredientes", "Servir"]
    },
    {
        "nombre": "Ensalada mixta",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Greek_Salad_Choriatiki.jpg/320px-Greek_Salad_Choriatiki.jpg",
        "ingredientes": ["Lechuga", "Tomate", "Pepino", "Aceitunas", "Queso feta"],
        "pasos": ["Lavar vegetales", "Cortar", "Mezclar y aderezar"]
    },
    {
        "nombre": "Pasta al tomate",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Pasta_Pomodoro.jpg/320px-Pasta_Pomodoro.jpg",
        "ingredientes": ["Pasta", "Tomate", "Ajo", "Aceite de oliva", "Sal"],
        "pasos": ["Hervir pasta", "Salsa de tomate", "Mezclar"]
    }
]

def main(page: ft.Page):
    page.title = "Visor de Recetas"
    page.window_width = 900
    page.window_height = 600

    dd = ft.Dropdown(label="Selecciona receta",
                     options=[ft.dropdown.Option(r["nombre"]) for r in RECETAS])
    img = ft.Image(width=320, height=240, fit=ft.ImageFit.CONTAIN)
    lista_ingredientes = ft.Column()
    lista_pasos = ft.Column()

    def mostrar_receta(nombre: str):
        r = next((x for x in RECETAS if x["nombre"] == nombre), None)
        if not r: return
        img.src = r["imagen"]
        lista_ingredientes.controls = [ft.Text(f"• {i}") for i in r["ingredientes"]]
        lista_pasos.controls = [ft.Text(f"{idx+1}. {p}") for idx, p in enumerate(r["pasos"])]
        page.update()

    def on_change(e):
        mostrar_receta(dd.value)

    dd.on_change = on_change
    if RECETAS:
        dd.value = RECETAS[0]["nombre"]
        mostrar_receta(dd.value)

    page.add(
        ft.Column([
            ft.Text("Visor de Recetas", size=24, weight=ft.FontWeight.BOLD),
            dd,
            ft.Row([img, ft.Column([ft.Text("Ingredientes", size=18, weight=ft.FontWeight.BOLD), lista_ingredientes])]),
            ft.Text("Pasos", size=18, weight=ft.FontWeight.BOLD),
            lista_pasos
        ], expand=True, scroll=ft.ScrollMode.AUTO)
    )

if __name__ == "__main__":
    ft.app(target=main)
