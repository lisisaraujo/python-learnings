# EXERCISE: TRICKY COUNTER

# my solution
my_list = [1,2,3,4,5,6,7,8,9,10]
print(sum(my_list))

# # ZTM solution
counter = 0
for item in my_list:
    counter = counter + item
print(counter)

# EXERCISE: FIRST GUI

# picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
#            [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]

# case_0 = " "
# case_star = "*"

# for row in picture:
#     for pixel in row:
#         if (pixel == 1):
#             print(case_star, end='')
#         else:
#             print(case_0, end='')
#     print('')

# iterate over picture
# if it's 0 => print " "
# if it's 1 => print "*"

