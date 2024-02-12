from main import BooksCollector
import pytest

class TestBooksCollector:


    def test_add_new_book_add_no_name_book(self):
        collector = BooksCollector()
        collector.add_new_book('')

        assert '' not in collector.get_books_genre()


    def test_set_book_genre_set_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Existing Book')
        collector.set_book_genre('Existing Book', 'Ужасы')

        genre = 'Фантастика'
        collector.set_book_genre('Existing Book', genre)

        assert collector.books_genre['Existing Book'] == genre


    def test_get_book_genre_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('The Great Gatsby')
        collector.set_book_genre('The Great Gatsby', 'Детективы')

        genre = collector.get_book_genre('The Great Gatsby')

        assert genre == 'Детективы'


    def test_get_books_with_specific_genre_existing_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.add_new_book('Book2')

        collector.set_book_genre('Book1', 'Фантастика')
        collector.set_book_genre('Book2', 'Детективы')

        genre = 'Фантастика'
        result = collector.get_books_with_specific_genre(genre)

        assert result == ['Book1']


    def test_get_books_genre_three_books(self):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.add_new_book('Book2')
        collector.add_new_book('Book3')

        collector.set_book_genre('Book1', 'Фантастика')
        collector.set_book_genre('Book2', 'Детективы')
        collector.set_book_genre('Book3', 'Ужасы')

        genres = collector.get_books_genre()

        assert genres == {
            'Book1': 'Фантастика',
            'Book2': 'Детективы',
            'Book3': 'Ужасы'
        }


    def test_get_books_for_children_valid_books(self):
        collector = BooksCollector()
        collector.add_new_book('The Lion, the Witch and the Wardrobe')
        collector.add_new_book('Alices Adventures in Wonderland')
        collector.add_new_book('Pet Sematary')

        collector.set_book_genre('The Lion, the Witch and the Wardrobe', 'Фантастика')
        collector.set_book_genre('Alices Adventures in Wonderland', 'Фантастика')
        collector.set_book_genre('Pet Sematary', 'Ужасы')

        result = collector.get_books_for_children()

        assert result == ['The Lion, the Witch and the Wardrobe', "Alices Adventures in Wonderland"]


    def test_add_book_in_favorites_three_books(self):
        collector = BooksCollector()
        book_name = 'Book'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Ужасы')

        collector.add_book_in_favorites(book_name)

        assert book_name in collector.favorites


    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()
        book_name = 'Book'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Ужасы')
        collector.add_book_in_favorites(book_name)

        collector.delete_book_from_favorites(book_name)

        assert book_name not in collector.favorites


    @pytest.mark.parametrize('expected_favorites', [['Book1'], ['Book2'], ['Book3']])
    def test_get_list_of_favorites_books(self, expected_favorites):
        collector = BooksCollector()
        collector.favorites = expected_favorites

        assert collector.get_list_of_favorites_books() == expected_favorites
