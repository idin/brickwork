def remove_prefix(text, prefix):
	if text.startswith(prefix):
		return text[len(prefix):]
	return text


def get_full_path(path, file_store_dir='FileStore'):
	path = path.lstrip('/')
	path = remove_prefix(path, 'dbfs:/')
	path = remove_prefix(path, f'{file_store_dir}/')
	path = f'dbfs:/{file_store_dir}/{path}'
	return path


def get_short_path(path, file_store_dir='FileStore'):
	full_path = get_full_path(path)
	return remove_prefix(full_path, prefix=f'dbfs:/{file_store_dir}/')
