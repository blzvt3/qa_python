import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name', ['Война и мир', '123#!', '     ', 'Brave New World', 'Джонни+Silverhand=2077'])
    def test_add_new_book_add_books_different_symbols(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.get_books_genre() == {name: ''}

    def test_add_new_book_name_more_than_40_symbols(self):
        collector = BooksCollector()
        collector.add_new_book('Мечтают ли андроиды об электроовцах часть вторая')
        assert collector.get_books_genre() == {}

    def test_set_book_genre_set_genre_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_genre() == {'Дюна': 'Фантастика'}

    def test_set_book_genre_set_genre_not_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Басня')
        assert collector.get_books_genre() == {'Дюна': ''}

    def test_get_book_genre_get_genre(self):
        collector = BooksCollector()
        collector.books_genre = {'Мы': 'Фантастика'}
        assert collector.get_book_genre('Мы') == 'Фантастика'

    def test_get_books_with_specific_genre_get_books(self):
        collector = BooksCollector()
        collector.books_genre = {'Дюна': 'Фантастика', 'Оно': 'Ужасы', 'Русалочка': 'Мультфильмы', 'Звонок': 'Ужасы'}
        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно', 'Звонок']

    def test_get_books_for_children_get_books(self):
        collector = BooksCollector()
        collector.books_genre = {'Дюна': 'Фантастика', 'Оно': 'Ужасы', 'Русалочка': 'Мультфильмы', 'Шерлок': 'Детективы', 'Трое в лодке': 'Комедии'}
        assert collector.get_books_for_children() == ['Дюна', 'Русалочка', 'Трое в лодке']

    def test_add_book_in_favorites_add_book(self):
        collector = BooksCollector()
        collector.books_genre = {'Дюна': 'Фантастика', 'Оно': 'Ужасы', 'Русалочка': 'Мультфильмы'}
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_delete_book_in_favorites_delete_book(self):
        collector = BooksCollector()
        collector.books_genre = {'Дюна': 'Фантастика', 'Оно': 'Ужасы'}
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == ['Оно']