from ._dbutils import dbutils_ls, dbutils_rm
from .get_full_path import get_full_path


def is_file(path):
	full_path = get_full_path(path)
	l = dbutils_ls(full_path)
	if len(l) > 1:
		return False
	else:
		one = l[0]
		if l.isFile() and get_full_path(l.path) == full_path:
			return True
		else:
			return False
