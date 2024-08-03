from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_slug }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    description="{{ cookiecutter.project_short_description }}",
    packages=find_packages(),
    install_requires=[
        # Adicione os requisitos do seu projeto aqui
    ],
)
