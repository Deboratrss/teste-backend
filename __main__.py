import requests
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


response = requests.get("https://api.chucknorris.io/jokes/random")
piada = response.json()['value']


engine = create_engine('sqlite:///database.db')

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos' 

    id = Column(Integer, primary_key=True)
    title = Column(String)
    category = Column(String)
    price = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

url = "https://dummyjson.com/products"
response = requests.get(url)
products = response.json()['products']
soma_precos = 0
qd_smartphone = 0

for produto in products:
    p = Produto(title = produto['title'], category = produto['category'], price = produto['price'])
    session.add(p)
    session.commit()

    if produto['category'] == 'smartphones':
        qd_smartphone = qd_smartphone + 1 
        soma_precos = soma_precos + produto['price']

session.close()

print("## Resultado da coleta de dados ##")
print("Preço médio dos smartphones: $ %.2f" % (soma_precos / qd_smartphone))
print()
print("Uma piadinha só para contrariar:")
print(piada)
