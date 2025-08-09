

# Создаем собственный класс исключения
class MyCustomError(Exception):
    def __init__(self, message):
        super().__init__(message)  # Передаем сообщение базовому классу
        self.message = message

# Пример использования
try:
    # Имитируем ошибку
    raise MyCustomError("Произошла критическая ошибка!")
except MyCustomError as e:
    print(f"Поймано исключение: {e.message}")
