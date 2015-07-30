# Eventsim setup
# Last updated (TSK, 2015-07-27)

from sys import version
if version < '2.2.3':
	from distutils.dist import DistributionMetadata
	DistributionMetadata.classifiers = None
	DistributionMetadata.download_url = None
	
#from setuptools import setup
from distutils.core import setup

setup(
	name='eventsim',
	version='0.6',
	description='Contains various useful tools in simulating discrete system events based on outcome and probabilities',
	long_description = open('README').read(),
	author='Taiwo Kareem',
	author_email='taiwo.kareem36@gmail.com',
	url='http://bitbucket.org/tushortz/eventsim',
	packages=['eventsim','eventsim/example'],
	package_data={
		'eventsim/examples':['*.py', 'eventsim/example/*.py'],
		#'eventsim/help': ['*.txt', 'eventsim/help/*.txt']
		},
	platforms='any',
	keywords='Discrete event simulation tools',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Intended Audience :: Education', 
		'Intended Audience :: Financial and Insurance Industry',
		'Intended Audience :: Information Technology',
		'Intended Audience :: Other Audience',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 3',
	],
)

