# Importación de bibliotecas necesarias
import numpy as np  # Para operaciones numéricas y matrices
import matplotlib.pyplot as plt  # Para crear visualizaciones
from sklearn.linear_model import LinearRegression  # Algoritmos de regresión
from sklearn.preprocessing import PolynomialFeatures  # Para crear características polinómicas
from sklearn.datasets import make_regression  # Para generar datos sintéticos

# Configuración básica de matplotlib
plt.style.use('default')  # Usar el estilo predeterminado de matplotlib


def plot_linear_regression():
    """
    Visualiza la regresión lineal mostrando cómo se ajusta
    una línea recta a un conjunto de datos.
    """
    # Generar datos sintéticos para regresión
    X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=1)
    
    # Crear y entrenar el modelo de regresión lineal
    model = LinearRegression()
    model.fit(X, y)
    
    # Visualización
    plt.figure(figsize=(10, 8))
    # Dibujar los puntos de datos
    plt.scatter(X, y, color='blue', alpha=0.5, label='Datos')
    # Dibujar la línea de regresión
    plt.plot(X, model.predict(X), color='red', label='Regresión', linewidth=2)
    plt.title('Regresión Lineal')
    plt.xlabel('Variable independiente')
    plt.ylabel('Variable dependiente')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_polynomial_regression():
    """
    Visualiza la regresión polinómica mostrando cómo se ajusta
    una curva no lineal a un conjunto de datos.
    """
    # Generar datos sintéticos no lineales
    X = np.linspace(-3, 3, 100).reshape(-1, 1)
    y = 0.5 * X**2 + X + 2 + np.random.normal(0, 1, 100)  # Función cuadrática con ruido
    
    # Crear características polinómicas (añade términos cuadráticos)
    poly_features = PolynomialFeatures(degree=2)
    X_poly = poly_features.fit_transform(X)
    
    # Crear y entrenar el modelo
    model = LinearRegression()
    model.fit(X_poly, y)
    
    # Generar puntos para la curva de predicción
    X_plot = np.linspace(-3, 3, 300).reshape(-1, 1)
    X_plot_poly = poly_features.transform(X_plot)
    y_plot = model.predict(X_plot_poly)
    
    # Visualización
    plt.figure(figsize=(10, 8))
    plt.scatter(X, y, color='blue', alpha=0.5, label='Datos')
    plt.plot(X_plot, y_plot, color='red', label='Regresión polinómica', linewidth=2)
    plt.title('Regresión Polinómica')
    plt.xlabel('Variable independiente')
    plt.ylabel('Variable dependiente')
    plt.legend()
    plt.grid(True)
    plt.show()

# Punto de entrada principal
if __name__ == "__main__":
    print("Generando visualizaciones...")
    # Generar todas las visualizaciones una por una
    plot_linear_regression()
    plot_polynomial_regression()