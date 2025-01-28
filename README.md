# qa_python

Список тестов:
1. test_add_new_book_add_two_books - был исправлен тестовый пример, т.к. нет словаря books_rating и метода get_books_rating
2. test_add_new_book_add_books_different_symbols - проверка добавления книг с названиями из разных символов (латиница, кириллица, цифры, пробелы)
3. test_add_new_book_name_more_than_40_symbols - проверка добавления книги с названием длиной больше 40 символов (не добавляется)
4. test_set_book_genre_set_genre_in_list - проверка добавления жанра для одной книги (жанр есть в списке доступных жанров)
5. test_set_book_genre_set_genre_not_in_list - проверка добавления жанра для одной книги (жанра нет в списке доступных жанров)
6. test_get_book_genre_get_genre - проверка получения жанра одной книги
7. test_get_books_with_specific_genre_get_books - проверка получения всех книг одного жанра
8. test_get_books_for_children_get_books - проверка получения детских книг
9. test_add_book_in_favorites_add_book - проверка добавления книги в избранное
10. test_delete_book_in_favorites_delete_book - проверка удаления книги из избранного