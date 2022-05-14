from setuptools import setup, find_packages

def readme():
    with open('./README.md') as f:
        return f.read()


setup(
    name='brickwork',
    version='2022.5.1',
    license='MIT',

    author='Idin',
    author_email='py@idin.ca',
    url='https://github.com/idin/brickwork',

    keywords='databricks filesystem files DBFS',
    description='Python library to simplify how we store files on DBFS',
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

    packages=find_packages(exclude=("jupyter_tests", ".idea", ".git")),
    install_requires=['IPython', 'pyspark'],
    python_requires='~=3.6',
    zip_safe=True
)

# this is for building the wheel:
# rm dist/*;python -m build;rm dist/*.tar.gz;rm -r build