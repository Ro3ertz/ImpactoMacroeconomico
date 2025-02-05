"""
Ejercicio Práctico: Análisis del Impacto del Macroambiente en una Empresa
Contexto del Problema
Una empresa manufacturera mexicana está evaluando cómo las condiciones macroeconómicas pueden afectar su rentabilidad en los próximos dos años. Los factores clave a considerar incluyen:

Inflación: Impacta el costo de materias primas y los precios de venta.
Tasa de interés: Afecta el costo de financiamiento de la empresa.
Tipo de cambio: Influye en la compra de insumos importados.
Crecimiento del PIB: Relacionado con la demanda de sus productos.
La empresa necesita proyectar su rentabilidad bajo diferentes escenarios económicos.

Datos del Problema
Supongamos que la empresa tiene los siguientes datos actuales:

Ventas actuales: $50,000,000 MXN anuales.
Costos de producción: $30,000,000 MXN anuales.
Préstamo bancario: $10,000,000 MXN con una tasa de interés del 10% anual.
Insumos importados: 40% de los costos de producción.
Margen de utilidad neta actual: 10%.
"""
import pandas as pd

# Datos iniciales
ventas_actuales = 50000000  # MXN
costos_produccion_actuales = 30000000  # MXN
prestamo = 10000000  # MXN
tasa_interes_actual = 0.10  # 10%
margen_utilidad_neta_actual = 0.10  # 10%

# Factores macroeconómicos
escenarios = {
    "Actual": {"inflacion": 0.05, "tasa_interes": 0.10, "tipo_cambio": 18, "PIB": 0.02},
    "Escenario 1": {"inflacion": 0.10, "tasa_interes": 0.12, "tipo_cambio": 18, "PIB": 0.01},
    "Escenario 2": {"inflacion": 0.06, "tasa_interes": 0.15, "tipo_cambio": 22, "PIB": -0.01},
}

# Cálculos para cada escenario
resultados = []
for escenario, valores in escenarios.items():
    inflacion = valores["inflacion"]
    tasa_interes = valores["tasa_interes"]
    tipo_cambio = valores["tipo_cambio"]

    # Aumento en costos de producción debido a inflación
    nuevos_costos_produccion = costos_produccion_actuales * (1 + inflacion)

    # Incremento en el costo financiero debido a la nueva tasa de interés
    intereses_prestamo = prestamo * tasa_interes

    # Utilidad bruta (Ventas - Costos de producción)
    utilidad_bruta = ventas_actuales - nuevos_costos_produccion

    # Utilidad neta (Utilidad bruta - intereses)
    utilidad_neta = utilidad_bruta - intereses_prestamo

    # Margen de utilidad neta
    margen_utilidad_neta = utilidad_neta / ventas_actuales

    resultados.append([escenario, nuevos_costos_produccion, intereses_prestamo, utilidad_neta, margen_utilidad_neta])

# Crear DataFrame para visualizar resultados
df_resultados = pd.DataFrame(resultados, columns=["Escenario", "Costos Producción", "Intereses Préstamo", "Utilidad Neta", "Margen Utilidad Neta"])

print(escenarios)
print(df_resultados)