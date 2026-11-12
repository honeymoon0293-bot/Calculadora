import cmath
import math


def leer_coeficientes():
	"""Lectura de coeficientes  de ax² + bx + c."""
	return tuple(float(input(f"Introduce {nombre}: ")) for nombre in ("a", "b", "c"))


def resolver_ecuacion(a, b, c):
	if a == 0:
		if b == 0:
			print("Infinitas soluciones." if c == 0 else "No hay soluciones.")
		else:
			print(f"Solución: x = {-c / b:g}")
		return

	discriminante = b * b - 4 * a * c
	raiz = cmath.sqrt(discriminante)
	x1 = (-b + raiz) / (2 * a)
	x2 = (-b - raiz) / (2 * a)
	if discriminante >= 0:
		print(f"Soluciones: x₁ = {x1.real:g}, x₂ = {x2.real:g}")
	else:
		print(f"Soluciones complejas: x₁ = {x1}, x₂ = {x2}")


def resolver_desigualdad(a, b, c, operador):
	evaluar = lambda x: a * x * x + b * x + c
	comparar = {
		"<": lambda valor: valor < 0,
		"<=": lambda valor: valor <= 0,
		">": lambda valor: valor > 0,
		">=": lambda valor: valor >= 0,
	}[operador]

	if a != 0:
		discriminante = b * b - 4 * a * c
		if discriminante < 0:
			raices = []
		elif discriminante == 0:
			raices = [-b / (2 * a)]
		else:
			raiz = math.sqrt(discriminante)
			raices = sorted(((-b - raiz) / (2 * a), (-b + raiz) / (2 * a)))
	elif b != 0:
		raices = [-c / b]
	else:
		print("Solución: todos los números reales." if comparar(c) else "Solución: conjunto vacío.")
		return

	limites = [None] + raices + [None]
	intervalos = []
	for izquierda, derecha in zip(limites, limites[1:]):
		if izquierda is None:
			muestra = derecha - max(1, abs(derecha))
		elif derecha is None:
			muestra = izquierda + max(1, abs(izquierda))
		else:
			muestra = (izquierda + derecha) / 2

		if comparar(evaluar(muestra)):
			corchete_izq = "[" if izquierda is not None and comparar(evaluar(izquierda)) else "("
			corchete_der = "]" if derecha is not None and comparar(evaluar(derecha)) else ")"
			inicio = f"{izquierda:g}" if izquierda is not None else "−∞"
			fin = f"{derecha:g}" if derecha is not None else "∞"
			intervalos.append(f"{corchete_izq}{inicio}, {fin}{corchete_der}")

	for raiz in raices:
		if comparar(evaluar(raiz)):
			intervalos.append(f"{{{raiz:g}}}")

	print("Solución: " + (" ∪ ".join(intervalos) if intervalos else "conjunto vacío."))


def main():
	while True:
		print("\nCalculadora de ecuaciones cuadráticas y desigualdades")
		print("1. Resolver ax² + bx + c = 0")
		print("2. Resolver ax² + bx + c <, <=, > o >= 0")
		print("0. Salir")
		opcion = input("Elige una opción: ").strip()

		if opcion == "0":
			break
		if opcion not in ("1", "2"):
			print("Opción no válida.")
			continue

		try:
			a, b, c = leer_coeficientes()
			if opcion == "1":
				resolver_ecuacion(a, b, c)
			else:
				operador = input("Operador (<, <=, >, >=): ").strip()
				if operador not in ("<", "<=", ">", ">="):
					print("Operador no válido.")
				else:
					resolver_desigualdad(a, b, c, operador)
		except ValueError:
			print("Entrada no válida: introduce números.")


if __name__ == "__main__":
	main()
