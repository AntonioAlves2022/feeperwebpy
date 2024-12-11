from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from typing import Dict, List, Any

Base = declarative_base()

class TutorModule:
    def __init__(self, student_profile: Dict[str, Any]):
        self.student_profile = student_profile
        self.learning_strategies = self._load_learning_strategies()
    
    def _load_learning_strategies(self) -> Dict[str, Any]:
        """
        Carrega estratégias de ensino baseadas no perfil do estudante
        """
        strategies = {
            "beginner": {
                "approach": "scaffolding",
                "content_difficulty": "low",
                "interaction_level": "high_support"
            },
            "intermediate": {
                "approach": "guided_exploration",
                "content_difficulty": "medium",
                "interaction_level": "moderate_support"
            },
            "advanced": {
                "approach": "problem_based_learning",
                "content_difficulty": "high",
                "interaction_level": "minimal_support"
            }
        }
        return strategies
    
    def determine_teaching_strategy(self) -> Dict[str, Any]:
        """
        Determina a estratégia de ensino com base no perfil do estudante
        """
        level = self.student_profile.get('programming_level', 'beginner')
        strategy = self.learning_strategies.get(level, self.learning_strategies['beginner'])
        
        return {
            "strategy": strategy,
            "personalized_content": self._select_personalized_content(strategy)
        }
    
    def _select_personalized_content(self, strategy: Dict[str, str]) -> List[Dict[str, Any]]:
        """
        Seleciona conteúdo personalizado baseado na estratégia
        """
        content_library = {
            "beginner": [
                {
                    "type": "tutorial",
                    "title": "Introdução à Programação em Python",
                    "difficulty": "low",
                    "format": "video_lesson"
                },
                {
                    "type": "exercise",
                    "title": "Primeiro Programa: Olá Mundo",
                    "difficulty": "low",
                    "format": "coding_challenge"
                }
            ],
            "intermediate": [
                {
                    "type": "project",
                    "title": "Sistema de Gerenciamento de Tarefas",
                    "difficulty": "medium",
                    "format": "hands_on_project"
                },
                {
                    "type": "theory",
                    "title": "Programação Orientada a Objetos",
                    "difficulty": "medium",
                    "format": "interactive_lesson"
                }
            ],
            "advanced": [
                {
                    "type": "advanced_project",
                    "title": "Desenvolvimento de API RESTful",
                    "difficulty": "high",
                    "format": "comprehensive_project"
                },
                {
                    "type": "advanced_theory",
                    "title": "Design Patterns em Python",
                    "difficulty": "high",
                    "format": "in_depth_seminar"
                }
            ]
        }
        
        difficulty = strategy.get('content_difficulty', 'low')
        return content_library.get(difficulty, content_library['beginner'])
    
    def generate_learning_path(self) -> Dict[str, Any]:
        """
        Gera um caminho de aprendizado personalizado
        """
        strategy = self.determine_teaching_strategy()
        
        return {
            "learning_path": {
                "current_level": self.student_profile.get('programming_level'),
                "recommended_content": strategy['personalized_content'],
                "learning_approach": strategy['strategy']['approach']
            }
        }
    
    def track_student_progress(self, student_performance: Dict[str, Any]) -> Dict[str, Any]:
        """
        Acompanha o progresso do estudante e ajusta a estratégia
        """
        progress_metrics = {
            "completed_tasks": student_performance.get('completed_tasks', 0),
            "success_rate": student_performance.get('success_rate', 0),
            "time_spent": student_performance.get('time_spent', 0)
        }
        
        # Lógica de ajuste de estratégia baseada no desempenho
        if progress_metrics['success_rate'] > 0.8:
            return {"recommendation": "advance_level"}
        elif progress_metrics['success_rate'] < 0.5:
            return {"recommendation": "provide_additional_support"}
        else:
            return {"recommendation": "continue_current_path"}

class TutorModel(Base):
    __tablename__ = 'tutors'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, nullable=False)
    learning_path = Column(JSON)
    progress_history = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
