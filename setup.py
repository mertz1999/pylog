from setuptools import setup, find_packages

setup(
    name='pylog',
    version='1.0.0',
    packages=find_packages(),
    description='A python package for make logging easily',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Reza Tanakizadeh',
    author_email='reza.tz780210@gmail.com',
    url='https://github.com/mertz1999/pylog',
    license='MIT',
    install_requires=[
        'colorama',
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)