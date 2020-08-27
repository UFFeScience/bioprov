__author__ = "Vini Salazar"
__license__ = "MIT"
__maintainer__ = "Vini Salazar"
__url__ = "https://github.com/vinisalazar/bioprov"
__version__ = "0.1.0"


"""
Contains the File class and related functions.
"""
from pathlib import Path
from bioprov.utils import get_size
from prov.model import ProvEntity


class File(ProvEntity):
    """
    Class for holding file and file information.
    """

    def __init__(self, path, bundle=None, tag=None, generated_by=None):
        """
        :param path: A UNIX-like file path.
        :param tag: optional tag describing the file.
        :param generated_by: An instance of the Run class which generated the command.
        """
        self.path = Path(path).absolute()
        self.name = self.path.name
        super().__init__(bundle, identifier="files:{}".format(self.name))
        self.directory = self.path.parent
        self.extension = self.path.suffix
        if tag is None:
            tag = self.name
        self.tag = tag
        self.exists = self.path.exists()
        self.size = get_size(self.path)
        self.raw_size = get_size(self.path, convert=False)
        self.generated_by = generated_by

        # Provenance attributes
        self._document = None
        self._entity = ProvEntity(self._document, self.path.name)

    def __repr__(self):
        return str(self.path)

    def __str__(self):
        return self.__repr__()

    @property
    def document(self):
        return self._document

    @document.setter
    def document(self, document):
        self._document = document

    @property
    def entity(self):
        return self._entity

    @entity.setter
    def entity(self, document):
        self._document = document
        self._entity = ProvEntity(self._document, self.path.name)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def exists(self):
        return self.path.exists()

    @exists.setter
    def exists(self, _):
        self._exists = self.path.exists()

    pass
