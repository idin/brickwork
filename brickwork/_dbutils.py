from pyspark.sql.session import SparkSession


def get_dbutils():
	spark = SparkSession.builder.getOrCreate()
	try:
		from pyspark.dbutils import DBUtils
		dbutils = DBUtils(spark)
	except ImportError:
		import IPython
		dbutils = IPython.get_ipython().user_ns["dbutils"]

	return dbutils

dbutils = get_dbutils()


def dbutils_ls(path):
	return dbutils.fs.ls(path)


def dbutils_rm(path):
	return dbutils.fs.rm(path)


def get_dbutils():
	return dbutils.notebook.entry_point.getDbutils()
