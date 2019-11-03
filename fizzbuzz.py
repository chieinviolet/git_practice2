def fizzbuzz_convert(number):

    if number % 15 == 0:
        print ('FizzBuzz')
    if number % 3 == 0:
        print ('Fizz')
    if number % 5 == 0:
        print ('Buzz')
    else:
        print(number)

assert fizzbuzz_convert(3) == 'Fizz'
assert fizzbuzz_convert(5) == 'Buzz'
assert fizzbuzz_convert(15) == 'FizzBuzz'
