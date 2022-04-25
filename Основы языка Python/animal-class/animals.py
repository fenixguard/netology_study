animals = ["корова", "коза", "овца", "курица", "утка", "гусь"]

missions = {
    1: "Покормить животных",
    2: "Подоить скот",
    3: "Постричь овец",
    4: "Собрать яйца"
}


class Animal:

    def __init__(self, name: str, weight: int, voice: str, type_animal: str):
        self.name = name
        self.weight = weight
        self.voice = voice
        self.feed = False
        self.type_animal = type_animal

    def feed_animals(self):
        self.feed = True


class Milk(Animal):

    def __init__(self, name: str, weight: int, voice: str, type_animal: str):
        super().__init__(name, weight, voice, type_animal)
        self.milk = False

    def to_milk(self):
        self.milk = True


class Shearing(Animal):

    def __init__(self, name: str, weight: int, voice: str, type_animal: str):
        super().__init__(name, weight, voice, type_animal)
        self.wool = False

    def to_cut(self):
        self.wool = True


class Eggs(Animal):

    def __init__(self, name: str, weight: int, voice: str, type_animal: str):
        super().__init__(name, weight, voice, type_animal)
        self.egg = False

    def to_eggs(self):
        self.egg = True


class Cow(Milk):

    def __init__(self, name: str, weight: int):
        super().__init__(name, weight, "muuu", "Корова")


class SheGoat(Milk):

    def __init__(self, name: str, weight: int):
        super().__init__(name, weight, "meee", "Коза")


class Sheep(Shearing):

    def __init__(self, name: str, weight: int):
        super().__init__(name, weight, "beee", "Овца")


class Chicken(Eggs):

    def __init__(self, name: str, weight: int):
        super().__init__(name, weight, "ko-ko-ko", "Курица")


class Duck(Eggs):

    def __init__(self, name: str, weight: int):
        super().__init__(name, weight, "krya-krya", "Утка")


class Goose(Eggs):

    def __init__(self, name: str, weight: int):
        super().__init__(name, weight, "ga-ga-ga", "Гусь")


def input_animal():
    animal_name = input("Введите кличку: ")
    animal_weight = int(input("Введите вес (кг): "))
    return animal_name, animal_weight


def detect_end_input_animal():
    end = input("Всех записали? (Да/Нет) ")
    if end.lower() == "да":
        return True
    else:
        return False


def output_animal(animal_list):
    for entity in animal_list:
        print(f"{entity.type_animal}: \nкличка: {entity.name.capitalize()}\nвес: {entity.weight}кг")
        print("-" * 20)
    return False


def welcome():
    global_flag = True
    country_farm = list()
    print("Добро пожаловать на ферму Дядюшки Джо!")
    print("Давай запишем всех животных в список, чтобы потом их не потерять.")
    while global_flag:
        animal = input("Какое животное ты видишь? ")
        if animal.lower() not in animals:
            print("Такого животного у Дядюшки Джо нет на ферме")
            print("Он оставил список всех животных, вот посмотри на него:")
            print(animals)
            continue

        if animal.lower() == "корова":
            animal_name, animal_weight = input_animal()
            country_farm.append(Cow(name=animal_name, weight=animal_weight))
            if detect_end_input_animal():
                global_flag = output_animal(country_farm)
            else:
                continue

        if animal.lower() == "коза":
            animal_name, animal_weight = input_animal()
            country_farm.append(SheGoat(name=animal_name, weight=animal_weight))
            if detect_end_input_animal():
                global_flag = output_animal(country_farm)
            else:
                continue

        if animal.lower() == "овца":
            animal_name, animal_weight = input_animal()
            country_farm.append(Sheep(name=animal_name, weight=animal_weight))
            if detect_end_input_animal():
                global_flag = output_animal(country_farm)
            else:
                continue

        if animal.lower() == "курица":
            animal_name, animal_weight = input_animal()
            country_farm.append(Chicken(name=animal_name, weight=animal_weight))
            if detect_end_input_animal():
                global_flag = output_animal(country_farm)
            else:
                continue

        if animal.lower() == "утка":
            animal_name, animal_weight = input_animal()
            country_farm.append(Duck(name=animal_name, weight=animal_weight))
            if detect_end_input_animal():
                global_flag = output_animal(country_farm)
            else:
                continue

        if animal.lower() == "гусь":
            animal_name, animal_weight = input_animal()
            country_farm.append(Goose(name=animal_name, weight=animal_weight))
            if detect_end_input_animal():
                global_flag = output_animal(country_farm)
            else:
                continue
    return country_farm


def mission_djo():
    view_missions = missions.copy()
    print("Дядюшка Джо оставил нам поручения")
    print("Взгляни на список:")
    for k, v in missions.items():
        print(f"{k} - {v}")

    while True:
        if len(view_missions) == 0:
            print("Ты выполнил все поручения Дядюшки Джо!")
            break
        activity = int(input("Чтобы выполнить дело из списка введи его номер: "))
        if activity not in view_missions.keys():
            print("Такого задания в списке еще нет, попробуй еще раз.")
            continue
        else:
            if activity == 1:
                to_feed()
                del view_missions[1]
                print("По списку осталось:")
                for k, v in view_missions.items():
                    print(f"{k} - {v}")

            elif activity == 2:
                to_milk()
                del view_missions[2]
                task_list(view_missions)

            elif activity == 3:
                to_wool()
                del view_missions[3]
                task_list(view_missions)

            elif activity == 4:
                to_egg()
                del view_missions[4]
                task_list(view_missions)


def task_list(missions_djo):
    print("По списку осталось:")
    for k, v in missions_djo.items():
        print(f"{k} - {v}")


def to_feed():
    for animal in country_farm:
        animal.feed_animals()
    print("Ты накормил всех животных!")


def to_milk():
    for animal in country_farm:
        if animal.type_animal == "Корова" or animal.type_animal == "Коза":
            animal.to_milk()
    print("Ты подоил коров и коз!")


def to_wool():
    for animal in country_farm:
        if animal.type_animal == "Овца":
            animal.to_cut()
    print("Ты постриг овец!")


def to_egg():
    for animal in country_farm:
        if animal.type_animal == "Курица" or animal.type_animal == "Утка" or animal.type_animal == "Гусь":
            animal.to_eggs()
    print("Ты собрал все яйца!")


def count_weight():
    total_weight = 0
    max_animal_weight = 0
    max_animal_name = str()
    max_animal_type = str()
    for animal in country_farm:
        total_weight += animal.weight
        if max_animal_weight < animal.weight:
            max_animal_weight = animal.weight
            max_animal_name = animal.name
            max_animal_type = animal.type_animal

    print(f"Суммарный вес всех животных на ферме составляет - {total_weight}кг")
    print(f"Самое увесистое животное - {max_animal_type} по кличке '{max_animal_name.capitalize()}' весом: {max_animal_weight}кг")


if __name__ == '__main__':
    country_farm = welcome()
    mission_djo()
    print("Теперь ты в курсе всех дел фермы Джо!")
    count_weight()
