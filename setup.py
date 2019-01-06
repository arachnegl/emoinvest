#!/usr/bin/env python
from setuptools import setup, find_packages


if __name__ == '__main__':
    setup(
        name='emoinvest',
        use_scm_version=True,
        description='''''',
        long_description='''''',
        author="Michael Schaidnagel",
        author_email="msmucah@googlemail.com",
        license='',
        url='https://github.com/CodeMonkeysGottaCode/emoinvest',
        scripts=[],
        package_dir={'': 'src'},
        packages=find_packages('src'),
        py_modules=[],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points={
            'console_scripts': [
            ],
        },
        include_package_data=True,
        extras_require={
            'develop': [
                'pytest==3.3.1',
                'pytest-env==0.6.2',
                'pytest-pythonpath==0.7.1',
                'pytest-cov==2.5.1',
                'pytest-flake8==0.9.1',
            ]
        },
        setup_requires=[
            'setuptools_scm'
        ],
        install_requires=[
            'pymssql',
            'pymongo',
            'pymysql',
            'SQLAlchemy',
            'pandas',
            'jupyter',
            'scikit-learn',
            'scipy',
            'slackclient',
            # 'airflow',
            'alpha_vantage',
            'matplotlib',
            'boto3',
            'mpl_finance',
            'pandas_datareader'
        ],
        dependency_links=[],
        zip_safe=True
    )
