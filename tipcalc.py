print('''
╔╦╗╦╔═╗  ╔═╗╔═╗╦  ╔═╗╦ ╦╦  ╔═╗╔╦╗╔═╗╦═╗
 ║ ║╠═╝  ║  ╠═╣║  ║  ║ ║║  ╠═╣ ║ ║ ║╠╦╝
 ╩ ╩╩    ╚═╝╩ ╩╩═╝╚═╝╚═╝╩═╝╩ ╩ ╩ ╚═╝╩╚═''')
bill = float(input("What is the total bill:$"))
tip = int(input("How much tip would you like to give?: 0%, 5%, 10%, 12%, 15%: "))
people = int(input("How many people are there?: "))
bill_tip = tip / 100 * bill + bill
bill_per_person = bill_tip / people
final_bill = round(bill_per_person, 3)
print(f"Each person gotta pay {final_bill} ")
billp1f = tip / 100 * bill + bill
print(f"OR if its just one person paying your TOTAL is: {billp1f}$")