# Fechas

from datetime import datetime, timedelta

# Obtener fecha y hora actual .now()

now = datetime.now()
print(now)

# Crear una fecha y hora especifica

specific_date = datetime(2026, 2, 2)
print(f"Fecha especifica: {specific_date}")

# Formatear fechas
# metodo strftime() para formatear fechas
# Funciona mediante directivas que inician con el simbolo %
import locale
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
format_date = now.strftime("%A %B %Y %H:%M:%S")
print(f"Fecha formateada: {format_date}")

# Operaciones con fechas (sumar/restar dias, minutos, horas, meses)

yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer: {yesterday}")

tomorrow = datetime.now() + timedelta(days=1)
print(f"Mañana: {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"Hora despues: {one_hour_after}")

# Obtener componentes individuales de una fecha

year = now.year
print(year)

month = now.month
print(month)

# Calcular la diferencia entre 2 fechas
date1 = datetime.now()
date2 = datetime(2026, 5, 10)
difference = date2 - date1
print(f"{difference.days} dias de diferencia")
