
carDealer = {
  "brand": ['Chevrolet', 'Jeep', 'Ford', 'Cadillac', 'Hyundai', 'Mazda', 'Lexus', 'Lamborghini', 'Mercedes', 'Buick', 'Nissan', 'Toyota', 'Audi', 'Kia', 'Prsche', 'Peugeot', 'Suziki', 'Pontiac', 'Land Rover', 'Renault', 'Daewoo', 'Opel', 'Maserati', 'Tata', 'Hammer', 'Bugatti', 'Jaguar', 'Volvo', 'Dodge', 'Chrysler'],
  
  "model": ['Tahoe', 'Wrangler', 'Mustang', 'CT4 Compact', 'Creta', 'CX-5', 'GX', 'Huran Euro', 'Benz', 'Encore', 'Pathfinder', 'Corolla', 'Sedans', 'Sonet', 'Macan', 'Passenger', 'Alto 800', 'Vibe', 'Discovery', 'Triber', 'Matiz', 'Corsa', 'Ghibli', 'Tiago', 'H3T', 'La Voiture', 'Lakh', 'S60', 'Hornet', 'Imperial' ],
  
  "price": [5.8, 7.4, 9.0, 12.8, 8.0, 1.4, 5.4, 9.1, 24.0, 1.7, 6.2, 3.8, 2.3, 2.7, 1.3, 7.8, 1.1, 1.7, 3.5, 20.0, 2.0, 5.5, 15.5, 3.2, 28.0, 13.4, 1.3, 4.5, 1.0, 6.3]
}

print('What are the brands of cars available: ')
for i in carDealer['brand']:
   print(i)
print('\n')

userChoice = input('What brand of car do you want: ')
if(userChoice in carDealer['brand']):
    print('Model available -> ' + carDealer['model'][carDealer['brand'].index(userChoice)])
    print('Price of model  -> ' + '$'+ str(carDealer['price'][carDealer['brand'].index(userChoice)] * (10 ** 6)))
else:
    print('Brand of car wanted is not available at the moment')
