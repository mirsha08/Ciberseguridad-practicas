# Control de intentos de login

# Definimos función que calcula el % de intentos de inicio fallidos
def calculate_fails(total_attempts, failed_attempts):
  fail_porcentage =(failed_attempts /total_attempts)
  return fail_porcentage

# definimos variable porcentage donde se calcula, pasamos los valores para total_attempts y failed_attempts,
# En caso real estos valores los tiene que proporcionar directamente el entorno del usuario.

porcentage = calculate_fails(4, 2) 

# Condicional para evaluar si el porcentaje está en alerta con mensaje en pantalla de alerta
if (percentage >= 0.5):
  print("Acoount locked.")
