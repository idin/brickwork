from .get_full_path import get_full_path
from ._dbutils import dbutils_ls


def ls(path):
	path = get_full_path(path)
	return [f.path for f in dbutils_ls(path)]
