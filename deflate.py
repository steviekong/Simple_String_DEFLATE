import sys

#main function which prints the output string
def main():
	filename = sys.argv[1]
	byte_array = read_file(filename)
	block_list = read_blocks_into_array(byte_array)
	file_string = deflate(block_list)
	print(file_string)

#Reads file from disk
def read_file(filename):
	file = open(filename, 'r')
	byte_array = file.read()
	return byte_array

#Horrible function that splits the input into an array of tuples I can work with. 
#I used regex first but it wouldn't help with the one with several whitespace characters.
#I need to get better at regex. 
def read_blocks_into_array(byte_array):
	block_list = byte_array.split('> ')
	fixed_list = []
	for i in block_list:
		fixed_list.append(i[1:len(i)])
	fixed_list[len(fixed_list) - 1] = fixed_list[len(fixed_list) - 1][0:len(fixed_list[len(fixed_list) - 1])-1]
	new_list = []
	for i in fixed_list:
		 split = i.split(', ')
		 i = ()
		 for j in split:
		 	i = i + (j,)
		 new_list.append(i)
	return new_list

#Simple function that deflates the given array of blocks.
def deflate(block_list):
	output = ""
	for i in block_list:
		if i[0] == "1":
			location = len(output) - int(i[1]) 
			substring = output[location:location+int(i[2])]
			output += substring
		else:
			output += i[1]
	return output

if __name__ == '__main__':
	main()