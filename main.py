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
#Taking Number(Watch)
watch_number = int(input("Please Enter A Watch Number: " ))

#is he Working ?
work_yes_no = str(input("Are You Actively Working(please enter just yes or no):"))

#If he is working take now salary
if work_yes_no == "yes" :
    salary = float(input("Please Enter Your Monthly Income: "))
    
# if he is not working take what level is he and take country    
elif work_yes_no == "no":
    country = str(input("Where Do You Want to Work ? (abroad or turkey) :"))
    level = str(input("Please enter Your Level(junior-mid-senior)"))
    
    #Turkey Working
    if country == "turkey" :  
        salary_usd_dict = SALARY_DATA_USD["turkey"]
        turkey_salary = salary_usd_dict.get(level)
        salary = turkey_salary 
    #Abroad Working
    elif country == "abroad" :
        salary_usd_dict = SALARY_DATA_USD["abroad"]
        abroad_salary = salary_usd_dict.get(level)
        salary = abroad_salary
#calculate net income
expense = float(input("Please Enter Your Monthly Expenses: "))
net = salary - expense 

price_dict = WATCH["Watch_Price"]
price = price_dict.get(watch_number) 

name_dict = WATCH["Watch_Name"]
watch_name = name_dict.get(watch_number)

month = price / net 

print(f"YOUR MONTHLY NET INCOME: {net}   | YOU CHOOSE WATCH: {watch_name}  |  YOU CHOOSE WATCH PRİCE: {price}   |  YOU WILL RECEIVE THIS WATCH IN {month} MONTHS.  ")