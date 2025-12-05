# Exercise 3-4
guests = ["Virat", "Rohit", "AB"]

print(f"Hey {guests[0]}, you're invited for dinner.")
print(f"Hey {guests[1]}, you're invited for dinner.")
print(f"Hey {guests[2]}, you're invited for dinner.")

# Exercise 3-5
print(f"\nSorry guys, but {guests[2]} can't come today.")

guests[2] = "Sachin"

print(f"Hey {guests[2]}, you're invited for dinner.")

# Exercise 3-6
print("\nGreat news! We found a bigger table.")

guests.insert(0, "David")
guests.insert(1, "Chris")
guests.append("Joe")

print(f"Hey {guests[0]}, you're invited for dinner.")
print(f"Hey {guests[1]}, you're invited for dinner.")
print(f"Hey {guests[2]}, you're invited for dinner.")
print(f"Hey {guests[3]}, you're invited for dinner.")
print(f"Hey {guests[4]}, you're invited for dinner.")
print(f"Hey {guests[5]}, you're invited for dinner.")

# Exercise 3-7
print(
    "\nUnfortunately, the new table won't arrive on time. Only two guests can be invited."
)

popped1 = guests.pop()
print(f"Sorry {popped1}, we can't invite you for dinner.")

popped2 = guests.pop()
print(f"Sorry {popped2}, we can't invite you for dinner.")

popped3 = guests.pop()
print(f"Sorry {popped3}, we can't invite you for dinner.")

popped4 = guests.pop()
print(f"Sorry {popped4}, we can't invite you for dinner.")

print(f"\n{guests[0]}, you're still invited.")
print(f"{guests[1]}, you're still invited.")

del guests[0]
del guests[0]

print("\nFinal guest list:", guests)
