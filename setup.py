from setuptools import setup, find_packages

setup(
    name="department_app",
    version="1.0.0",
    url="https://github.com/dmitrenko-v/department_app",
    author="Vladislav Dmitrenko",
    install_requires=[
        "Flask==2.0.0",
        "Flask-SQLAlchemy==2.5.1",
        "Flask-WTF==1.0.0"
    ],
    packages=find_packages()
)
