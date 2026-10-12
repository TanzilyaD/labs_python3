groupmates = [
    {
        "name": "Танзиля",
        "surname": "Долгополова",
        "exams": ["Информатика", "Метрология", "Web"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Алексей",
        "surname": "Смирнов",
        "exams": ["Информатика", "Метрология", "Web"],
        "marks": [4, 3, 4]
    },
    {
        "name": "Мария",
        "surname": "Кузнецова",
        "exams": ["Информатика", "Метрология", "Web"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Дмитрий",
        "surname": "Орлов",
        "exams": ["Информатика", "Метрология", "Web"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Елена",
        "surname": "Васильева",
        "exams": ["Информатика", "Метрология", "Web"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Игорь",
        "surname": "Новиков",
        "exams": ["Информатика", "Метрология", "Web"],
        "marks": [3, 4, 3]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(15),
          u"Экзамены".ljust(45), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(15),
              str(student["exams"]).ljust(45), str(student["marks"]).ljust(20))


def average_mark(student):
    return sum(student["marks"]) / len(student["marks"])


def filter_by_average(students, min_average):
    """Возвращает студентов, у которых средний балл выше заданного."""
    return [s for s in students if average_mark(s) > min_average]


print("Все студенты группы:")
print_students(groupmates)

threshold = float(input("\nВведите средний балл для фильтрации: ").replace(",", "."))
print("\nСтуденты со средним баллом выше", threshold, ":")
print_students(filter_by_average(groupmates, threshold))