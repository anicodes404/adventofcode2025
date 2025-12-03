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

            if len(s) % 2 == 0: 
                half = len(s) // 2
                left = s[:half]
                right = s[half:]

                if left == right: 
                    total += n

    return total 

    
result = solve(line)
print(result)


# for each r in range_list:

    
#     (start_str, end_str) = split r by "-"
#     start = convert start_str to integer
#     end = convert end_str to integer
    
#     for n from start to end:
        
#         s = convert n to string
        
#         if length of s is even:
            
#             half = length of s / 2
#             left = substring of s from 0 to half
#             right = substring of s from half to end
            
#             if left == right:
#                 total = total + n

# print total



# first_id
# comma_seperate
# last_id

# sequence of digits repeated twice (any number)
# invalid_ids


