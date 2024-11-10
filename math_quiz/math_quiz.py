import random


def generate_random_integer(min, max):
    """
    Generate a random integer between min_value and max_value.
    """
    return random.randint(min, max)


def select_random_operator():
    """
    Select a random operator from the set of basic math operations: +, -, *.
    """
    return random.choice(['+', '-', '*'])


def evaluate_expression(n1, n2, o):
    """
      Evaluate the expression based on the provided numbers and operator.
    Parameters:
        n1 (int): The first number.
        n2 (int): The second number.
        operator (str): The operator for the math expression.
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    """
    Run a math quiz game for the user to solve a series of math problems.
    """
    s = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = generate_random_integer(1, 10); n2 = generate_random_integer(1, 5); o = select_random_operator()

        PROBLEM, ANSWER = evaluate_expression(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)
        except:
            print(f"Invalid Input-{useranswer}, Enter a integer value")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
