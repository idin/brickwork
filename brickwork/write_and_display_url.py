from pyspark.sql import DataFrame
from IPython.core.display import HTML
import os
from .get_full_path import get_full_path, get_short_path
from .get_notebook_information import get_notebook_information
from .display_url import display_url


def write_and_display_url(data, path, coalesce=None, format='csv', file_store_dir='FileStore'):
	"""
	:type data: DataFrame
	:type path: str
	:type coalesce: NoneType or int
	:type format: str
	:rtype: NoneType or list[HTML]
	"""
	full_path = get_full_path(path)
	short_path = get_short_path(path)
	databricks_instance = get_notebook_information()['browserHostName']

	if coalesce is None:
		data.write.format(format).save(full_path)
	else:
		data.coalesce(coalesce).write.format(format).save(full_path)

	files = os.listdir(f'/dbfs/{file_store_dir}/{short_path}')

	file_parts = [x for x in files if x.startswith('part') and x.endswith(format)]

	urls_and_texts = {
		f'https://{databricks_instance}/files/{path}/{file}': f'https://{databricks_instance}/files/{path}'
		for file in file_parts
	}

	results = []
	for url, text in urls_and_texts.items():
		result = display_url(url=url, text=text)
		if result is not None:
			results.append(result)

	if len(results) > 0:
		return results
	else:
		return None
