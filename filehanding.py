# with open('a.txt','r') as file:
#     content=file.read()
# print("Entire file content: ")
# print(content)
file = 'a.txt'
# print(f"First {3} lines of the file:")
# with open('a.txt','r') as file:
#     for i in range(3):
#         line=file.readline().strip()
#         print(line)

# text_append = "Aditya balraj"
# with open('a.txt','r') as file:
#     file.write(text_append)
# with open('a.txt','r') as file:
#      updated_content=file.read()
# print("Updated Content:")
# print(updated_content)
# line_list=[]
# with open('a.txt','r') as file:
#     for line in file:
#         line_list.append(line.strip())
# print("file ;lines stored in a list:")
# print(line_list)
with open('a.txt','r') as file:
    content=file.read()
words=content.split()
largest_word=max(words, key=len)
print("The largest word in the file is:",largest_word)
print("lenght of the word: ",len(largest_word))

