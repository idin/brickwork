import json
from ._dbutils import dbutils_ls, dbutils_rm, get_dbutils


def get_notebook_information():
	notebook_info = json.loads(get_dbutils().notebook().getContext().toJson())
	return notebook_info["tags"]










def remove_file(path):
  path = get_full_path(path)
  return dbutils_rm(path)