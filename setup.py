from setuptools import setup, find_packages

setup(
    name='indexer',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit', 
        "pcloud",
        "psutil",
    ],
    entry_points='''
        [console_scripts]
        indexer=finalization.cli:main
    ''',
)
