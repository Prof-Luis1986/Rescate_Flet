import flet as ft
import random

PALABRAS = [
    {
        "es": "perro", 
        "en": "dog", 
        "imagen": "https://raw.githubusercontent.com/Prof-Luis1986/recursos-cetis50/refs/heads/main/Perro.jpg"
    },
    {
        "es": "gato", 
        "en": "cat", 
        "imagen": "https://cdn.pixabay.com/photo/2015/11/16/22/14/cat-1045782_640.jpg"
    },
    {
        "es": "casa", 
        "en": "house", 
        "imagen": "https://raw.githubusercontent.com/Prof-Luis1986/recursos-cetis50/refs/heads/main/casa.jpeg"
    },
    {
        "es": "manzana", 
        "en": "apple", 
        "imagen": "https://raw.githubusercontent.com/Prof-Luis1986/recursos-cetis50/refs/heads/main/manzana.jpg"
    }
]

def main(page: ft.Page):
    page.title = "Diccionario Visual Bilingüe"
    page.window_width = 800
    page.window_height = 560

    idioma = "es"
    idx = 0

    palabra_txt = ft.Text("", size=24, weight=ft.FontWeight.BOLD)
    img = ft.Image(width=320, height=240, fit=ft.ImageFit.CONTAIN)
    search = ft.TextField(label="Buscar (es/en)", width=260)

    def mostrar():
        p = PALABRAS[idx]
        palabra_txt.value = p[idioma]
        img.src = p["imagen"]
        page.update()

    def azar(_):
        nonlocal idx
        idx = random.randrange(len(PALABRAS))
        mostrar()

    def alternar(_):
        nonlocal idioma
        idioma = "en" if idioma == "es" else "es"
        mostrar()

    def buscar(_):
        nonlocal idx
        q = (search.value or "").strip().lower()
        for i, p in enumerate(PALABRAS):
            if p["es"] == q or p["en"] == q:
                idx = i
                mostrar()
                return
        page.snack_bar = ft.SnackBar(ft.Text("No encontrado"), open=True)
        page.update()

    mostrar()

    page.add(ft.Column([
        ft.Text("Diccionario Visual Bilingüe", size=24, weight=ft.FontWeight.BOLD),
        palabra_txt,
        img,
        ft.Row([
            ft.ElevatedButton("Azar", on_click=azar),
            ft.OutlinedButton("Alternar es/en", on_click=alternar),
            search,
            ft.ElevatedButton("Buscar", on_click=buscar)
        ]),
    ], expand=True, alignment=ft.MainAxisAlignment.START))

if __name__ == "__main__":
    ft.app(target=main)