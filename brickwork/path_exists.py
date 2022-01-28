from ._dbutils import dbutils_ls


def path_exists(path):
	try:
		dbutils_ls(path)
		return True
	except Exception as e:
		if 'java.io.FileNotFoundException' in str(e):
			return False
		else:
			raise e
