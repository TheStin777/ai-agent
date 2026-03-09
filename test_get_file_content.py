from functions.get_file_content import get_file_content

#Test 1: lorem.txt
print("Result for the  'lorem.txt file:")
print(f"{get_file_content("calculator", "lorem.txt")}")

#Test 2: main.py
print("Result for the  'main.py' file:")
print(f"{get_file_content("calculator", "main.py")}")

#Test 3: pkg/calculator.py
print("Result for the 'calculator.py' file:")
print(f"{get_file_content("calculator", "pkg/calculator.py")}")

#Test 4: /bin/cat
print("Result for the 'cat' file:")
print(f"{get_file_content("calculator", "/bin/cat")}")


#Test 5: pkg/does_not_exist.py"
print("Result for the'does_not_exist.py' file:")
print(f"{get_file_content("calculator", "pkg/does_not_exist.py")}")