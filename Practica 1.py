import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Se inicializa el puntaje
user_points = 0

# Se generan las preguntas con sus respuestas
questions_to_ask = random.sample(list(zip(questions,answers, correct_answers_index)), k=3)
# El usuario deberá contestar 3 preguntas
for que, opt, ans in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(que)
    for i, answer in enumerate(opt):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        # Se verifica si la respuesta es valida
        if user_answer in ["1","2","3","4"]:
            user_answer = int(user_answer) - 1
        else:
            print("Respuesta no válida")
            sys.exit(1)
        # Se verifica si la respuesta es correcta y se incrementa el puntaje
        # o se disminuye en el caso contrario
        if user_answer == ans:
            print("¡Correcto!")
            user_points += 1
            break
        else:
            user_points -= 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(opt[ans])

    # Se imprime un blanco al final de la pregunta
    print()
# Se convierte el puntaje negativo a cero, que es el puntaje mínimo posible
if user_points <= 0:
    user_points = 0
# Se imprime el puntaje
print(f"Obtuviste un total de {user_points} puntos")