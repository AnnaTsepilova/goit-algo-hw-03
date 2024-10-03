import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання

    t.penup()
    t.goto(-size / 2, size / 3)  # Позиціонуємо черепаху
    t.pendown()

    # Малюємо три сторони сніжинки Коха
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)  # Повертаємо черепаху для наступної сторони трикутника

    turtle.done()  # Завершення програми, очікування команди на закриття вікна

def main():
    # Отримуємо рівень рекурсії від користувача
    while True:
        try:
            order = int(input("Введіть рівень рекурсії (0 або більше): "))
            if order < 0:
                print("Рівень рекурсії повинен бути 0 або більше.")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    # Виклик функції для малювання сніжинки Коха
    draw_koch_snowflake(order)

if __name__ == "__main__":
    main()
