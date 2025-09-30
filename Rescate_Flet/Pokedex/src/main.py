import flet as ft

def main(page: ft.Page):
    page.title = "Pokédex"
    page.padding = 20
    page.scroll = "adaptive"
    
    # Base de datos de Pokémon (lista de diccionarios)
    pokedex = [
        {
            "num": 1,
            "nombre": "Bulbasaur",
            "tipo": "Planta",
            "descripcion": "Un Pokémon que nace con una semilla en el lomo, la cual crece al absorber energía solar.",
            "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png"
        },
        {
            "num": 4,
            "nombre": "Charmander",
            "tipo": "Fuego",
            "descripcion": "Prefiere las cosas calientes. Se dice que cuando llueve, el vapor fluye de la punta de su cola.",
            "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png"
        },
        {
            "num": 7,
            "nombre": "Squirtle",
            "tipo": "Agua",
            "descripcion": "Cuando se retrae en su caparazón, dispara agua a alta presión con una fuerza impresionante.",
            "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png"
        },
        {
            "num": 25,
            "nombre": "Pikachu",
            "tipo": "Eléctrico",
            "descripcion": "Cuando varios de estos Pokémon se juntan, su electricidad puede causar tormentas eléctricas.",
            "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
        },
        {
            "num": 39,
            "nombre": "Jigglypuff",
            "tipo": "Normal",
            "descripcion": "Cuando sus grandes ojos brillan, canta una melodía misteriosa que hace dormir a sus enemigos.",
            "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png"
        },
        {
            "num": 54,
            "nombre": "Psyduck",
            "tipo": "Agua",
            "descripcion": "Usa un misterioso poder. Cuando lo hace, este Pokémon genera ondas cerebrales nunca vistas.",
            "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/54.png"
        },
        {
            "num": 133,
            "nombre": "Eevee",
            "tipo": "Normal",
            "descripcion": "Tiene una composición genética irregular. Puede evolucionar de muchas formas diferentes.",
            "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png"
        },
        {
            "num": 152,
            "nombre": "Chikorita",
            "tipo": "Planta",
            "descripcion": "En combate, agita su hoja para mantener a raya al enemigo. También emite un aroma dulce que calma.",
            "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/152.png"
        },
    ]
    
    # Colores por tipo
    colores_tipo = {
        "Fuego": ft.colors.RED_400,
        "Agua": ft.colors.BLUE_400,
        "Planta": ft.colors.GREEN_400,
        "Eléctrico": ft.colors.YELLOW_700,
        "Normal": ft.colors.GREY_400,
    }
    
    # Variable para almacenar el tipo seleccionado
    tipo_filtro = "Todos"
    
    # Contenedor de la lista de Pokémon
    lista_pokemon = ft.Column(spacing=10, scroll="adaptive")
    
    # Contenedor del detalle
    detalle_container = ft.Column(visible=False, spacing=10)
    
    # Función para mostrar la lista de Pokémon
    def mostrar_lista(tipo="Todos"):
        lista_pokemon.controls.clear()
        
        # Filtrar Pokémon según el tipo
        pokemon_filtrados = pokedex if tipo == "Todos" else [p for p in pokedex if p["tipo"] == tipo]
        
        for pokemon in pokemon_filtrados:
            # Crear tarjeta de Pokémon
            tarjeta = ft.Container(
                content=ft.Row(
                    [
                        ft.Image(src=pokemon["imagen"], width=80, height=80, fit=ft.ImageFit.CONTAIN),
                        ft.Column(
                            [
                                ft.Text(f"#{pokemon['num']:03d}", size=12, color=ft.colors.GREY_600),
                                ft.Text(pokemon["nombre"], size=18, weight=ft.FontWeight.BOLD),
                                ft.Container(
                                    content=ft.Text(pokemon["tipo"], size=12, color=ft.colors.WHITE),
                                    bgcolor=colores_tipo.get(pokemon["tipo"], ft.colors.GREY),
                                    padding=5,
                                    border_radius=5,
                                ),
                            ],
                            spacing=2,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                bgcolor=ft.colors.SURFACE_VARIANT,
                padding=10,
                border_radius=10,
                on_click=lambda e, p=pokemon: mostrar_detalle(p),
                ink=True,
            )
            lista_pokemon.controls.append(tarjeta)
        
        page.update()
    
    # Función para mostrar el detalle de un Pokémon
    def mostrar_detalle(pokemon):
        detalle_container.controls.clear()
        detalle_container.visible = True
        lista_pokemon.visible = False
        filtro_row.visible = False
        
        detalle_container.controls.append(
            ft.Column(
                [
                    # Botón de regresar
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        on_click=lambda e: volver_lista(),
                    ),
                    # Imagen grande
                    ft.Image(src=pokemon["imagen"], width=250, height=250, fit=ft.ImageFit.CONTAIN),
                    # Número
                    ft.Text(f"#{pokemon['num']:03d}", size=20, color=ft.colors.GREY_600),
                    # Nombre
                    ft.Text(pokemon["nombre"], size=32, weight=ft.FontWeight.BOLD),
                    # Tipo
                    ft.Container(
                        content=ft.Text(pokemon["tipo"], size=16, color=ft.colors.WHITE),
                        bgcolor=colores_tipo.get(pokemon["tipo"], ft.colors.GREY),
                        padding=10,
                        border_radius=10,
                    ),
                    # Descripción
                    ft.Text("Descripción:", size=18, weight=ft.FontWeight.BOLD),
                    ft.Text(pokemon["descripcion"], size=14, text_align=ft.TextAlign.JUSTIFY),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )
        )
        
        page.update()
    
    # Función para volver a la lista
    def volver_lista():
        detalle_container.visible = False
        lista_pokemon.visible = True
        filtro_row.visible = True
        page.update()
    
    # Función para cambiar el filtro
    def cambiar_filtro(e):
        nonlocal tipo_filtro
        tipo_filtro = e.control.value
        mostrar_lista(tipo_filtro)
    
    # Dropdown para filtrar por tipo
    filtro_dropdown = ft.Dropdown(
        label="Filtrar por tipo",
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Fuego"),
            ft.dropdown.Option("Agua"),
            ft.dropdown.Option("Planta"),
            ft.dropdown.Option("Eléctrico"),
            ft.dropdown.Option("Normal"),
        ],
        value="Todos",
        on_change=cambiar_filtro,
        width=200,
    )
    
    # Row del filtro
    filtro_row = ft.Row([filtro_dropdown], alignment=ft.MainAxisAlignment.CENTER)
    
    # Agregar elementos a la página
    page.add(
        ft.Text("🔴 Pokédex", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
        filtro_row,
        lista_pokemon,
        detalle_container,
    )
    
    # Mostrar la lista inicial
    mostrar_lista()

# Ejecutar la app
ft.app(target=main)