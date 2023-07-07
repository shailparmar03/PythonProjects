# with open("a_file.txt") as file:
#     file.read()

# try:
#     file = open("a_file.txt")
#     a_dictionary={"Key":"Value"}
#     print(a_dictionary["shail"])
# except FileNotFoundError:
#     # print("There is an error")
#     file = open("a_file.txt","w")
#     file.write("Something.")
# except KeyError as error_message:  #getting hold of error message
#     print(f"Key {error_message} not found.")
# else: # only executed if the try block succeeds
#     content=file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")

