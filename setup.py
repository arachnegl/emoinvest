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
            'setuptools-scm==1.15.6',
            'pymssql==2.1.3',
            'pymongo==3.3.1',
            'pymysql==0.7.9',
            'SQLAlchemy==1.1.18',
            'pandas==0.20.3',
            'jupyter==1.0.0',
            'scikit-learn==0.19.0',
            'scipy==0.19.0',
            'slackclient==1.3.0',
            'airflow',
            'alpha_vantage',
            'matplotlib',
            'boto3',
        ],
        dependency_links=[],
        zip_safe=True
    )
