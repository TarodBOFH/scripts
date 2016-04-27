#!/usr/bin/python
#### Series Renamer
#    Rename Series files based on the args supplied
#    

import glob, os, re, sys, argparse, textwrap,shutil

def main(argv):
	src_dir = ''
	sample_fileName = ''
	series_name = ''
	replace_dots = False
	delete_double_spaces = True
	title = False
	season = None

	parser = argparse.ArgumentParser(
		formatter_class=argparse.RawDescriptionHelpFormatter,
		description=textwrap.dedent('''\
			Rename files in a folder to appropiate plex name according plex naming
			conventions. If a series name is supplied, will be used as prefix to the season
			and episode information. If not, %(prog)s will try to guess it from a sample 
			file.

			If such sample filename does not exist, %(prog)s will try to guess it from the 
			files in src_dir using the following rules:

			  If any file doesn\'t follow nxnn nor snnenn formats, will exit
			  If any file has snnenn format, will precede over nxnn formats
			  If all files from a chosen format share the same root (after dots and camel 
			  case processing), then the part before the format will be used.

			Example:

			  Hello World 1x01 foobar
	
			will produce Hello World

			  Hello World 1x01 foobar
			  Helloworld s01e01 foobar

			will produce Helloworld

			  Hello World 1x01 foobar
			  Helloworld 1x01 foobar

			will give an error.'''),
		epilog=textwrap.dedent('''\
			See plex naming convention at 
			https://support.plex.tv/hc/en-us/articles/200220687''')
	)

	parser.add_argument("src_dir", help="Directory where the files are stored")
        parser.add_argument("pattern", help="Pattern to extract episode number for regex substitution",default=None);
	parser.add_argument("series_name",help="Name of the series (to rename if needed)",default=None)
	parser.add_argument("-d","--replace-dots",help="Replaces dots on name with spaces",action='store_true')
	parser.add_argument("-k","--keep-double-spaces",help="Don't delete double spaces in the file name",action='store_true')
	parser.add_argument("-t","--title",help="Capitalize each letter of series name title",action='store_true')
	parser.add_argument("-s","--season",help="Force a season number instead of guessing it")

	args = parser.parse_args()

	if args.src_dir:
		src_dir = args.src_dir
	
	if args.series_name:
		series_name = args.series_name
	
	if args.pattern:
		pattern = args.pattern

	if args.replace_dots:
		replace_dots = True

	if args.keep_double_spaces:
		delete_double_spaces = False
	
	if args.title:
		title = True
	if args.season:
		season = args.season
		
	if not src_dir:
		src_dir = os.getcwd()
		print "No habia src_dir"
		exit(1)

	files = [os.path.join(src_dir,f) for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir,f))]

	if replace_dots:
		for file in files:
			(fileName,ext) = os.path.splitext(os.path.basename(file))
			newName=re.sub(r"\.+"," ",fileName)
			newFile = newName+ext if ext else newName
			os.rename(file,os.path.join(src_dir,newFile))
#			shutil.move(file,os.path.join(src_dir,newFile))
	        files = [os.path.join(src_dir,f) for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir,f))]

	if delete_double_spaces:
	        for file in files:
			(fileName,ext) = os.path.splitext(os.path.basename(file))
			if re.match("\s\s+",fileName):
				newName = re.sub("\s\s+", " ", fileName)
				newFile = newName+ext if ext else newName
				os.rename(file,os.path.join(src_dir,newFile))
#				shutil.move(file,os.path.join(src_dir,newFile))

        	files = [os.path.join(src_dir,f) for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir,f))]
	
	if title:
		for file in files:
	                (fileName,ext) = os.path.splitext(os.path.basename(file))
	                newName = fileName.title()+ext if ext else fileName.title()
	                os.rename(file,os.path.join(src_dir,newName))
			#shutil.move(file,os.path.join(src_dir,newName))
	        files = [os.path.join(src_dir,f) for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir,f))]

	

	#pattern_x = '\s*-*\s*(\d+)[xX](\d+)\s*-*\s*' 
        #pattern_s = '\s*-*\s*[sS](\d+)[eE](\d+)\s*-*\s*'
	#pattern = re.escape(pattern)
        files = [os.path.join(src_dir,f) for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir,f))]
	namePart = series_name+" - s"+season+r"e\1 - \2" if season else series_name+r" - s\1e\2 - \3"
	for file in files:
		(fileName,ext) = os.path.splitext(os.path.basename(file))
		newFileName = re.sub(pattern+"(.*)",namePart, fileName)
		newFile = newFileName+ext if ext else newFileName
		if not fileName == newFileName:
	                #print "Renaming {0} into {1}".format(file,newFile)
			os.rename(file,os.path.join(src_dir,newFile))
			#shutil.move(file,os.path.join(src_dir,newFile))

if __name__ == "__main__":
    main(sys.argv[1:])
