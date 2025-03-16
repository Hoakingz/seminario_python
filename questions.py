import random
import sys
 # Preguntas para el juego
questions = ["¿Qué función se usa para obtener la longitud de una cadena en Python?","¿Cuál de las siguientes opciones es un número entero en Python?",
 "¿Cómo se solicita entrada del usuario en Python?", "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
 "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",]
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
# se seleccionan 3 preguntas aleatorias
questions_to_ask = random.sample(list(zip(questions,answers, correct_answers_index)), k=3)
# contador de puntos
puntos = 0
# El usuario deberá contestar 3 preguntas
for questions, answers, correct_answers in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(questions)
    for i, answer in enumerate(answers):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = int(input("Respuesta: "))-1
    # Se verifica si la respuesta es correcta y suman puntos
        if user_answer == correct_answers:    
            print("¡Correcto!")
            puntos+=1
            break
    # se verifica si la respuesta no se encuentra en el index
        elif user_answer not in correct_answers_index:
            print ("respuesta invalida")
            sys.exit(1)
    # intento fallido resta puntos
        else:
            puntos+=-0.5
    else:
    # Si el usuario no responde correctamente después de 2 intentos,
    # se muestra la respu esta correcta y resta puntos
        print("Incorrecto. La respuesta correcta es:")
        print(answers[correct_answers])
        puntos+=-0.5
    # Se imprime un blanco al final de la pregunta
    print()
print(f"puntuacion: {puntos}/3")

#se tuvieron que reeplazar los indices porque las variables ya contaban con valores determinados, osea que se accedia a una direccion de forma directa
