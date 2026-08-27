# Working with Numbers
from pyscript import display, document


# Addition
def addition(e):
    document.getElementById("result").innerHTML = " "
    first_number = float(document.getElementById("num1").value or "0")
    second_number = float(document.getElementById("num2").value or "0")
    sum = first_number + second_number

    display(
        f" The sum of {first_number} and {second_number} is {sum}",
        target="result",
    )


# Subtraction
def subtraction(e):
    document.getElementById("result").innerHTML = " "
    first_number = float(document.getElementById("num1").value or "0")
    second_number = float(document.getElementById("num2").value or "0")
    difference = first_number - second_number

    display(
        f" The difference of {first_number} and {second_number} is {difference}",
        target="result",
    )


# Multiplication
def multiplication(e):
    document.getElementById("result").innerHTML = " "
    first_number = float(document.getElementById("num1").value or "0")
    second_number = float(document.getElementById("num2").value or "0")
    product = first_number * second_number

    display(
        f" The product of {first_number} and {second_number} is {product}",
        target="result",
    )


# Division
def division(e):
    document.getElementById("result").innerHTML = " "
    first_number = float(document.getElementById("num1").value or "0")
    second_number = float(document.getElementById("num2").value or "0")
    quotient = first_number / second_number

    display(
        f" The quotient of {first_number} and {second_number} is {quotient}",
        target="result",
    )


# Modulus
def modulus(e):
    document.getElementById("result").innerHTML = " "
    first_number = float(document.getElementById("num1").value or "0")
    second_number = float(document.getElementById("num2").value or "0")
    remainder = first_number % second_number

    display(
        f" The remainder of {first_number} and {second_number} is {remainder}",
        target="result",
    )


# Exponentiation
def exponentiation(e):
    document.getElementById("result").innerHTML = " "
    first_number = float(document.getElementById("num1").value or "0")
    second_number = float(document.getElementById("num2").value or "0")
    power = first_number**second_number

    display(
        f" The exponent of {first_number} and {second_number} is {power}",
        target="result",
    )


# Floor Division
def floor_division(e):
    document.getElementById("result").innerHTML = " "
    first_number = float(document.getElementById("num1").value or "0")
    second_number = float(document.getElementById("num2").value or "0")
    floor_quotient = first_number // second_number

    display(
        f" The floor division of {first_number} and {second_number} is {floor_quotient}",
        target="result",
    )