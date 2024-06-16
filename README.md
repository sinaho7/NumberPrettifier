# Number Prettifier

## Overview
The Number Prettifier project aims to provide a utility for converting large numbers into a more human-readable format. It takes numeric input and returns a truncated, "prettified" string version. This prettified version includes one number after the decimal when the truncated number is not an integer and supports millions, billions, and trillions.

## Approach
The approach involves the following steps:
1. Determine the appropriate unit based on the magnitude of the number (thousands, millions, billions, trillions).
2. Truncate the number to one decimal place if it's not an integer.
3. Construct the prettified string by combining the truncated number and the unit.

## Assumptions
1. The input will be a numeric type (integer or float).
2. The function supports thousands (K), millions (M), billions (B), and trillions (T).
3. Numbers smaller than one thousand should be returned as is.


## Design Decisions
1. Implementation of a static method within a class (`NumberPrettifier`) for modularity and encapsulation.
2. Definition of units and their corresponding divisors as class-level constants for easy maintenance.
3. Usage of string formatting to ensure one decimal place is shown when necessary.
4. Consideration of edge cases such as very small numbers, zero, and boundary values.
5. Use of Python's `unittest` framework for testing to ensure correctness and robustness of the solution.

## Requirements Questions
1. Are there any specific performance requirements or constraints for the function?
2. Should the function handle edge cases such as very large numbers beyond trillions?
3. Is there a preferred output format for special cases like zero or very small numbers?

## Time Complexity
The time complexity of the Number Prettifier function is O(1) as it involves simple arithmetic operations and a constant number of iterations through a predefined set of units.

## Space Complexity
The space complexity of the Number Prettifier function is O(1) as it does not require any additional data structures or allocations that grow with the size of the input.

## Running Tests
To run the tests, navigate to the directory containing `test_prettifier.py` and use the following command:

```bash
python -m unittest test_prettifier.py
