# count the even numbers 

def count_even_numbers(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


def count_odd_numbers(numbers):
    count = 0
    for number in numbers:
        if number % 2 != 0:
            count += 1
    return count 


# Example usage
if __name__ == "__main__":
    sample_numbers = [1, 2, 3, 4, 5, 6]
    even_count = count_even_numbers(sample_numbers)
    print(f"Count of even numbers: {even_count}")

    odd_count = count_odd_numbers(sample_numbers)
    print(f"Count of odd numbers: {odd_count}")# count the odd numbers  
    


