![Tec de Monterrey](../../images/logotecmty.png)
# Pass Fail Grade
Decisiones - Calificacion aprobatoria o reprobatoria

Modifica el programa que se encuentra en la carpeta `src` que se llama
`main.py` y que contiene el siguiente código:

```python
def check_grade(grade):
    # Write your code here
    pass


def main():
    grade = int(input("Ingresa calificación: "))
    print(check_grade(grade))


if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario,
el programa la va a ignorar al ejecutarse.

El programa va a preguntar por una calificación numerica, entre 0 y 100.
Añade el código necesario para que el programa imprima **Aprobado** si la
calificación es mayor o igual a 70, o que imprima **Reprobado** si la
calificación es menor a 70.

La salida del programa debe de ser exactamente de la siguiente forma:

```plaintext
Ingresa calificación: 90
Aprobado
```

Únicamente necesitas modificar la función **check_grade** y asegurarte de
que regrese la palabra correcta.

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest --tb=short`,
subela a tu repositorio en GitHub, con el proceso de commit + push.
