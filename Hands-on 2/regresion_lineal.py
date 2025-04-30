class RegresionLineal:
    def __init__(self, datos):
        self.datos = datos
        self.n = len(datos)
        
    def calcular_sumatorias(self):
        #Inicializamos las cuatro sumatorias
        suma_x = 0
        suma_y = 0
        suma_x2 = 0
        suma_xy = 0
        
        #Calculamos las sumatorias
        for x, y in self.datos:
            suma_x += x
            suma_y += y
            suma_x2 += x ** 2
            suma_xy += x * y
        
        #Guardamos las sumatorias
        self.suma_x = suma_x
        self.suma_y = suma_y
        self.suma_x2 = suma_x2
        self.suma_xy = suma_xy
        
    def calcular_beta1(self):
        #Aplicamos la fórmula de beta1
        #Separamos en tres calculos
        numerador_beta1 = self.n * self.suma_xy - self.suma_x * self.suma_y
        denominador_beta1 = self.n * self.suma_x2 - self.suma_x ** 2
        beta1 = numerador_beta1 / denominador_beta1
        return beta1
    
    def calcular_beta0(self):
        #Aplicamos la fórmula de beta0
        #Separamos en tres calculos
        numerador_beta0 = self.suma_x2 * self.suma_y - self.suma_x * self.suma_xy
        denominador_beta0 = self.n * self.suma_x2 - self.suma_x ** 2
        beta0 = numerador_beta0 / denominador_beta0
        return beta0
    
    def predecir(self, x, beta0, beta1):
        #Usamos la ecuacion para predecir
        return beta0 + beta1 * x


datos = [
    (23, 651), (26, 762), (30, 856), (34, 1063), (43, 1190),
    (48, 1298), (52, 1421), (57, 1440), (58, 1518)
]


modelo = RegresionLineal(datos)


modelo.calcular_sumatorias()


beta1 = modelo.calcular_beta1()


beta0 = modelo.calcular_beta0()

#Mostrar la ecuación de la recta
print(f"Ecuación de la recta: y = {beta0:.5f} + {beta1:.5f}x")

#Predecimos los 5 valores de x diferentes al dataset
valores_publicidad = [19, 25, 40, 50, 60]

#Mostrar las predicciones
print("\nPredictions:")
for x in valores_publicidad:
    y_pred = modelo.predecir(x, beta0, beta1)
    print(f"Advertising = {x:.2f}, sales = {y_pred:.2f}")
