def generate_fibonacci(n):
    """
    Generate a Fibonacci sequence up to the nth term.
    
    :param n: The number of terms in the Fibonacci sequence.
    :return: A list containing the Fibonacci sequence.
    """
    fibonacci_sequence = [0, 1]
    
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence

def main():
    try:
        n = int(input("Enter the number of Fibonacci terms to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        
        fibonacci_sequence = generate_fibonacci(n)
        print("Fibonacci Sequence:")
        print(fibonacci_sequence)
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
