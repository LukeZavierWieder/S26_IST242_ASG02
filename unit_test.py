'''
Testing for personal library.
'''

import unittest
import personal_library
from unittest.mock import patch
from io import StringIO

from personal_library import (
    add_book,
    remove_book,
    update_book,
    list_books,
    search_book,
)

# Test class
class TestPersonalLibrary(unittest.TestCase):
    # Test case for add book function
    def test_add_book_normal_case(self):
        library = []
        with patch("builtins.input", return_value = ["test", "test2", "test3"]):
            add_book()
        self.assertEqual(personal_library.library,
            [{
                "title": "test",
                "author": "test2",
                "year_published": "test3"
            }]
        )


if __name__ == "__main__":
    unittest.main()