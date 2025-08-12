from math import ceil


class PhotoAlbum:
    PAGE_SIZE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for p in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        album_pages = ceil(photos_count / cls.PAGE_SIZE)
        return cls(album_pages)

    def add_photo(self, label: str):
        for i, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PAGE_SIZE:
                page.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        result = f"{'-' * 11}\n"
        for page in range(self.pages):
            result += ' '.join(["[]" for el in self.photos[page] if el]) + "\n"
            result += f"{'-' * 11}\n"

        return result

