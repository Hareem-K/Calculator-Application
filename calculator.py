#
# calculator.py
# Hareem Khan, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.
#
# first, the user is instructed to input three numbers and two operators
first_number = int(input('Enter the first value:\n'))
first_operator = input('Enter the first operator:\n')
second_number = int(input('Enter the second value:\n'))
second_operator = input('Enter the second operator:\n')
third_number = int(input('Enter the thrid value\n'))

# if the first operator that was inputted is +, then the code will run through the four options of second operators to combine with it to complete the expression.
if first_operator == '+' :
    if second_operator == '+':
        entered_expression = first_number + second_number + third_number
    elif second_operator == '-':
        entered_expression = first_number + second_number - third_number
    elif second_operator == '*':
        entered_expression = first_number + second_number * third_number
    elif second_operator == '/':
        entered_expression = first_number + second_number // third_number


# if the first operator that was inputted is -, then the code will run through the four options of second operators to combine with it to complete the expression.
elif first_operator == '-':
    if second_operator == '+':
        entered_expression = first_number - second_number + third_number
    elif second_operator == '-':
        entered_expression = first_number - second_number - third_number
    elif second_operator == '*':
        entered_expression = first_number - second_number * third_number
    elif second_operator == '/':
        entered_expression = first_number - second_number // third_number
    

# if the first operator that was inputted is *, then the code will run through the four options of second operators to combine with it to complete the expression.
elif first_operator == '*':
    if second_operator == '+':
        entered_expression = first_number * second_number + third_number
    elif second_operator == '-':
        entered_expression = first_number * second_number - third_number
    elif second_operator == '*':
        entered_expression = first_number * second_number * third_number
    elif second_operator == '/':
        entered_expression = first_number * second_number // third_number
   

# if the first operator that was inputted is /, then the code will run through the four options of second operators to combine with it to complete the expression.
elif first_operator == '/':
    if second_operator == '+':
        entered_expression = first_number // second_number + third_number
    elif second_operator == '-':
        entered_expression = first_number // second_number - third_number
    elif second_operator == '*':
        entered_expression = first_number // second_number * third_number
    elif second_operator == '/':
        entered_expression = first_number // second_number // third_number
  

# We are assuming that only valid integers and operators (+,-,*,/) will be inputted into the code, and therefore will not test for the validity of these inputs. 



# Once the operators are selected and the algebraic expression is created, the code will print out the entered expression and the final answer for the user.

print('Entered Expression:', first_number, first_operator, second_number, second_operator, third_number)
print('Your final answer', entered_expression)
print()

