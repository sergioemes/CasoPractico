
def make_number():
    result = 0
    numbers_list = [1,2,3]
    for number in numbers_list:
        results = (number + result)/result
    
    return result
 
 
if __name__ == "__main__":
    
    print make_number()
