from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    
    # Características Psicossociais
    learning_style = Column(String(50))  # visual, auditivo, etc
    motivation_level = Column(Integer)
    
    # Nível de Conhecimento
    programming_level = Column(String(20))  # beginner, intermediate, advanced
    
    # Habilidades e Dificuldades
    skills = Column(JSON)  # Habilidades técnicas
    difficulties = Column(JSON)  # Áreas com mais dificuldade
    
    progress_history = Column(JSON)  # Histórico de progresso
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Student {self.username}>"
