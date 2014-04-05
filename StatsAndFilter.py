#! /usr/bin/python
__author__ = "Xuan Zhou"
__version__="1.0"
__email__= "reformasky01@gmail.com"

import sys

sourceFile  = "./test.csv"
numOfGenes  = 100
numOfLevels = 5


def getParameters():
	global sourceFile, numOfGenes, numOfLevels
	parameters = {}
	if ( len(sys.argv) > 1):
		for i in range(len(sys.argv)  -1 ):
			key, value = sys.argv[i + 1].split('=')
			parameters[key.lower()] = value
		try:
			sourceFile = parameters['file']
			numOfGenes = int(parameters['numOfGenes'.lower()])
			numOfLevels = int(parameters['numOfLevels'.lower()])
		except Exception, err:
			sys.stderr.write("Error: %s\n"%str(err))








if __name__ == '__main__':
	getParameters()
	print sourceFile, numOfGenes,numOfLevels


