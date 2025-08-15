#for variavel in range

for i in range(5):
    print("repeticao", i)

for i in range(1, 11, 2):
    print(i)


# --------------------------------------------

# While

counter_time = 0

while counter_time < 5:
    print("counter_time", counter_time)
    counter_time += 1




# for

num = int(input("Chose a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# --------------------

timer_start = int(input("Set timer start: "))
while timer_start > 0:
    timer_start -= 1
    print(f"{timer_start}")