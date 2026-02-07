print("""PLEASE WRITE DOWN THE NUMBER NEXT TO THE WATCH YOU WANT.
      1-Rolex Datejust 41(16.500$)
      2-Rolex Yacht-Master II(22.500$)
      3-Patek Philippe Aquanaut 5167A(70.000$)
      4-Cartier Santos de Cartier(8.000$)
      5-Audemars Piguet Royal Oak 15510ST(50.000$)
      """)

WATCH= {   
    "Watch_Price" :  {
        1 : 16500,
        2 : 22500,
        3 : 70000,
        4 : 8000,
        5 : 50000,
    },
    "Watch_Name" : {
        1 : "Rolex Datejust 41" ,
        2 : "Rolex Yacht-Master II ", 
        3 : "Patek Philippe Aquanaut" ,
        4 : "Cartier Santos de Cartier",
        5 : "Audemars Piguet Royal Oak" , 
}
}



SALARY_DATA_USD = {
    "turkey" : {
        "junior" : 1000,
        "mid"    : 1500,
        "senior" : 2000,
                }, 
    "abroad" : {
        "junior" : 3000,
        "mid"    : 5000,
        "senior" : 7000,
     }
}


salary = float(input("Please Enter Your Monthly Income: "))
expense = float(input("Please Enter Your Monthly Expenses: "))
net = salary - expense 

watch_number = int(input("Please Enter A Watch Number: " ))

price_dict = WATCH["Watch_Price"]
price = price_dict.get(watch_number) 

name_dict = WATCH["Watch_Name"]
watch_name = name_dict.get(watch_number)

month = price / net 

print(f"YOUR MONTHLY NET INCOME: {net}   | YOU CHOOSE WATCH: {watch_name}  |  YOU CHOOSE WATCH PRİCE: {price}   |  YOU WILL RECEIVE THIS WATCH IN {month} MONTHS.  ")