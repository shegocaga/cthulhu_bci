import io

MaxVal = 10000000
StepInterval = 1


#try:
#    for i in range(1, MaxVal, StepInterval):
#        print(i)
#except KeyboardInterrupt:
#    print("INTERRUPTED!")
#    #pass

f = io.StringIO()
f.write("Some Text")
f.write("Some more text!")
my_bytes = f.getvalue().encode("cp1252")
print(my_bytes)

print("done")
