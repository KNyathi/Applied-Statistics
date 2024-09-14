#Prompt user for input data
def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():  # Check if the input is a digit
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid integer.")

inputA = get_integer_input("Enter favourable outcome value: ")
inputB = get_integer_input("Enter total possible outcomes value: ")


def basic_probability(favourable_outcomes, total_outcomes):
    result = favourable_outcomes/total_outcomes

    if result >=0 and result<=1:
        return result
    
    print("Error: Probability must be between 0 and 1. Try to think and input meaningful values.")


def result_basic(event, total):
    if basic_probability(event, total) is not None:
        print(f"The probability of picking {event} from {total} is: {basic_probability(event, total):.2f}\n") #round off to two decimal places


result_basic(inputA, inputB)


