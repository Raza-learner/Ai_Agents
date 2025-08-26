from functions.run_python import run_python_file

def run_tests():
    # Test 1: Run main.py without arguments
    print("Result for running 'main.py':")
    print(run_python_file("calculator", "main.py"))
    
    # Test 2: Run main.py with arguments ["3 + 5"]
    print("\nResult for running 'main.py' with args ['3 + 5']:")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    
    # Test 3: Run tests.py
    print("\nResult for running 'tests.py':")
    print(run_python_file("calculator", "tests.py"))
    
    # Test 4: Run ../main.py (outside working directory)
    print("\nResult for running '../main.py':")
    print(run_python_file("calculator", "../main.py"))
    
    # Test 5: Run nonexistent.py
    print("\nResult for running 'nonexistent.py':")
    print(run_python_file("calculator", "nonexistent.py"))

if __name__ == "__main__":
    run_tests()