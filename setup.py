from setuptools import setup, find_packages

setup(
    name = 'mol-coma',
    version = '0.1.5',
    description = 'Choi, J., Seo, S. & Park, S. COMA: efficient structure-constrained molecular generation using contractive and margin losses. J Cheminform 15, 8 (2023). https://doi.org/10.1186/s13321-023-00679-y',
    author = 'Jonghwan Choi',
    author_email = 'mathcombio@yonsei.ac.kr',
    url = 'https://github.com/mathcom/mol-coma',
    install_requires = [
        'numpy==1.19.5',
        'scikit-learn==0.20.0',
        'rdkit==2022.3.3',
        'torch==1.10.1',
        'jupyter>=1.0.0',
        'scipy>=1.5.3',
        'networkx>=2.3',
        'pandas>=1.1.5',
        'tqdm>=4.64.0',
        'requests>=2.28.0',
        'matplotlib>=3.3.4',
        'seaborn>=0.11.2',
    ],
    packages = find_packages(exclude = []),
    keywords = ['coma', 'mol-coma'],
    python_requires = '==3.7.*',
    package_data = {
        '': ['*.pkl.gz', '*.pkl']
    },
    zip_safe = False,
    classifiers = [
        'Programming Language :: Python :: 3.7',
    ],
)
