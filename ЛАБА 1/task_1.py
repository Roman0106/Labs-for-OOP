class Table:
    """
    Абстрактный класс, описывающий стол.
    Характеристики:
    - Материал: материал изготовления стола (например, дерево, металл).
    - Форма: форма стола (например, круглый, прямоугольный).
    - Высота: высота стола в сантиметрах.

    """

    def __init__(self, material: str, shape: str, height: int):
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        self.material = material
        self.shape = shape
        self.height = height

    def fold(self) -> None:
        """
        Сложить стол, если он складной.

         Пример:
        >>> table.fold()  #doctest пользования методом

        """
        ...

    def change_height(self, new_height: int) -> None:
        """
        Изменить высоту стола.

        :param new_height: Новая высота стола.
        :raises ValueError: Если высота стола меньше ил равна нулю.

        """
        if new_height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        self.height = new_height

    def clean(self) -> None:
        """
        Очистить поверхность стола.

        """
        ...


class Tree:
    """
    Абстрактный класс, описывающий дерево.
    Характеристики:
    - Вид: вид дерева (например, клён, берёза).
    - Высота: высота дерева в метрах.
    - Возраст: возраст дерева в годах.
    """

    def __init__(self, species: str, height: float, age: int):
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.species = species
        self.height = height
        self.age = age

    def grow(self, years: int) -> None:
        """
        Увеличить возраст и высоту дерева.

        :param years: Количество лет, на которое увеличивается возраст.

        """
        if years < 0:
            raise ValueError("Количество лет не может быть отрицательным.")
        self.age += years
        self.height += years * 0.5  # Примерное увеличение высоты в метрах

    def shed_leaves(self) -> None:

        """
        Опадение листьев у дерева.

        """
        ...


class SocialMediaPlatform:
    """
    Абстрактный класс, описывающий социальную медиа-платформу.
    Характеристики:
    - Название: название платформы (например: Telegram, VK).
    - Количество пользователей: текущее количество зарегистрированных пользователей.
    - Год основания: год создания платформы.
    """

    def __init__(self, name: str, user_count: int, founding_year: int):
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        if founding_year > 2024:
            raise ValueError("Год основания не может превышать текущий.")
        self.name = name
        self.user_count = user_count
        self.founding_year = founding_year

    def add_user(self, user_id: str) -> None:
        """
        Добавить нового пользователя на платформу.

        :param user_id: Уникальный айди пользователя.

        """

    def remove_user(self, user_id: str) -> None:

        """
        Удалить пользователя с платформы.

        :param user_id: Уникальный айди пользователя.

        """

        ...
