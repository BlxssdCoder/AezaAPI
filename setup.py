from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r', encoding="utf8") as f:
        return f.read()


setup(
    name='AezaAPI',
    version='1.0.2',
    author='blxssd',
    description='AezaAPI module',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/BlxssdCoder/AezaAPI',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='aeza python',
    python_requires='>=3.7'
)
