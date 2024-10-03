def hanoi_tower(n, source, target, auxiliary, state):
    if n == 1:
        # Перемістити диск 1 зі стрижня source на стрижень target
        print(f"Перемістити диск з {source} на {target}: {state[source][-1]}")
        state[target].append(state[source].pop())  # Оновлюємо стан стрижнів
        print(f"Проміжний стан: {state}")
    else:
        # Перемістити n-1 дисків з source на auxiliary, використовуючи target як допоміжний
        hanoi_tower(n - 1, source, auxiliary, target, state)
        
        # Перемістити найбільший диск (n) зі стрижня source на стрижень target
        print(f"Перемістити диск з {source} на {target}: {state[source][-1]}")
        state[target].append(state[source].pop())  # Оновлюємо стан стрижнів
        print(f"Проміжний стан: {state}")
        
        # Перемістити n-1 дисків з auxiliary на target, використовуючи source як допоміжний
        hanoi_tower(n - 1, auxiliary, target, source, state)

def main():
    n = int(input("Введіть кількість дисків: "))  # Запитуємо кількість дисків
    state = {
        'A': list(range(n, 0, -1)),  # Ініціалізуємо стрижень A з дисками (від найбільшого до найменшого)
        'B': [],  # Стрижень B порожній
        'C': []   # Стрижень C порожній
    }
    
    print(f"Початковий стан: {state}")
    hanoi_tower(n, 'A', 'C', 'B', state)  # Викликаємо функцію для переміщення дисків
    print(f"Кінцевий стан: {state}")

if __name__ == "__main__":
    main()
