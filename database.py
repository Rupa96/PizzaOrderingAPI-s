from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine=create_engine('postgresql://postgres:local_pc1234@localhost/pizza_delivery',
    echo=True
)

Base=declarative_base()

Session=sessionmaker()