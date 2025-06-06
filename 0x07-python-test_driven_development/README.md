# <ins> Test Driven Development</ins>

## Introduction

Test driven development or TDD is a way of coming up with solutions to problems in python by first testing then writing the code and taking care of the errors and fails from the testing.

There is interactive testing and OOP testing. In the former, the module `doctest1 is used to access submodules that help test the code for errors and breakage. It does this by scanning the python file and finding the symbol `>>>` and executing the code as if in interactive mode.

In the OOP approach, `unittests` are used to test for code. The different ways are used by different proogrammers. For instance, the unittest way is used to test code that is majorly in classes. That is why it is OOP oriented.

## 02 - This function prints My name is <first name> <last name>
- Prototype: `def say_my_name(first_name, last_name=""):`
- `first_name` and `last_name` must be strings otherwise, raises a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`
- No modules were imported