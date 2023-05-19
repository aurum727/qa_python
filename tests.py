from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    # Проверка добавления книг
    def test_add_new_book_add_two_books_result_len_books_rating_2(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # Нельзя добавить одну и ту же книгу дважды.
    def test_add_new_book_not_add_existing_book_true(self):
        # создаем объект BooksCollector м пустым словарем books_rating
        collector = BooksCollector()
        # книга которую будем добавлять два раза
        test_book = 'Гордость и предубеждение и зомби'
        # добавляем книгу в словарь первый раз
        collector.add_new_book(test_book)
        # добавляем ту же самую книгу повторно
        collector.add_new_book(test_book)
        # счетчик для подсчета количества записи тестовой книги в словаре
        count_test_book_in_books_rating = 0
        # считаем количество ключей с именем test_book в словаре books_rating
        for book in collector.get_books_rating().keys():
            if book == test_book:
                count_test_book_in_books_rating += 1
        # проверяем, что в словаре только одна запись с именем test_book
        assert count_test_book_in_books_rating == 1

    # нельзя присвоить значение ретинга для книги,которой нет в словаре
    def test_get_book_rating_book_not_in_books_rating_none(self):
        # создаем объект BooksCollector м пустым словарем books_rating
        collector = BooksCollector()
        # книга не добавленная в словарь books_rating
        book_not_in_books_rating = "Три мушкетера"
        # пытаемся установить рейтинг 3 для книги не добавленной в словарь
        collector.set_book_rating(book_not_in_books_rating, 3)
        # проверяем, что словарь не содержить значение с ключем book_not_in_books_rating
        assert collector.get_book_rating(book_not_in_books_rating) is None

    # Нельзя выставить рейтинг меньше 1
    def test_set_book_rating_not_set_rating_less_1_true(self):
        # создаем объект BooksCollector м пустым словарем books_rating
        collector = BooksCollector()
        # название добавляемой книга
        book = 'Гордость и предубеждение и зомби'
        # добавляем новую книгу book в словарь
        collector.add_new_book(book)
        # значение рейтинга = 3 для книги book
        test_less_1_rating = 0
        # устанавливаем рейтинг test_less_1_rating для книги book
        collector.set_book_rating(book, test_less_1_rating)
        # проверяем, что рейтинг test_less_1_rating для book не установился
        assert collector.get_book_rating(book) != test_less_1_rating

    # Нельзя выставить рейтинг больше 10
    def test_set_book_rating_not_set_rating_more_10_true(self):
        # создаем объект BooksCollector м пустым словарем books_rating
        collector = BooksCollector()
        # название добавляемой книга
        book = 'Гордость и предубеждение и зомби'
        # добавляем новую книгу book в словарь
        collector.add_new_book(book)
        # значение рейтинга = 11 для книги book
        test_more_10_rating = 11
        # устанавливаем рейтинг test_less_1_rating для книги book
        collector.set_book_rating(book, test_more_10_rating)
        # проверяем, что рейтинг test_less_1_rating для book не установился
        assert collector.get_book_rating(book) != test_more_10_rating

    # проверяем что нельзя присвоить рейтинг книге которой нет в словаре
    def test_get_book_rating_book_not_in_dict_none(self):
        # создаем объект BooksCollector м пустым словарем books_rating
        collector = BooksCollector()
        # название добавляемой книга
        test_book = 'Гордость и предубеждение и зомби'
        # проверяем, если книги нет в словаре, то метод get_book_rating вернет отсутствующее значение
        assert collector.get_book_rating(test_book) is None

    # Добавление книги в избранное.
    def test_add_book_in_favorites_add_book_from_book_ratings_true(self):
        # создаем объект BooksCollector м пустым словарем books_rating
        collector = BooksCollector()
        # название добавляемой книга
        book = 'Гордость и предубеждение и зомби'
        # добавляем новую книгу book в словарь
        collector.add_new_book(book)
        # добавляем новую книгу в список избранного favorites
        collector.add_book_in_favorites(book)
        # проеряем вхождение книги book в словарь favorites
        assert book in collector.get_list_of_favorites_books()

    # Нельзя добавить книгу в избранное, если её нет в словаре books_rating.
    def test_add_book_in_favorites_added_book_not_in_book_ratings_true(self):
        # создаем объект BooksCollector м пустым словарем books_rating
        collector = BooksCollector()
        # название книги, которую будем искать в списке favorites
        test_book_not_in_book_rating = 'Гордость и предубеждение и зомби'
        # добавляем test_book_not_in_book_rating в список favorites
        collector.add_book_in_favorites(test_book_not_in_book_rating)
        # проверям, что добавленная книга test_book_not_in_book_rating отсутствует в списке favorites
        assert test_book_not_in_book_rating not in collector.get_list_of_favorites_books()

    # Проверка удаления книги из избранного.
    def test_delete_delete_book_from_favorites_deleted_book_not_in_favorites_false(self):
        # создаем объект BooksCollector м пустым словарем books_rating
        collector = BooksCollector()
        # название добавляемой книга
        book = 'Гордость и предубеждение и зомби'
        # обавляем новую книгу book в словарь
        collector.add_new_book(book)
        # добавляем book в список favorites
        collector.add_book_in_favorites(book)
        # удаляем книгу book из списка favorites
        collector.delete_book_from_favorites(book)
        # проверяем, что книга book отсутсвует в списке favorites
        assert book not in collector.get_list_of_favorites_books()
