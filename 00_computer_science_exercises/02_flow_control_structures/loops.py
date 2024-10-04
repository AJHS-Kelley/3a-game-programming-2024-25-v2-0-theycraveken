# Loops, Kennedy Spencer, v0.1
import random # import the random module for us tp use.
# Generally put all your import statements at the top.

#  TWO TYPES OF LOOPS 
# for <-- Used when you kno whow many loops you'll need.
# while <-- Used when you do not know how many loops you'll need.

# for loop is like Go Fish, you search each card for what the player asked.
# while loop is like musical chairs, you move around until the music stops.

# EACH TRIP THROUGH THE ENTIRE LOOP IS CALLED AN iteration
# "iterate throgh the list" means use a for loop

# for loop Example -- Iterating a List
# fruits =["apple", " banana", "kiwi", "orange"]
# for eachFruit in fruits:
#     print(eachFruit)

#continue Keyword -- Skips the current iteration and then finishes the loop.
# fruits =["apple", " banana", "kiwi", "orange"]
# for eachFruit in fruits:
#     if eachFruit== "banana":
#         continue
#     print(eachFruit)

# break Keyword -- Immediately exit the loop.
# fruits =["apple", " banana", "kiwi", "orange"]
# for eachFruit in fruits:
#     if eachFruit== "banana":
#         break
#     print(eachFruit)

# for loops using range().  range(x) is EXCLUSIVE, it starts at 0 and ends at x -1 
# for i in range(10): # range is 0-9
#     print(i)

# # Might not always want to start at zero.
# for i in range(10,100): #
#     print(i)

# # Not want to count by 1
# for i in range(10,100,5) # 10 = start, 100 - 1 = stop, 5 = # to count by
#     print(i)

# Sometimes you're not done writing the loops.
# for x in range (10):
#     pass # tells Pthon this loop isn't finished, don't Freak out.



# while loops -- Musical Chairs
playerscore = 0
counter =0
while playerscore < 199: # Run as long as this true.
    print(f"Starting: {playerscore}")
    playerscore += random.randint(1,100)
    print(f"After: {playerscore}")
    counter += 1
print(f" Counter: {counter}") 



loopCount = 0 
