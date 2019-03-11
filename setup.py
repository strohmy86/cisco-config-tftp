#!/usr/bin/env/python3

import setuptools

setuptools.setup(name='cisco-config-tftp',
	version='1.0',
	description='Tool to download and upload running-config from/to a cisco switch using the snmp protocol.',
	url='https://github.com/Strohmy86/cisco-config-tftp',
	author='Luke Strohm',
	author_email='strohm.luke@gmail.com',
	license='MIT',
	packages=setuptools.find_packages(),
	classifiers=['Programming Language :: Python :: 3',
				'License :: OSI Approved :: MIT License',
				'Operating System :: Linux or MacOS',
				],
	)
