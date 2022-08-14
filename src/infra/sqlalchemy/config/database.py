from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# URL de conexão
SQLALCHEMY_DATABASE_URL = "sqlite:///./app_dlx.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Criação do engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa
Base = declarative_base()

# Função para criar o banco de dados
def criar_bd():
    Base.metadata.create_all(bind=engine)

# Função para disponibilizar conexão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

