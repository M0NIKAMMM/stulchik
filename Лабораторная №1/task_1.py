import doctest

class TikTok:
    def __init__(self, like: int, repost: int):
        """
        Создание и подготовка к работе объекта "ТиТок" (характеристики под видео пользователя)

        :param like: Количество лайков под видео
        :param repost: Количество репостов под видео

        Пример:
        >>> video = TikTok(100, 40)  # инициализация экземпляра класса
        """
        if not isinstance(like, (int)):
            raise TypeError("Количество лайков должно быть исключительно натуральным ЧИСЛОМ!!")
        if like < 0:
            raise ValueError("Количество лайков должно быть исключительно НАТУРАЛЬНЫМ числом!!")
        self.like = like

        if not isinstance(repost, (int)):
            raise TypeError("Количество репостов должно быть исключительно натуральным ЧИСЛОМ!!")
        if repost < 0:
            raise ValueError("Количество репостов должно быть исключительно НАТУРАЛЬНЫМ числом!!")
        self.repost = repost

    def increasing_the_number_of_likes(self, people: int) -> None:
        """
        Увеличение лайков под видео

        :param people: Люди, лайкнувшие данное видео

        Пример:
        >>> video = TikTok(100, 40)
        >>> video.increasing_the_number_of_likes(1000)
        """
        if not isinstance(people, (int)):
            raise TypeError("Количество людей, которым понравилось данное видео, должно быть исключительно натуральным ЧИСЛОМ!!")
        if people < 0:
            raise ValueError("Количество людей, которым понравилось данное видео, должно быть исключительно НАТУРАЛЬНЫМ числом!!")
        ...

    def increasing_the_number_of_reposts(self, people: int) -> None:
        """
        Увеличение репостов под видео

        :param people: Люди, которые репостнули данное видео

        Пример:
        >>> video = TikTok(100, 40)
        >>> video.increasing_the_number_of_reposts(200)
        """
        if not isinstance(people, (int)):
            raise TypeError("Количество людей, которые репостнули данное видео, должно быть исключительно натуральным ЧИСЛОМ!!")
        if people < 0:
            raise ValueError("Количество людей, которые репостнули данное видео, должно быть исключительно НАТУРАЛЬНЫМ числом!!")
        ...



class Cat:
    def __init__(self, poroda: str, vozrast: int):
        """
        Создание и подготовка к работе объекта "Кот"
        :param poroda: Порода кота
        :param vozrast: Возраст кота

        Пример:
        >>> Barsik = Cat("Британец", 5)  # инициализация экземпляра класса
        """
        if not isinstance(poroda, str):
            raise TypeError("Название породы должна содержать в себе исключительно буквы")
        self.poroda = poroda

        if not isinstance(vozrast, int):
            raise TypeError("Возраст должен содержать в себе исключительно натуральное число")
        if vozrast <= 0:
            raise ValueError("Возраст должен быть больше нуля")
        self.vozrast = vozrast

    def meow(self, myaukanie) -> None:
        """
        Кот мяукает.

        Пример:
        >>> Barsik = Cat("Британец", 5)
        >>> Barsik.meow("МИЯУУ!!!")
        """
        if not isinstance(myaukanie, str):
            raise TypeError("Коты мяукают буквами...")
        ...
    def sleep(self, spat) -> None:
        """
        Кот спит.

        Пример:
        >>> Barsik = Cat("Британец", 5)
        >>> Barsik.sleep("Кот принял для себя удобную позу и заснул... z-z-z...")
        """
        if not isinstance(spat, str):
            raise TypeError("Как можно в письменном формате передать сон кота иными символами, кроме букв?")
        ...

class suhariki:
    def __int__(self, vkus: str, cena: float):
        """
        Создание и подготовка к работе объекта "Сухарики"
        :param vkus: Вкус сухариков
        :param cena: Цена сухариков

        Пример:
        >>> kirieshki = suhariki("Сметана и зелень", 35.0)  # инициализация экземпляра класса
        """
        if not isinstance(vkus, str):
            raise TypeError("Вкус должен быть представлен буквами")
        self.vkus = vkus

        if not isinstance(cena, float):
            raise TypeError("Цена должна быть представлена целым числом")
        if cena <= 0:
            raise ValueError("Цена не может быть отрицательным числом или быть равной нулю")
        self.cena = cena

    def add_cena(self, new_cena) -> None:
        """
        Увеличение цены на сухарики

        Пример:
        >>> kirieshki = suhariki("Сметана и лук", 35.0)
        >>> kirieshki.add_cena(20.0)
        """

        if not isinstance(new_cena, float):
            raise TypeError("Новая цена должна быть представлена целым числом")
        if new_cena < 0:
            raise ValueError("Цена должна быть положительной")
        ...

    def buying(self, wanted_suhariki) -> None:
        """
        Увеличение цены на сухарики

        Пример:
        >>> kirieshki = suhariki("Сметана и лук", 35.0)
        >>> kirieshki.buying(wanted_suhariki)
        """

        if not isinstance(wanted_suhariki, str):
            raise TypeError("Желаемые сухарики должны быть представлены буквами")
        ...

if __name__ == "__main__":
    doctest.testmod()
