from sqlalchemy import create_engine

# dialect+driver://username:password@host:port/database
url = 'mysql+pymysql://root:password@db/app_test?charset=utf8'
engine = create_engine(url, echo=True)

engine.execute('CREATE TABLE drink (name VARCHAR(20) PRIMARY KEY, price INT)')

ins = 'INSERT INTO drink (name, price) VALUES (%s, %s)'
engine.execute(ins, 'beer', 580)
engine.execute(ins, 'whiskey', 720)
engine.execute(ins, 'sake', 880)

rows = engine.execute('SELECT * FROM drink')

for row in rows:
    print(row)
