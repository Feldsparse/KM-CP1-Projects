#charles motta. idiot proof

name1 = input("what is your first name? ").strip().title()
name2 = input("what is your last name? ").strip().title()

name3 = name1.split()
name4 = name2.split()

name5 = "".join(name3)
name6 = "".join(name4)

full_name = name5.title() + " " + name6.title()
print(full_name)

while True:

    try:
        number =(int(input("what is your phonenumber? ")))

    except:
        print("thats not a phone number")

    else:
        break

print(number)