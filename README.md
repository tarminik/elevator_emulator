# Эмулятор Лифта

### Описание
Этот проект представляет собой эмулятор работы лифта в многоэтажном доме. Лифт может быть вызван с любого этажа, а также внутри кабины можно выбирать целевые этажи. Пользователь может в любой момент взаимодействовать с лифтом и наблюдать его текущее состояние: этаж, направление движения и остановки.

### Возможности
- Вызов лифта с любого этажа.
- Выбор целевого этажа внутри кабины лифта.
- Многопоточная работа: лифт может продолжать движение, пока пользователь вводит команды.
- Отображение состояния лифта в реальном времени: текущий этаж, направление движения, остановки.

### Управление
При запуске программы в консоль выводятся инструкции по доступным командам:
- `F<этаж>` — Вызвать лифт на указанный этаж (например, `F1` для вызова на 1 этаж).
- `C<этаж>` — Выбрать этаж внутри кабины лифта (например, `C4` для выбора 4 этажа).
- `!q` — Завершить работу программы.

### Установка и запуск
1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/tarminik/elevator_emulator.git
    ```

2. Перейдите в папку проекта:
    ```bash
    cd elevator_emulator
    ```

3. Запустите программу:
    ```bash
    python3 elevator.py # для Linux/MacOS
    python elevator.py # для Windows
    ```

### Пример использования

```bash
    Welcome to the Elevator Simulator!
    Available commands:
    - F<floor>: Call the elevator to a specific floor (e.g., F1 for floor 1).
    - C<floor>: Press a button inside the elevator to go to a specific floor (e.g., C4 for floor 4).
    - !q: Quit the program.

Enter the number of floors in the building: 5

>> F1
Floor 1 called the elevator.
Cabin on floor 3. Going down. <Press any key to enter new command>
Cabin on floor 2. Going down. <Press any key to enter new command>
>> C4
Button for floor 4 pressed inside the cabin.
Cabin on floor 1. Going up. <Press any key to enter new command>
...
```
