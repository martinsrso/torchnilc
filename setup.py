from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='deeptagger',
    version='0.0.1',
    description='Part-of-speech tagger based on Deep Learning',
    long_description=readme,
    author='Marcos Treviso',
    author_email='marcostreviso@usp.br',
    url='https://github.com/mtreviso/deeptagger',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    data_files=['LICENSE'],
    zip_safe=False,
    keywords='evaluator',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
