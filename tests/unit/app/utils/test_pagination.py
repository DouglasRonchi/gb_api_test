import unittest

from app.utils.pagination import Pagination


class TestPagination(unittest.TestCase):
    def setUp(self) -> None:
        self.data = ["a", "b", "c", "d", "e"]

    def test_pagination_class_attributes(self):
        pag = Pagination(total=len(self.data), per_page=2, current_page=1)
        self.assertEqual(repr(pag), "{'total': 5, 'per_page': 2, 'current_page': 1}")
        self.assertEqual(pag.total, 5)
        self.assertEqual(pag.total_pages, 3)
        self.assertEqual(pag.next_page, 2)
        self.assertEqual(pag.pages, range(1, 4))
        self.assertEqual(pag.prev_page, None)
        self.assertEqual(self.data[pag.start : pag.end], ["a", "b"])

    def test_pagination_page_one(self):
        pag = Pagination(total=len(self.data), per_page=2, current_page=1)
        self.assertEqual(self.data[pag.start : pag.end], ["a", "b"])

    def test_pagination_page_two(self):
        pag = Pagination(total=len(self.data), per_page=2, current_page=2)
        self.assertEqual(self.data[pag.start : pag.end], ["c", "d"])

    def test_pagination_page_three(self):
        pag = Pagination(total=len(self.data), per_page=2, current_page=3)
        self.assertEqual(self.data[pag.start : pag.end], ["e"])


if __name__ == "__main__":
    unittest.main()
