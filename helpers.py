""" modulo helpers  """
from pathlib import Path


def abs_path(file):
    """ Obtiene la ruta absoluta de un archivo """
    return str(Path(__file__).parent.absolute() / file)
