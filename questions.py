# importacion de biblotecas random y sys(para el exit del sistema)
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
# se seleccionan 3 preguntas aleatorias no repetidas, con su respuesta e indice
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
        user_answer = (input("Respuesta: "))
        try:
            user_answer_int = int(user_answer)-1
         # se verifica si la respuesta no se encuentra en el index y sale del sistema con status=1
            if (user_answer_int)not in correct_answers_index:
                print ("respuesta invalida")
                sys.exit(1) 
        except ValueError:
                print ("respuesta invalida")
                sys.exit(1)  
            # Se verifica si la respuesta es correcta y suman puntos
        if int(user_answer)-1 == correct_answers:    
            print("¡Correcto!")
            puntos+=1
            break
    # intento fallido resta puntos
        else:
            puntos+=-0.5
    else:
    # Si el usuario no responde correctamente después de 2 intentos,
    # se muestra la respu esta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[correct_answers])
    # Se imprime un blanco al final de la pregunta
    print()
# se muestra el puntaje final
print(f"puntuacion: {puntos}/3")

#se tuvieron que reeplazar los indices porque las variables ya contaban con valores determinados, osea que se accedia a una direccion de forma directa
