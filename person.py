from faker import Faker
import csv
import time
faker = Faker('id_ID')
fields = ['fname', 'lname', 'pnumber', 'email']
start_time = time.time()
rows = [(faker.first_name(), faker.last_name(), faker.phone_number(), faker.email()) for _ in range(0, 1000000)]
with open('person1mil.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(rows)
print("--- %s seconds ---" % (time.time() - start_time))
