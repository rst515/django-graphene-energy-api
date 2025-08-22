
# django-graphene-energy-api
[![](https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif)]() [![](https://camo.githubusercontent.com/f4f347ad8671a2f09eba5346bd1daa21a4c5d422f2772cc8d625804368cf7087/687474703a2f2f6772617068656e652d707974686f6e2e6f72672f66617669636f6e2e706e67)]()
## Description
A mini GraphQL API demo built with Django + Graphene, modelling energy tariffs and usage data.

## Features
•	Query customers, tariffs, and usage.  
•	Add new usage records via mutations.  
•	Simple relational model in Django ORM.  

## Quickstart
Clone the repo
```bash
git clone <repo>
cd django-graphene-energy-api
```
Create and run migrations and seed data, then run the server. 
```bash
pip install -r requirements.txt
python manage.py makemigrations energy
python manage.py migrate
python manage.py seed
python manage.py runserver
```
Open GraphiQL at: http://127.0.0.1:8000/graphql/

## Example Queries & Mutations: 
Query all customers and their usage
```graphql
{
  allCustomers {
    id
    name
    email
    usagerecordSet {
      kwhUsed
      timestamp
      tariff {
        name
        pricePerKwh
      }
    }
  }
}
```
Query customer usage within a date range (filtered)
```graphql
{
  customerUsage(customerId: 1, startDate: "2025-08-01", endDate: "2025-08-31") {
    id
    kwhUsed
    totalCost
    tariff {
      name
      pricePerKwh
    }
    timestamp
  }
}
```
Mutation: Log a new usage record
```graphql
mutation {
  createUsage(customerId: 1, tariffId: 2, kwhUsed: 12.5) {
    usage {
      id
      kwhUsed
      tariff {
        name
      }
    }
  }
}
```
