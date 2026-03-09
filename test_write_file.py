from functions.write_file import write_file

#Test 1: lorem.txt
print("Result for the  'lorem.txt':")
print(f'{write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")}')

#Test 2: pkg/morelorem.txt
print("Result for the  'pkg/morelorem.txt' file:")
print(f'{write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")}')

#Test 3: pkg/calculator.py
print("Result for the '/tmp/temp.txt' file:")
print(f'{write_file("calculator", "/tmp/temp.txt", "this should not be allowed")}')

