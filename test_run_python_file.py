from functions.run_python_file import run_python_file

#Test 1: main.py
print("Result for the  'main.py':")
print(f'{run_python_file("calculator", "main.py")}')

#Test 2: main.py ["3 + 5"]
print('Result for the "main.py ["3 + 5"]" file:')
print(f'{run_python_file("calculator", "main.py", ["3 + 5"])}')

#Test 3: tests.py
print("Result for the 'tests.py' file:")
print(f'{run_python_file("calculator", "tests.py")}')

#Test 4: ../main.py
print("Result for the '../main.py' file:")
print(f'{run_python_file("calculator", "../main.py")}')


#Test 5: nonexistent.py
print("Result for the 'nonexistent.py' file:")
print(f'{run_python_file("calculator", "nonexistent.py")}')


#Test 6: lorem.txt
print("Result for the 'lorem.txt' file:")
print(f'{run_python_file("calculator", "lorem.txt")}')


