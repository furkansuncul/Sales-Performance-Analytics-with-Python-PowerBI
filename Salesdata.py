'''
Created on 1 Mar 2026

@author: furka
'''
import pandas as pd
from faker import Faker
import random

fake = Faker()

# Kategori ve ürünler
categories = ['Teknoloji', 'Mobilya', 'Ofis Malzemeleri']
products = {
    'Teknoloji': ['Laptop', 'Telefon', 'Monitör', 'Klavye'],
    'Mobilya': ['Masa', 'Sandalye', 'Kitaplık', 'Lamba'],
    'Ofis Malzemeleri': ['Kağıt', 'Kalem Seti', 'Zımba', 'Dosya']
}

data = []

# Veri Üretme
for i in range(1000):
    cat = random.choice(categories)
    prod = random.choice(products[cat])
    price = random.randint(100, 5000) if cat == 'Teknoloji' else random.randint(10, 500)
    quantity = random.randint(1, 5)
    
    data.append({
        'Order_ID': f'ORD-{1000 + i}',
        'Date': fake.date_between(start_date='-2y', end_date='today'),
        'Customer_Name': fake.name(),
        'City': fake.city(),
        'Category': cat,
        'Product': prod,
        'Sales_Amount': price * quantity,
        'Quantity': quantity,
        'Profit': (price * quantity) * random.uniform(0.1, 0.3) # %10-30 kar marjı
    })

# CSV Olarak Kaydetme
df = pd.DataFrame(data)
df.to_csv('Sales_Performance_Data.csv', index=False)
print("Veri seti başarıyla oluşturuldu: Sales_Performance_Data.csv")