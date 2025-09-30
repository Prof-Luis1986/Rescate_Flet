import flet as ft

FRUTAS = [
    {"nombre": "Manzana", "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/320px-Red_Apple.jpg"},
    {"nombre": "Banana", "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Banana-Single.jpg/320px-Banana-Single.jpg"},
    {"nombre": "Fresa", "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/PerfectStrawberry.jpg/320px-PerfectStrawberry.jpg"},
    {"nombre": "Naranja", "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Orange-Fruit-Pieces.jpg/320px-Orange-Fruit-Pieces.jpg"},
    {"nombre": "Uvas", "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Table_grapes_on_white.jpg/320px-Table_grapes_on_white.jpg"}
]

def card_fruit(f):
    return ft.Container(
        content=ft.Column([
            ft.Image(src=f["imagen"], width=180, height=140, fit=ft.ImageFit.CONTAIN),
            ft.Text(f["nombre"], size=16, weight=ft.FontWeight.BOLD)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=10,
        border_radius=8,
        border=ft.border.all(1, ft.colors.GREY_300)
    )

def main(page: ft.Page):
    page.title = "Galería de Frutas"
    page.window_width = 900
    page.window_height = 600

    grid = ft.GridView(expand=True, max_extent=220, child_aspect_ratio=1)
    for f in FRUTAS:
        grid.controls.append(card_fruit(f))

    page.add(ft.Column([
        ft.Text("Galería de Frutas Favoritas", size=24, weight=ft.FontWeight.BOLD),
        grid
    ], expand=True))

if __name__ == "__main__":
    ft.app(target=main)
