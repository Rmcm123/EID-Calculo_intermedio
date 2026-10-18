from manim import *

class Presentacion(Scene):
    def construct(self):
        self.portada()
        self.presentar_pregunta()
        self.explicar_tasa()
        self.integral_y_acumulacion()
        self.acumulado_vs_final()
        self.calculo_ejercicio()
        self.cierre()
        self.creditos()

    def portada(self):
        titulo = self.texto("Cambio acumulado \nversus cantidad final", tamano=48)
        titulo.to_edge(UP, buff=2)
        grupo = self.texto("Grupo 7", tamano=36)
        integrantes = self.texto("Renato Cáceres · Lucas Núñez · Victor Hidalgo")
        integrantes.next_to(grupo, DOWN, buff=0.4)

        self.mostrar(titulo, grupo, integrantes, tiempo=7)
        self.desaparecer(titulo, grupo, integrantes)

    def presentar_pregunta(self):
        pregunta = self.texto("¿Por qué integrar una tasa de cambio \nno entrega necesariamente la cantidad final?", tamano=36)
        pregunta.to_edge(UP, buff=1.2)

        self.escribir(pregunta, tiempo=8)

        ej_texto = self.texto("Nuestro ejemplo", tamano=24)
        ej_texto.next_to(pregunta, DOWN, buff=0.5)

        estanque = self.crear_estanque(litros=100)
        estanque.next_to(ej_texto, DOWN, buff=0.5)

        self.mostrar(ej_texto, estanque, tiempo=4)
        self.desaparecer(pregunta, ej_texto, estanque)

    def explicar_tasa(self):
        tasa = self.encabezado("La tasa de cambio describe qué tan rápido cambia")
        self.escribir(tasa, tiempo=6)

        rt = self.texto("r(t) = Q'(t)", tamano=36, color=BLUE)
        rt.next_to(tasa, DOWN, buff=0.5)
        self.escribir(rt, tiempo=6)

        medida_cantidad = self.texto("Q(t) = Cantidad de agua, en litros", tamano=24)
        medida_cantidad.next_to(rt, DOWN, buff=0.5)
        medida_tasa = self.texto("r(t) = Tasa de cambio de la cantidad de agua, en litros por minuto", tamano=24)
        medida_tasa.next_to(medida_cantidad, DOWN, buff=0.5)
        self.mostrar(medida_cantidad, medida_tasa, tiempo=9)

        positiva = self.tarjeta("Tasa positiva","+5 L/min","Aumenta",borde=GREEN,color_valor=GREEN,color_debajo=GREEN)
        negativa = self.tarjeta("Tasa negativa","−5 L/min","Disminuye",borde=RED,color_valor=RED,color_debajo=RED)
        cero = self.tarjeta("Tasa cero","0 L/min","No cambia en ese instante",borde=GRAY,color_valor=WHITE)
        tarjetas = VGroup(positiva, negativa, cero)
        tarjetas.arrange(RIGHT, buff=0.4, aligned_edge=UP)

        tarjetas.next_to(medida_tasa, DOWN, buff=1)

        self.mostrar(tarjetas, tiempo=17)
        self.desaparecer(tasa, rt, medida_cantidad, medida_tasa, tarjetas)

    def texto(self, texto, tamano=24, color=WHITE):
        return Text(texto, font_size=tamano, fill_color=color)

    def rectangulo(self, ancho, alto, color=WHITE, relleno=0):
        return Rectangle(
            width=ancho,
            height=alto,
            stroke_color=color,
            fill_color=color,
            fill_opacity=relleno
        )

    def mostrar(self, *objetos, tiempo=2):
        self.add(*objetos)
        self.wait(tiempo)

    def escribir(self, *objetos, tiempo=2):
        self.play(*[Write(objeto) for objeto in objetos])
        self.wait(tiempo)

    def desaparecer(self, *objetos):
        self.play(*[FadeOut(objeto) for objeto in objetos])

    def crear_estanque(self, litros=100, capacidad=150, ancho=3, alto=4):
        contorno = self.rectangulo(ancho, alto)

        altura_agua = (alto - 0.1) * (litros / capacidad)

        agua = self.rectangulo(
            ancho - 0.1,
            altura_agua,
            BLUE,
            0.7
        )

        agua.set_stroke(width=0)
        agua.align_to(contorno, DOWN)
        agua.shift(UP * 0.05)

        return VGroup(agua, contorno)

    def crear_estanque_etiquetado(self, litros):
        """Devuelve el estanque, su etiqueta y el número que se puede animar."""
        estanque = self.crear_estanque(litros=litros)
        numero = DecimalNumber(
            litros, num_decimal_places=0, mob_class=Text,
            font_size=24, color=BLUE
        )
        unidad = self.texto("L", tamano=24, color=BLUE)
        etiqueta = VGroup(numero, unidad).arrange(RIGHT, buff=0.1)

        return estanque, etiqueta, numero

    def encabezado(self, contenido):
        titulo = self.texto(contenido, tamano=36)
        titulo.to_edge(UP, buff=0.4)

        linea = Line(
            LEFT * 6,
            RIGHT * 6,
            color=GRAY,
            stroke_width=1
        )
        linea.next_to(titulo, DOWN, buff=0.25)

        return VGroup(titulo, linea)

    def iniciar_seccion(self, contenido):
        if self.mobjects:
            self.desaparecer(*list(self.mobjects))

        titulo = self.encabezado(contenido)
        self.add(titulo)
        return titulo

    def tarjeta(self, titulo,valor,texto_debajo="",ancho=3.6,alto=1.5,fondo="#020202",borde=WHITE,color_titulo=WHITE,color_valor=BLUE,color_debajo=WHITE):
        caja = Rectangle(
            width=ancho,
            height=alto,
            stroke_color=borde,
            stroke_width=2,
            fill_color=fondo,
            fill_opacity=1
        )

        titulo_obj = self.texto(titulo, tamano=22)
        titulo_obj.set_color(color_titulo)

        valor_obj = self.texto(valor, tamano=36)
        valor_obj.set_color(color_valor)

        textos = VGroup(titulo_obj, valor_obj)
        textos.arrange(DOWN, buff=0.15)

        if textos.width > ancho - 0.4:
            textos.scale_to_fit_width(ancho - 0.4)

        if textos.height > alto - 0.4:
            textos.scale_to_fit_height(alto - 0.4)

        textos.move_to(caja.get_center())

        tarjeta = VGroup(caja, textos)

        if texto_debajo:
            pie = self.texto(texto_debajo, tamano=22)
            pie.set_color(color_debajo)

            if pie.width > ancho:
                pie.scale_to_fit_width(ancho)

            pie.next_to(caja, DOWN, buff=0.2)
            tarjeta.add(pie)

        return tarjeta

    def integral(self, inferior, superior, cuerpo, prefijo="", sufijo="", tamano=36):
        signo = self.texto("∫", tamano * 1.7)
        arriba = self.texto(str(superior), tamano * 0.55)
        abajo = self.texto(str(inferior), tamano * 0.55)
        arriba.move_to(signo.get_top() + RIGHT * 0.25 + UP * 0.16)
        abajo.move_to(signo.get_bottom() + RIGHT * 0.08 + DOWN * 0.16)
        simbolo = VGroup(signo, arriba, abajo)
        partes = []
        if prefijo:
            partes.append(self.texto(prefijo, tamano))
        partes += [simbolo, self.texto(cuerpo, tamano)]
        if sufijo:
            partes.append(self.texto(sufijo, tamano))
        return VGroup(*partes).arrange(RIGHT, buff=0.18)

    def llenar_estanque(self, estanque, inicial, final):
        agua = estanque[0]
        altura_final = agua.height * (final / inicial)

        return agua.animate.stretch_to_fit_height(
            altura_final,
            about_edge=DOWN
        )

    def integral_y_acumulacion(self):
        self.iniciar_seccion("Integral y acumulación")

        ejemplo = self.texto(
            "Tasa constante durante un minuto:\n\n"
            "5 L/min × 1 min = 5 L",
            tamano=32
        )
        self.mostrar(ejemplo, tiempo=21)
        self.desaparecer(ejemplo)

        ejes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 10, 2],
            x_length=5.5,
            y_length=3.2,
            tips=False
        ).move_to(LEFT * 2.7 + DOWN * 0.3)

        ejes.set_z_index(2)

        nombre_tiempo = self.texto("t (min)", tamano=20)
        nombre_tiempo.next_to(ejes.x_axis, DOWN, buff=0.45)

        nombre_tasa = self.texto("r(t) (L/min)", tamano=20)
        nombre_tasa.next_to(ejes, UP, buff=0.2)

        etiquetas = VGroup(nombre_tiempo, nombre_tasa)

        for t in [0, 5]:
            marca = self.texto(str(t), tamano=18)
            marca.next_to(ejes.c2p(t, 0), DOWN, buff=0.1)
            etiquetas.add(marca)

        marca_diez = self.texto("10", tamano=18)
        marca_diez.next_to(ejes.c2p(0, 10), LEFT, buff=0.1)
        etiquetas.add(marca_diez)
        etiquetas.set_z_index(3)

        curva = ejes.plot(lambda t: 2 * t, color=BLUE)
        curva.set_z_index(3)

        modelo = self.texto("r(t) = 2t", tamano=32)
        modelo.move_to(RIGHT * 3.3 + UP * 1.8)

        definiciones = self.texto("n: número de intervalos\nt*: extremo derecho", tamano=21)
        definiciones.move_to(RIGHT * 3.3 + DOWN * 0.3)

        aporte = VGroup(
            self.texto("Cada aporte aproxima", tamano=24),
            self.texto("un cambio:", tamano=24),
            self.texto("r(t*) × Δt", tamano=28)
        )
        aporte.arrange(DOWN, buff=0.15)
        aporte.move_to(RIGHT * 3.3 + DOWN * 2)

        self.add(ejes, etiquetas, curva, modelo, definiciones, aporte)

        def rectangulos(n):
            return ejes.get_riemann_rectangles(
                curva,
                x_range=[0, 5],
                dx=5 / n,
                input_sample_type="right",
                color=YELLOW,
                fill_opacity=0.4,
                stroke_width=1,
                width_scale_factor=1
            ).set_z_index(1)

        bloques = rectangulos(4)

        contador = self.texto("n = 4\nΔt = 1.25 min", tamano=24)
        contador.move_to(RIGHT * 3.3 + UP * 0.7)

        self.play(FadeIn(bloques), FadeIn(contador))
        self.wait(20)

        for n in [8, 16, 32]:
            nuevo_texto = self.texto(f"n = {n}\nΔt = {5 / n:g} min", tamano=24)
            nuevo_texto.move_to(contador)

            self.play(
                Transform(bloques, rectangulos(n)),
                Transform(contador, nuevo_texto)
            )
            self.wait(3)

        region = ejes.get_area(
            curva,
            x_range=[0, 5],
            color=YELLOW,
            opacity=0.4
        )
        region.set_z_index(1)

        self.add(region)
        self.desaparecer(bloques, contador, definiciones, aporte)
        cambio = self.texto("Cambio acumulado\n25 L", tamano=30, color=YELLOW)
        cambio.move_to(RIGHT * 3.3 + DOWN * 0.3)
        self.escribir(cambio, tiempo=5)

        grafico = VGroup(ejes, etiquetas, curva, region)
        self.desaparecer(modelo, cambio, grafico)

        conclusion = VGroup(
            self.integral(0, 5, "r(t) dt", tamano=36),
            self.texto("Cambio acumulado", tamano=32)
        )
        conclusion.arrange(DOWN, buff=0.4)

        self.escribir(conclusion, tiempo=5)

        aviso = self.texto(
            "Para conocer la cantidad final, falta la cantidad inicial.",
            tamano=25
        )
        aviso.to_edge(DOWN, buff=0.4)

        self.mostrar(aviso, tiempo=4)

    def acumulado_vs_final(self):
        titulo = self.iniciar_seccion("Cambio acumulado versus cantidad final")

        ejemplo = self.texto(
            "Cantidad Final = Cantidad Inicial + Cambio Acumulado",
            tamano=28
        )
        ejemplo.next_to(titulo, DOWN, buff=0.5)

        self.escribir(ejemplo, tiempo=12)

        formula = self.integral("a", "b", "r(t) dt", prefijo="Q(b) = Q(a) +", tamano=33)
        formula.next_to(ejemplo, DOWN, buff=1)
        self.escribir(formula, tiempo=14)
        self.desaparecer(formula)

        estanque_a, etiqueta_a, texto_a = self.crear_estanque_etiquetado(100)
        estanque_b, etiqueta_b, texto_b = self.crear_estanque_etiquetado(40)
        tasa = self.texto("Misma tasa r(t)\nMismo intervalo\n+25L en ambos", tamano=28, color=BLUE)

        estanques = VGroup(estanque_a, tasa, estanque_b)
        estanques.arrange(RIGHT, buff=1)
        estanques.next_to(ejemplo, DOWN, buff=1)

        etiqueta_a.next_to(estanque_a, DOWN, buff=0.2)
        etiqueta_b.next_to(estanque_b, DOWN, buff=0.2)

        self.add(estanques, etiqueta_a, etiqueta_b)
        self.wait(6)

        self.play(
            self.llenar_estanque(estanque_a, inicial=100, final=125),
            self.llenar_estanque(estanque_b, inicial=40, final=65),
            ChangeDecimalToValue(texto_a, 125),
            ChangeDecimalToValue(texto_b, 65),
            run_time=8,
            rate_func=lambda progreso: progreso**2
        )

        self.wait(9)

    def calculo_ejercicio(self):
        titulo = self.iniciar_seccion("Cálculo del cambio acumulado")
        datos = self.texto("Q(0) = 100 L   ·   r(t) = 2t L/min   ·   De 0 a 5 min", tamano=26)
        datos.next_to(titulo, DOWN, buff=0.5)
        self.escribir(datos, tiempo=7)

        tasas = VGroup(
            self.texto("La tasa crece con el tiempo", tamano=28),
            self.texto("r(0) = 0   ·   r(1) = 2   ·   r(2) = 4   ·   r(5) = 10 L/min", color=BLUE)
        ).arrange(DOWN, buff=0.4)
        self.escribir(tasas, tiempo=11)
        self.desaparecer(tasas)

        fundamento = self.texto(
            "r(t) es continua en [0, 5].\nAplicamos el teorema fundamental del cálculo.", tamano=26
        )
        self.escribir(fundamento, tiempo=8)
        self.desaparecer(fundamento)

        calculo = self.integral(0, 5, "2t dt", prefijo="ΔQ =", tamano=36)
        calculo.move_to(UP * 0.3)
        self.escribir(calculo, tiempo=4)
        explicacion = self.texto("ΔQ representa el cambio acumulado.", tamano=24)
        explicacion.next_to(calculo, DOWN, buff=0.6)
        self.mostrar(explicacion, tiempo=1)
        pasos = [
            (self.integral(0, 5, "t dt", prefijo="ΔQ = 2", tamano=36),
             "El factor constante 2 sale de la integral.", 4),
            (self.texto("ΔQ = 2 [t² / 2]₀⁵", tamano=36),
             "Una antiderivada de t es t² / 2.", 4),
            (self.texto("ΔQ = [t²]₀⁵", tamano=36),
             "F(t) = t² es una antiderivada, porque F'(t) = 2t.", 6),
            (self.texto("ΔQ = F(5) − F(0)", tamano=36),
             "Evaluamos en el límite superior (5)\ny restamos el valor en el límite inferior (0).", 8),
            (self.texto("ΔQ = 5² − 0²", tamano=36),
             "Sustituimos t por 5 y por 0 en F(t) = t².", 4),
            (self.texto("ΔQ = 25 − 0 = 25", tamano=36),
             "El cambio acumulado en esos cinco minutos es de 25 litros.", 3)
        ]
        for expresion, mensaje, tiempo in pasos:
            expresion.move_to(calculo)
            nuevo_texto = self.texto(mensaje, tamano=24).move_to(explicacion)
            self.play(Transform(calculo, expresion), Transform(explicacion, nuevo_texto))
            self.wait(tiempo)
        self.desaparecer(explicacion)

        unidades = VGroup(
            self.texto("r(t): L/min   ·   dt: min", tamano=24),
            self.texto("(L/min) × min = L", tamano=28, color=BLUE)
        ).arrange(DOWN, buff=0.2)
        unidades.next_to(calculo, DOWN, buff=0.5)
        self.escribir(unidades, tiempo=5)

        resultado = VGroup(
            self.texto("Cambio acumulado: +25 L en cinco minutos", tamano=28, color=GREEN),
            self.texto("Cantidad final: 100 L + 25 L = 125 L", tamano=30, color=BLUE)
        ).arrange(DOWN, buff=0.3)
        resultado.next_to(unidades, DOWN, buff=0.5)
        self.escribir(resultado, tiempo=9)

    def cierre(self):
        titulo = self.iniciar_seccion("Respuesta a la pregunta inicial")
        cierre_a = self.texto("Integrar la tasa entrega el cambio acumulado.", tamano=28)
        cierre_b = self.texto("Para conocer la cantidad final, falta la cantidad inicial.", tamano=28)
        textos = VGroup(cierre_a, cierre_b).arrange(DOWN, buff=0.5)
        textos.next_to(titulo, DOWN, buff=0.6)
        self.escribir(textos, tiempo=11)

        tabla = VGroup()
        for nombre, valores, color in [
            ("Inicial", ("100 L", "40 L"), BLUE),
            ("Cambio", ("+25 L", "+25 L"), YELLOW),
            ("Final", ("125 L", "65 L"), GREEN)
        ]:
            columna = VGroup(
                self.texto(nombre, tamano=26, color=GRAY),
                *[self.texto(valor, tamano=38, color=color) for valor in valores]
            ).arrange(DOWN, buff=0.35)
            tabla.add(columna)
        tabla.arrange(RIGHT, buff=1.5, aligned_edge=UP)
        tabla.next_to(textos, DOWN, buff=0.7)
        self.escribir(tabla, tiempo=10)

        cantidad_final = self.texto("Cantidad final = Cantidad inicial + Cambio acumulado", tamano=28, color=YELLOW)
        cantidad_final.next_to(tabla, DOWN, buff=0.6)
        self.escribir(cantidad_final, tiempo=6)

        aclaracion = self.texto("Si la cantidad inicial es cero, la integral coincide con la final", tamano=24, color=GRAY)
        aclaracion.next_to(cantidad_final, DOWN, buff=0.4)
        self.escribir(aclaracion, tiempo=6)

    def creditos(self):
        titulo = self.iniciar_seccion("Fuentes y recursos")
        fuentes = self.texto(
            "Apuntes del curso: Introducción a la integral (2026).\n"
            "Larson y Edwards: Cálculo 1 de una variable, 9.ª ed. (2010).\n"
            "Stewart, J. (2012). Cálculo de varias variables:\n"
            "Trascendentes tempranas, 7.ª ed. Cengage Learning.\n"
            "Manim Community: docs.manim.community\n\n"
            "Declaración de IA:\n"
            "ChatGPT/Codex: apoyo en el desarrollo y correcion del código.\n"
            "Verificación: comprobación de cálculos, ejecución en Manim\n"
            "y revisión visual de las escenas.", tamano=22
        )
        fuentes.next_to(titulo, DOWN, buff=0.6)
        self.mostrar(fuentes, tiempo=20)