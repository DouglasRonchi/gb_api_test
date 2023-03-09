"""
Pagination util module
"""
from math import ceil


class Pagination:
    """A Pagination class to be used to help on displaying pagination"""

    def __init__(self, total=None, per_page=1000, current_page=1):
        self.total = total
        self.per_page = per_page
        self.current_page = current_page

    def __repr__(self):
        return str(self.__dict__)

    @property
    def total_pages(self):
        """The number of total pages"""
        return int(ceil(float(self.total) / self.per_page))

    @property
    def pages(self):
        """Returns list of integers of pages e.g. for 3 pages [1,2,3]"""
        return range(1, self.total_pages + 1)

    @property
    def next_page(self):
        """The page number after the current_page or None"""
        return self._get_page_offset(+1)

    @property
    def prev_page(self):
        """The page number before the current_page or None"""
        return self._get_page_offset(-1)

    def _get_page_offset(self, offset):
        """Give an offset, +1 or -1 and the page number around the current_page will be returned
        So if we are on current_page 2 and pass +1 we get 3, if we pass -1 we get 1.  Or None if not valid
        """
        try:
            return self.pages[self.pages.index(self.current_page + offset)]
        except ValueError:
            return None

    @property
    def start(self):
        """The starting offset used when querying"""
        return self.current_page * self.per_page - self.per_page

    @property
    def end(self):
        """The starting offset used when querying"""
        return self.start + self.per_page
