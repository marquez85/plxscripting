from setuptools import find_packages
from setuptools import setup

setup(
   name='plxscripting',
   version='1.0',
   description='essencial py files to run to connect plaxis',
   author='PLAXIS_FM',
   author_email='fpvsm85@gmail.com',
   url="https://github.com/marquez85/plxscripting/tree/main/plxscripting/",
   packages=find_packages(),
   entry_points={
       'console_script':[
           'plxscripting=plxscripting.main:main',
           ],
       },
)