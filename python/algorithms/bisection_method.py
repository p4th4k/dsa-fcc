def square_root_bisection(number, tolerance=0.1, max_iterations = 10):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    
    root = 0
    low = 0
    high = number

    itr_count = 0
    while itr_count < max_iterations:
        mid = (low + high)/2
        square = mid**2
        if square > number and (high-low) > tolerance:
            high = mid
        elif square < number and (high-low) > tolerance:
            low = mid
        else:
            print(f"The square root of {number} is approximately {mid}")
            return mid
        itr_count += 1
    print(f"Failed to converge within {max_iterations} iterations")
    return None
