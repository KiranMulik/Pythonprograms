names = input("Enter names separated by space: ").split()
names.sort(key=lambda name: len(name))
print("Names sorted by length:", names)
