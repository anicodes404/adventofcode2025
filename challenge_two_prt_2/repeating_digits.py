with open("input.txt", "r") as file: 
    line = file.read().strip()

def solve(line): 
    range_list = line.split(",")
    total = 0

    for r in range_list: 
        start_str, end_str = r.split("-")
        start = int(start_str)
        end = int(end_str)
        
        for n in range(start, end + 1):
            s = str(n)
            length = len(s)
            invalid = False

            for chunk_size in range(1, length // 2 + 1):
                if length % chunk_size == 0: 
                    chunk = s[:chunk_size]
                    number_of_repeats = length // chunk_size
                    repeated_chunk = chunk * number_of_repeats

                    if repeated_chunk == s: 
                        invalid = True
                        break

            if invalid: 
                total += n

    return total

result = solve(line)
print(result)