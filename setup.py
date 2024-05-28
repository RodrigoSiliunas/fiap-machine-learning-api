from setuptools import setup, find_packages

"""
==========================================================================
 ➠ Backend of Twitter
 ➠ Section By: Rodrigo Siliunas
==========================================================================
"""

# Informações sobre nosso pacote de API.
setup(
    name='API - Embrappa - ML',
    author='Rodrigo Siliunas',
    author_email='rodrigo.siliunas@gmail.com',
    description='Essa API foi desenvolvida com o intuito de ser utilizada para o desenvolvimento de modelos de Machine Learning',
    version='1.0.0',
    packages=find_packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
    include_package_data=True
)
