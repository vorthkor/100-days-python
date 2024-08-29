# day20_100 days - loop increment

print("""
******************
* LIST GENERATOR *
******************

""")

start = int(input("Start at: "))
end = int(input("End before: "))
inc = int(input("Increment between values: "))
print()

for i in range(start, end, inc):
  print(i)