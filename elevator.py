import time
import threading


class Elevator:
    def __init__(self, floors):
        self.floors = floors
        self.current_floor = 3  # Лифт начинается с 3-го этажа
        self.target_floors = []  # Очередь вызовов
        self.direction = "stopped"  # Лифт может двигаться "up", "down" или быть "stopped"
        self.lock = threading.Lock()  # Для синхронизации ввода
        self.running = True  # Флаг для остановки программы

    def move(self):
        while self.running:
            with self.lock:
                if not self.target_floors:
                    self.direction = "stopped"
                elif self.current_floor < self.target_floors[0]:
                    self.direction = "up"
                    self.current_floor += 1
                elif self.current_floor > self.target_floors[0]:
                    self.direction = "down"
                    self.current_floor -= 1
                else:
                    self.direction = "stopped"
                    self.target_floors.pop(0)
                    print(f"Cabin on floor {self.current_floor}. Stopped. Doors opened")
                    time.sleep(2)  # Ожидание открытия дверей

            if self.direction != "stopped":
                print(
                    f"Cabin on floor {self.current_floor}. Going {self.direction}. <Press any key to enter new command>")
                time.sleep(1)  # Эмуляция времени перемещения лифта

    def call_elevator(self, floor):
        with self.lock:
            if floor not in self.target_floors:
                self.target_floors.append(floor)
                self.target_floors.sort()  # Упорядочиваем вызовы по очереди
            print(f"Floor {floor} called the elevator.")

    def cabin_button_pressed(self, floor):
        with self.lock:
            if floor not in self.target_floors:
                self.target_floors.append(floor)
                self.target_floors.sort()
            print(f"Button for floor {floor} pressed inside the cabin.")


def print_instructions():
    instructions = """
    Welcome to the Elevator Simulator!
    Available commands:
    - F<floor>: Call the elevator to a specific floor (e.g., F1 for floor 1).
    - C<floor>: Press a button inside the elevator to go to a specific floor (e.g., C4 for floor 4).
    - !q: Quit the program.
    """
    print(instructions)


def main():
    # Вывод инструкции по управлению
    print_instructions()

    floors = int(input("Enter the number of floors in the building: "))

    elevator = Elevator(floors)

    # Запускаем движение лифта в отдельном потоке
    threading.Thread(target=elevator.move, daemon=True).start()

    while elevator.running:
        command = input(">>").strip().lower()
        if command == "!q":  # Команда для выхода из программы
            elevator.running = False
            print("Exiting the program...")
        elif command.startswith("f"):  # Вызов лифта с этажа
            floor = int(command[1:])
            if 1 <= floor <= floors:
                elevator.call_elevator(floor)
            else:
                print(f"Invalid floor number. Please choose a floor between 1 and {floors}.")
        elif command.startswith("c"):  # Кнопка внутри кабины лифта
            floor = int(command[1:])
            if 1 <= floor <= floors:
                elevator.cabin_button_pressed(floor)
            else:
                print(f"Invalid floor number. Please choose a floor between 1 and {floors}.")
        else:
            print("Unknown command. Use F<floor> for calling from floor, C<floor> for cabin buttons, or !q to quit.")


if __name__ == "__main__":
    main()
