from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    # Проверка добавления книг
    def test_add_new_book_add_two_books(self):
        """
        - создаем экземпляр (объект) класса BooksCollector
        - добавляем две книги
        - проверяем, что добавилось именно две,
          словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        """
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    # Нельзя добавить одну и ту же книгу дважды.
    def test_add_new_book_not_add_existing_book(self):
        """
        - создаем объект BooksCollector м пустым словарем books_rating
        - test_book - книга которую будем добавлять два раза
        - добавляем книгу в словарь первый раз
        - добавляем ту же самую книгу повторно
        - проверяем, что количество книг в словаре равно одному, т.е. книга не добавилась повторно
        """
        collector = BooksCollector()
        test_book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(test_book)
        collector.add_new_book(test_book)
        assert len(collector.get_books_rating()) == 1

    # нельзя присвоить значение ретинга для книги,которой нет в словаре
    def test_get_book_rating_book_not_in_books_rating(self):
        """
        - создаем объект BooksCollector м пустым словарем books_rating
        - книга не добавленная в словарь books_rating
        - пытаемся установить рейтинг 3 для книги не добавленной в словарь
        - проверяем, что словарь не содержить значение с ключем book_not_in_books_rating
        """
        collector = BooksCollector()
        book_not_in_books_rating = "Три мушкетера"
        collector.set_book_rating(book_not_in_books_rating, 3)
        assert collector.get_book_rating(book_not_in_books_rating) is None

    # Нельзя выставить рейтинг меньше 1
    def test_set_book_rating_not_set_rating_less_1(self):
        """
        - создаем объект BooksCollector м пустым словарем books_rating
        - book - название добавляемой книга
        - добавляем новую книгу book в словарь
        - значение рейтинга = 3 для книги book
        - устанавливаем рейтинг test_less_1_rating для книги book
        - проверяем, что рейтинг test_less_1_rating для book не установился
        """
        collector = BooksCollector()
        book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book)
        test_less_1_rating = 0
        collector.set_book_rating(book, test_less_1_rating)
        assert collector.get_book_rating(book) == 1

    # Нельзя выставить рейтинг больше 10
    def test_set_book_rating_not_set_rating_more_10(self):
        """
        - создаем объект BooksCollector м пустым словарем books_rating
        - book - название добавляемой книга
        - добавляем новую книгу book в словарь
        - значение рейтинга = 11 для книги book
        - устанавливаем рейтинг test_less_1_rating для книги book
        - проверяем, что рейтинг test_less_1_rating для book не установился
        """
        collector = BooksCollector()
        book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book)
        test_more_10_rating = 11
        collector.set_book_rating(book, test_more_10_rating)
        assert collector.get_book_rating(book) == 1

    # Добавление книги в избранное.
    def test_add_book_in_favorites_add_book_from_book_ratings(self):
        """
        - создаем объект BooksCollector м пустым словарем books_rating
        - book - название добавляемой книги
        - добавляем новую книгу book в словарь
        - добавляем новую книгу в список избранного favorites
        - проеряем вхождение книги book в словарь favorites
        """
        collector = BooksCollector()
        book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert book in collector.get_list_of_favorites_books()

    # Нельзя добавить книгу в избранное, если её нет в словаре books_rating.
    def test_add_book_in_favorites_added_book_not_in_book_ratings(self):
        """
        - создаем объект BooksCollector м пустым словарем books_rating
        - test_book_not_in_book_rating - название книги, которую будем искать в списке favorites
        - добавляем test_book_not_in_book_rating в список favorites
        - проверям, что добавленная книга test_book_not_in_book_rating отсутствует в списке favorites
        """
        collector = BooksCollector()
        test_book_not_in_book_rating = 'Гордость и предубеждение и зомби'
        collector.add_book_in_favorites(test_book_not_in_book_rating)
        assert test_book_not_in_book_rating not in collector.get_list_of_favorites_books()

    # Проверка удаления книги из избранного.
    def test_delete_book_from_favorites_deleted_book_not_in_favorites(self):
        """
        - создаем объект BooksCollector м пустым словарем books_rating
        - book - название добавляемой книги
        - добавляем новую книгу book в словарь
        - добавляем book в список favorites
        - удаляем книгу book из списка favorites
        - проверяем, что книга book отсутсвует в списке favorites
        """
        collector = BooksCollector()
        book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert book not in collector.get_list_of_favorites_books()

    # Позитивный сценарии для set_book_rating и get_book_rating
    def test_set_book_rating_get_corresponds_rating(self):
        """
        - создаем объект BooksCollector м пустым словарем books_rating
        - book - название добавляемой книга
        - добавляем новую книгу book в словарь
        - значение рейтинга = 5 для книги book
        - устанавливаем рейтинг test_less_1_rating для книги book
        - проверяем, что рейтинг test_less_1_rating для book не установился
        """
        collector = BooksCollector()
        book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book)
        rating = 5
        collector.set_book_rating(book, rating)
        assert collector.get_book_rating(book) == rating

    # добавление списка книг с разными ретингами, получение списка с определенным рейтингом
    # позитивная проверка метода get_books_with_specific_rating
    def test_get_books_with_specific_rating_add_books_get_count_of_specific_rating(self, books_dict):
        """
        - создаем объект BooksCollector м пустым словарем books_rating
        - book_dict - словарь с парами название книги и целевой рейтинг
        - В цикле добавляем данные из book_dict в book_rating и выставляем соотвествующий рейтинг
        - проверяем для метод возвращает список с тремя записями по рейтингу 6
        :param books_dict: фикстура со словарем книг и их рейтинга
        """
        collector = BooksCollector()
        for key, value in books_dict.items():
            collector.add_new_book(key)
            collector.set_book_rating(key, value)
        assert len(collector.get_books_with_specific_rating(6)) == 3

    # Позитивный сценарии для метода get_books_rating - вывод словаря
    def test_get_books_rating_add_books_get_list(self, books_dict):
        """
        - добавляем в объект книги из фикстуры
        - проверяем, что метод get_books_rating вернул словарь
          и его длина соответсвует словарю books_dict
        :param books_dict: фикстура со словарем книг и их рейтинга
        """
        collector = BooksCollector()
        for key, value in books_dict.items():
            collector.add_new_book(key)
            collector.set_book_rating(key, value)
        books_rating = collector.get_books_rating()
        assert len(books_rating) == 10 and type(books_rating) is dict
