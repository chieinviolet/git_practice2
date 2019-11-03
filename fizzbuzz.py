def fizzbuzz_convert(number):

    if number % 15 == 0:
        return ('FizzBuzz')
    if number % 3 == 0:
        return ('Fizz')
    if number % 5 == 0:
        return ('Buzz')
    return str(number)


for i in range(1, 101):
    print(fizzbuzz_convert(i))

assert fizzbuzz_convert(3) == 'Fizz'
assert fizzbuzz_convert(5) == 'Buzz'
assert fizzbuzz_convert(15) == 'FizzBuzz'
assert fizzbuzz_convert(7) == '7'
