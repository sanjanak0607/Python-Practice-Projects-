#ek file leni h 1000 lines ki jisme errors bi honge warnings and info bhi and vhi line print krvani h jaha error honge count bi dena h
line_no=1
errors=0
with open("xyz.txt") as f:
    for line in f:
        if "error" in line:
            print("line", line_no,':', line.strip())
            errors += 1
        line_no += 1
print('total errors:', errors)