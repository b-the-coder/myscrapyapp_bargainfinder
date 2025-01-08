import matplotlib.pyplot as plt 
import csv 
  
prices = []
  
with open('adidashoodies.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    print(plots) 
    next(plots)
    for row  in plots:
        price = int(row[1].replace('$', ''))
        prices.append(price)
         
  
plt.hist(prices, bins= 10, color = 'g') 
plt.xlabel('Price Range(USD)') 
plt.ylabel('Product Numbers') 
plt.title('Adidas Women Hoodies Price Distrubute') 
plt.grid(True)
plt.tight_layout()
plt.show() 