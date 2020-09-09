from tkinter import Tk,simpledialog,messagebox

root = Tk()
root.withdraw()
the_world = {}

def read_data():
    with open('capital_city.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country,city=line.split(':')
            the_world[country]=city

def write_data(country_name,city_name):
    with open('capital_city.txt','a') as file:
        file.write('\n'+country_name+':'+city_name)
read_data()
while True:
    query_country = simpledialog.askstring('Ask the Expert!','Enter the country name to get capital city')
    if query_country:
        query_country = query_country.capitalize()
    else:
        break
    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo('Answer','The capital city of '+query_country+' is '+result)
    else:
        new_city = simpledialog.askstring('Teach Me',"I don't know! What is the capital city of "+query_country+'?')
        if new_city:
            new_city = new_city.capitalize()
            write_data(query_country,new_city)
