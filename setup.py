
  
from setuptools import setup 
from projet_billard  import __version__ as current_version 

setup(
    name='projet_billard',
    version='current_version',
    description='Square case, Flat Torus case and Elliptic case (game)',
    url='https://github.com/amahjourwalid/projet_billard',
    author='Aamahjour Walid, Amghar Cherif, Charoy Leo',
    author_mail='amahjour.walid@etu.umontpellier.fr, amghar.mohamed@etu.umontpellier.fr, charoy-gerard.leo@etu.umontpellier.fr',
    license='MIT',
    packages=['projet_billard','projet_billard.square_case','projet_billard.flat_torus','projet_billard.elliptic_case'],
    zip_safe=False
)
