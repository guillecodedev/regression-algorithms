# 📈 Algoritmos de Regresión en Python

Este módulo implementa visualizaciones interactivas de los algoritmos de regresión más comunes en Machine Learning utilizando scikit-learn.

## 📋 Contenido

### 1. Regresión Lineal
La función `plot_linear_regression()` visualiza el ajuste de una línea recta a los datos.

**Características principales:**
- Ajuste de una línea recta a los datos
- Visualización de los puntos originales
- Representación clara de la relación lineal
- Incluye la línea de mejor ajuste

### 2. Regresión Polinómica
La función `plot_polynomial_regression()` muestra el ajuste de una curva no lineal.

**Características principales:**
- Ajuste de una curva polinómica de grado 2
- Visualización de los puntos originales
- Representación de relaciones no lineales
- Muestra la flexibilidad del modelo polinómico

## 🛠️ Requisitos

```python
numpy==1.21.0
matplotlib==3.4.3
scikit-learn==0.24.2

pip install numpy matplotlib scikit-learn
```

## 🚀 Uso

```python
# Importar las funciones necesarias
from visualizations import plot_linear_regression, plot_polynomial_regression

# Generar visualizaciones individuales
plot_linear_regression()
plot_polynomial_regression()
```

## 📊 Ejemplos de Salida

Cada función generará una visualización detallada del algoritmo correspondiente:
- Regresión Lineal: Muestra la línea de mejor ajuste y los puntos de datos
- Regresión Polinómica: Muestra la curva de ajuste y los puntos de datos

## 🔍 Detalles Técnicos

### Regresión Lineal
- Utiliza el método de mínimos cuadrados
- Implementada usando `sklearn.linear_model.LinearRegression`
- Genera datos sintéticos con ruido controlado
- Visualiza la relación entre variables dependientes e independientes

### Regresión Polinómica
- Utiliza transformación polinómica de grado 2
- Implementada usando `PolynomialFeatures` y `LinearRegression`
- Genera datos cuadráticos con ruido
- Muestra la capacidad de ajuste a patrones no lineales

## 📝 Notas
- Los datos son generados sintéticamente para demostración
- Las visualizaciones son interactivas cuando se ejecutan en un notebook
- Los parámetros de los modelos pueden ajustarse según necesidades
- Se incluye una cuadrícula para mejor referencia visual

## 🔧 Personalización

Los gráficos pueden personalizarse modificando:
- Tamaño de la figura
- Colores de los puntos y líneas
- Etiquetas de los ejes
- Título de la visualización
- Transparencia de los puntos
- Estilo de la cuadrícula