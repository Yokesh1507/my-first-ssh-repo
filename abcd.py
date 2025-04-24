
a = 'MS Dhoni - 7'
b = 'Virat Kohli - 18'
c = 'Rohit Sharma - 45'
d = 'Sachin Tendulkar - 10'
e = 'Yuvraj Singh - 12'
f = 'Hardik Pandya - 33'
g = 'Jasprit Bumrah - 93'
h = 'Ravindra Jadeja - 8'
i = 'Shubman Gill - 77'
j = 'KL Rahul - 1'
k = 'Mohammed Shami - 11'

india = (a, b, c, d, e, f, g, h, i, j, k)


players_dict = {}
for player in india:
    name, num = player.rsplit(" - ", 1) 
    players_dict[int(num)] = name  



num = int(input("Enter a jersey number: "))

if num in players_dict:
    print(f"The player with jersey number {num} is {players_dict[num]}")
else:
    print("No player found with this jersey   number")



