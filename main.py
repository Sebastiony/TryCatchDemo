import os, json

# Random function that has a 1 in 100 chance to throw error
def random_function():
    import random
    if random.randint(1, 100) == 1:
        raise Exception("Random error")
    else:
        return True
    

# Main function that will:
# 1. Catch error
# 2. Save all successful numbers to success.json
# 3. Save error number to error.json

saved_numbers = []

def main():
    try:
        for x in range(1000):
            if random_function():
                print(f"Success: {x}")
                saved_numbers.append(x)
    except Exception as e:
                with open("success.json", "w") as f:
                    saved_json = json.dumps(saved_numbers, indent=2)
                    f.write(saved_json)
                with open("error.json", "w") as f:
                    f.write(f"{x}\n")
                print(e)



main()
