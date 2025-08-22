from functions.get_files_content import get_file_content

def run_tests():
    # Test 1: Get content of lorem.txt (to check truncation)
    print("Result for 'lorem.txt' content:")
    print(get_file_content("calculator", "lorem.txt"))
    
    # Test 2: Get content of main.py
    print("\nResult for 'main.py' content:")
    print(get_file_content("calculator", "main.py"))
    
    # Test 3: Get content of pkg/calculator.py
    print("\nResult for 'pkg/calculator.py' content:")
    print(get_file_content("calculator", "pkg/calculator.py"))
    
    # Test 4: Get content of /bin/cat (outside working directory)
    print("\nResult for '/bin/cat' content:")
    print(get_file_content("calculator", "/bin/cat"))
    
    # Test 5: Get content of non-existent file
    print("\nResult for 'pkg/does_not_exist.py' content:")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    run_tests()