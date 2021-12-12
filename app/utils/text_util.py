from slugify import slugify


class TextUtil:
    @staticmethod
    def slugify_text(string):
        return slugify(string)
