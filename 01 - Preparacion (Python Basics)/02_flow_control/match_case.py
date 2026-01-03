def sum_numbers(a: int, b: int) -> int:
  """Suma dos números"""
  return a + b


def rest_numbers(a: int, b: int) -> int:
  """Resta dos números"""
  return a - b


def multiply_numbers(a: int, b: int) -> int:
  """Multiplica dos números"""
  return a * b


def divide_numbers(a: int, b: int) -> float | str:
  """Divide dos números"""
  if b == 0:
    return "Error: no se puede dividir entre 0"
  return a / b


def show_menu() -> None:
  print("\nElige una de las siguientes opciones:\n")
  print("""
  1. Sumar
  2. Restar
  3. Multiplicar
  4. Dividir
  5. Salir del programa
  """)


def get_numbers() -> tuple[int, int]:
  """Solicita dos números al usuario"""
  first_num = int(input("Ingresa el primer número: "))
  second_num = int(input("Ingresa el segundo número: "))
  return first_num, second_num


flag = True

while flag:
  show_menu()

  try:
    user_option = int(input("Ingresa la opción de la operación que deseas realizar: "))

    match user_option:
      case 1:
        a, b = get_numbers()
        result = sum_numbers(a, b)
        print(f"El resultado de sumar {a} + {b} es: {result}")

      case 2:
        a, b = get_numbers()
        result = rest_numbers(a, b)
        print(f"El resultado de restar {a} - {b} es: {result}")

      case 3:
        a, b = get_numbers()
        result = multiply_numbers(a, b)
        print(f"El resultado de multiplicar {a} x {b} es: {result}")

      case 4:
        a, b = get_numbers()
        result = divide_numbers(a, b)
        print(f"El resultado de dividir {a} / {b} es: {result}")

      case 5:
        print("Saliendo del programa...")
        flag = False

      case _:
        print("ERROR: Ingresaste una opción inválida, intenta de nuevo.")

  except ValueError:
    print("ERROR: Debes ingresar solo valores numéricos.")
