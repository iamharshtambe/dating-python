motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "royal enfield"
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles.insert(0, "tvs")
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
