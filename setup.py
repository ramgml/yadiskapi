from setuptools import setup, find_packages

with open('README.md', mode='r') as readme:
    README = readme.read()

setup(
    name='yadiskapi',
    version='0.1',
    license='GNU LGPLv3',
    description='Пакет упрощает обращение к REST API Яндекс Диска.',
    long_description=README,
    url='https://github.com/kovalevvjatcheslav/yadiskapi',
    author='Ковалев Вячеслав',
    author_email='kovalevvjatcheslav@gmail.com',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU LGPLv3",
        "Operating System :: OS Independent",
    ],
)
