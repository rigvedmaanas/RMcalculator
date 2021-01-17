from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(name='RMcalculator', version='0.0.1', description='A calculator with Graphical User Interface', long_description=open('README.md').read(), url='https://github.com/rigvedmaanas/RMcalculator/',   author='Rigved Maanas M', author_email='rigvedmaanas@gmail.com', license='MIT',  classifiers=classifiers, keywords='calculator', packages = find_packages(), install_requires=[''])

