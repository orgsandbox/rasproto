#!/usr/bin/python

import os

def main():
	fileList = open('meta' , 'r')
	newFileList = []
	for i in fileList:
		newFile = i[:-4] + '_r' + '.png'
		print newFile
		os.system('convert -flip -transverse ' + i + ' ' + newFile)
		newFileList.append( newFile )
	fileList = open('pimetaslides', 'w')
	for i in newFileList:
		fileList.write(i + '\n')
	fileList.close()
		

if __name__ == '__main__':
	main()
