from abc import ABCMeta

from .libs.base import Base
from .libs import fs
from .libs.db import Manga


class Provider(Base, metaclass=ABCMeta):
    _db = None

    def __init__(self):
        super().__init__()
        self._db = Manga()

    def run(self, args: dict):
        super()._args = args

    def loop_chapters(self):
        for chapter in self.chapters:
            self.chapter = chapter

    def loop_files(self):
        path_location = fs.get_temp_path()
        for idx, url in enumerate(self.files):
            try:
                filename = fs.remove_query(fs.basename(url))
                filename = fs.path_join(path_location, filename)
                self.download(url, filename, idx)
            except AttributeError:
                pass

    def _update_db(self):
        db = self._db.select().where(Manga.url == self.domain)
        pass
