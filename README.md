# TryCatchPythonDemo

## Reason

I was going through 9000+ SMS files that had to be uploaded to our database. I wanted to test catching potential errors that could occur during the process. I created a simple script that would throw an error if the file was not found. I then created a try catch block to catch the error and print a message to the console.

This way I could see which files were not found and then manually upload them to the database. Whilst having a list of the files that successfully entered the database.

## Usage

Simply running the program gives you an update on the files that were successfully uploaded and the files that were not found.

```python

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
```
