from .get_full_path import get_full_path
from ._dbutils import dbutils_rm


def remove_file(path):
	path = get_full_path(path)
	return dbutils_rm(path)
