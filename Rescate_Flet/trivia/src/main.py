import flet as ft

def main(page: ft.Page):
    page.title = "Trivia: Historia de la Informática"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = "adaptive"
    
    # Preguntas y respuestas
    preguntas = [
        {
            "pregunta": "¿Quién es considerado el 'padre de la computación'?",
            "opciones": ["Bill Gates", "Alan Turing", "Steve Jobs", "Charles Babbage"],
            "correcta": 1
        },
        {
            "pregunta": "¿Qué máquina diseñó Charles Babbage en el siglo XIX?",
            "opciones": ["Enigma", "Máquina Analítica", "Colossus", "UNIVAC"],
            "correcta": 1
        },
        {
            "pregunta": "¿Qué lenguaje de programación fue creado en los años 50 y es usado en ciencia e ingeniería?",
            "opciones": ["Python", "COBOL", "Fortran", "Java"],
            "correcta": 2
        },
        {
            "pregunta": "La máquina Enigma fue usada durante:",
            "opciones": ["La Primera Guerra Mundial", "La Guerra Fría", "La Segunda Guerra Mundial", "La Revolución Industrial"],
            "correcta": 2
        },
        {
            "pregunta": "¿Cuál fue la primera computadora electrónica de propósito general?",
            "opciones": ["Mark I", "ENIAC", "Z3", "Colossus"],
            "correcta": 1
        },
        {
            "pregunta": "¿Qué mujer fue pionera en la programación y colaboró en el desarrollo de COBOL?",
            "opciones": ["Ada Lovelace", "Grace Hopper", "Margaret Hamilton", "Katherine Johnson"],
            "correcta": 1
        },
        {
            "pregunta": "¿Qué científico propuso la 'máquina universal' como concepto teórico?",
            "opciones": ["John von Neumann", "Alan Turing", "Claude Shannon", "Nikola Tesla"],
            "correcta": 1
        },
        {
            "pregunta": "La arquitectura de Von Neumann introdujo la idea de:",
            "opciones": ["Computadoras analógicas", "Programas almacenados en memoria", "Multi-core processors", "Sistemas binarios"],
            "correcta": 1
        },
        {
            "pregunta": "¿Cuál fue la primera computadora personal de IBM lanzada en 1981?",
            "opciones": ["IBM 5100", "IBM PC", "IBM 360", "IBM XT"],
            "correcta": 1
        },
        {
            "pregunta": "¿Quién desarrolló el lenguaje de programación C?",
            "opciones": ["John Backus", "Ken Thompson", "Dennis Ritchie", "James Gosling"],
            "correcta": 2
        }
    ]
    
    pregunta_actual = 0
    puntaje = 0
    respuesta_seleccionada = None
    
    # Componentes UI
    titulo = ft.Text("🖥️ Trivia: Historia de la Informática", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_700)
    progreso = ft.Text(f"Pregunta 1 de {len(preguntas)}", size=16, color=ft.colors.GREY_700)
    texto_pregunta = ft.Text("", size=20, weight=ft.FontWeight.W_500)
    
    opciones_container = ft.Column(spacing=10)
    boton_siguiente = ft.ElevatedButton("Siguiente", visible=False, on_click=lambda e: siguiente_pregunta())
    resultado_texto = ft.Text("", size=18, weight=ft.FontWeight.BOLD)
    
    def cargar_pregunta():
        nonlocal respuesta_seleccionada
        respuesta_seleccionada = None
        
        if pregunta_actual < len(preguntas):
            p = preguntas[pregunta_actual]
            texto_pregunta.value = p["pregunta"]
            progreso.value = f"Pregunta {pregunta_actual + 1} de {len(preguntas)}"
            
            opciones_container.controls.clear()
            for i, opcion in enumerate(p["opciones"]):
                btn = ft.Container(
                    content=ft.Text(opcion, size=16),
                    padding=15,
                    border=ft.border.all(2, ft.colors.BLUE_300),
                    border_radius=10,
                    bgcolor=ft.colors.BLUE_50,
                    on_click=lambda e, idx=i: seleccionar_opcion(idx),
                    data=i
                )
                opciones_container.controls.append(btn)
            
            boton_siguiente.visible = False
            resultado_texto.value = ""
        else:
            mostrar_resultado_final()
        
        page.update()
    
    def seleccionar_opcion(idx):
        nonlocal respuesta_seleccionada, puntaje
        
        if respuesta_seleccionada is not None:
            return
        
        respuesta_seleccionada = idx
        correcta = preguntas[pregunta_actual]["correcta"]
        
        for i, control in enumerate(opciones_container.controls):
            if i == correcta:
                control.bgcolor = ft.colors.GREEN_200
                control.border = ft.border.all(2, ft.colors.GREEN_700)
            elif i == idx and idx != correcta:
                control.bgcolor = ft.colors.RED_200
                control.border = ft.border.all(2, ft.colors.RED_700)
            else:
                control.bgcolor = ft.colors.GREY_200
        
        if idx == correcta:
            puntaje += 1
            resultado_texto.value = "✅ ¡Correcto!"
            resultado_texto.color = ft.colors.GREEN_700
        else:
            resultado_texto.value = "❌ Incorrecto"
            resultado_texto.color = ft.colors.RED_700
        
        boton_siguiente.visible = True
        page.update()
    
    def siguiente_pregunta():
        nonlocal pregunta_actual
        pregunta_actual += 1
        cargar_pregunta()
    
    def mostrar_resultado_final():
        page.clean()
        
        porcentaje = (puntaje / len(preguntas)) * 100
        
        if porcentaje >= 80:
            emoji = "🏆"
            mensaje = "¡Excelente!"
        elif porcentaje >= 60:
            emoji = "👍"
            mensaje = "¡Bien hecho!"
        else:
            emoji = "📚"
            mensaje = "Sigue aprendiendo"
        
        page.add(
            ft.Column([
                ft.Text("🎉 Trivia Completada", size=32, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_700),
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                ft.Text(f"{emoji} {mensaje}", size=24),
                ft.Text(f"Puntaje: {puntaje} de {len(preguntas)}", size=28, weight=ft.FontWeight.BOLD),
                ft.Text(f"Porcentaje: {porcentaje:.0f}%", size=20, color=ft.colors.GREY_700),
                ft.Divider(height=30, color=ft.colors.TRANSPARENT),
                ft.ElevatedButton("Reiniciar Trivia", on_click=lambda e: reiniciar(), bgcolor=ft.colors.BLUE_700, color=ft.colors.WHITE)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
        )
    
    def reiniciar():
        nonlocal pregunta_actual, puntaje
        pregunta_actual = 0
        puntaje = 0
        page.clean()
        iniciar_app()
    
    def iniciar_app():
        page.add(
            ft.Column([
                titulo,
                ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                progreso,
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                texto_pregunta,
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                opciones_container,
                ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                resultado_texto,
                boton_siguiente
            ], spacing=5)
        )
        cargar_pregunta()
    
    iniciar_app()

ft.app(target=main)