from setuptools import setup, find_packages

"""
==========================================================================
 ➠ Backend of Twitter
 ➠ Section By: Rodrigo Siliunas
==========================================================================
"""

# Informações sobre nosso pacote de API.
setup(
    name='API Embrapa ML',
    author='Rodrigo Siliunas',
    author_email='rodrigo.siliunas12@outlook.com',
    description='Essa API foi desenvolvida com o intuito de ser utilizada para o desenvolvimento de modelos de Machine Learning',
    version='1.0.0',
    packages=find_packages(),
    python_requires='>=3.12',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
