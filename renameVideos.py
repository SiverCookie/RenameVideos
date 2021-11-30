# Python3 code to rename multiple files in a directory or folder
# command example python renameVideos.py textToBeCut textToBeCutFormat whereToCut
#                 textToBeCut      : the portion of text needed to be cut or the number of characters needed to be cut
#                 textToBeCutFormat: t - text, n - number of characters to be cut
#                 whereToCut       : b - beggining, e - end
# Delete 4 characters from thew end      :  python renameVideos.py 4 n e 
# Delete 4 characters from thew beggining:  python renameVideos.py 4 n b 
# Delete a chunk of text from the file   :  python renameVideos.py theChunk t 

import os
import sys

def getVideoFormat(filename):
	idx = -1
	format = ''
	curr_ch = ''
	while (curr_ch!='.'):
		format = format+curr_ch
		curr_ch = filename[idx]
		idx = idx-1
	format = format + '.'
	format = format[::-1]
	#print(format)
	return format
	

# Function to rename multiple files
def cutVideos(filename,textToBeCut,textToBeCutFormat, whereToCut):
	dst = ''
	if filename == 'renameVideos.py':
		pass
	else:
		if textToBeCutFormat == 't':
			dst = filename.replace(textToBeCut, '') #if textToBeCut not in the original name nothing is done
		else: #if textToBeCutFormat == n 
			if whereToCut == 'b':
				dst = filename[int(textToBeCut):]
			else:#whereToCut == 'e':
				videoFormat = getVideoFormat(filename) #4 is used because most formats have 3 letters and a '.'
				print("The format is " + videoFormat)
				dst = filename[:-(int(textToBeCut) + len(videoFormat))]+videoFormat
				
		# rename() function will
		# rename all the files
		print('Old name = ',filename,'\nNew name = ', dst, '\n')
		os.rename(filename, dst)
	

def main():
	print("Hello")
	if len(sys.argv) != 4 and len(sys.argv) != 3:
		print("Incorrect number of arguments (needed 3 or 4)")
		print("Python3 code to rename multiple files in a directory or folder \ncommand example python renameVideos.py textToBeCut textToBeCutFormat whereToCut\n\t\t\t\ttextToBeCut      : the portion of text needed to be cut or the number of characters needed to be cut\n\t\t\t\ttextToBeCutFormat: t - text, n - number of characters to be cut\n\t\t\t\twhereToCut       : b - beggining, e - end\nDelete 4 characters from thew end      :  python renameVideos.py 4 n e \nDelete 4 characters from thew beggining:  python renameVideos.py 4 n b\nDelete a chunk of text from the file   :  python renameVideos.py theChunk t")
	else:
		print("Script start")
		textToBeCut = sys.argv[1] 
		textToBeCutFormat = sys.argv[2]
		whereToCut = ''
		if len(sys.argv) == 4:
			whereToCut = sys.argv[3] 
		for filename in os.listdir(r'C:\Users\N\Desktop\VideoDownloads'):
			cutVideos(filename,textToBeCut,textToBeCutFormat, whereToCut)
			
# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()
