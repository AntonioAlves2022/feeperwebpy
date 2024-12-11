from sqlalchemy import Column, Integer, String, JSON, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from typing import Dict, List, Any
import json

Base = declarative_base()

class InterfaceModule:
    def __init__(self, student_profile: Dict[str, Any]):
        self.student_profile = student_profile
        self.interface_components = self._load_interface_components()
        self.chatbot_config = self._configure_chatbot()
    
    def _load_interface_components(self) -> Dict[str, Any]:
        """
        Carrega componentes de interface personalizados
        """
        return {
            "color_scheme": self._select_color_scheme(),
            "layout_preference": self._determine_layout(),
            "accessibility_options": {
                "high_contrast": False,
                "text_size": "medium",
                "screen_reader_support": True
            }
        }
    
    def _select_color_scheme(self) -> str:
        """
        Seleciona esquema de cores baseado no perfil do estudante
        """
        learning_style = self.student_profile.get('learning_style', 'default')
        color_schemes = {
            "visual": "high_contrast_blue",
            "kinesthetic": "soft_green",
            "default": "neutral_gray"
        }
        return color_schemes.get(learning_style, color_schemes['default'])
    
    def _determine_layout(self) -> Dict[str, str]:
        """
        Determina layout da interface
        """
        return {
            "main_view": "vertical_split",
            "code_editor": "syntax_highlighted",
            "tutorial_section": "side_panel"
        }
    
    def _configure_chatbot(self) -> Dict[str, Any]:
        """
        Configura assistente de chatbot personalizado
        """
        return {
            "personality": "friendly_mentor",
            "response_style": {
                "beginner": "very_detailed",
                "intermediate": "balanced",
                "advanced": "concise"
            },
            "support_level": self._determine_chatbot_support_level()
        }
    
    def _determine_chatbot_support_level(self) -> str:
        """
        Determina nível de suporte do chatbot
        """
        programming_level = self.student_profile.get('programming_level', 'beginner')
        support_levels = {
            "beginner": "high_interaction",
            "intermediate": "moderate_guidance",
            "advanced": "minimal_hints"
        }
        return support_levels.get(programming_level, support_levels['beginner'])
    
    def generate_interactive_content(self, content_type: str) -> Dict[str, Any]:
        """
        Gera conteúdo interativo baseado no tipo
        """
        interactive_contents = {
            "coding_exercise": self._generate_coding_exercise(),
            "tutorial_slide": self._generate_tutorial_slide(),
            "code_visualization": self._generate_code_visualization()
        }
        
        return interactive_contents.get(content_type, {
            "error": "Tipo de conteúdo não encontrado"
        })
    
    def _generate_coding_exercise(self) -> Dict[str, Any]:
        """
        Gera exercício de código interativo
        """
        return {
            "title": "Exercício de Programação",
            "instructions": "Complete o código para calcular a média de uma lista",
            "starter_code": """
def calcular_media(numeros):
    # Seu código aqui
    pass
            """,
            "test_cases": [
                {"input": "[10, 20, 30]", "expected_output": "20"},
                {"input": "[5, 5, 5]", "expected_output": "5"}
            ]
        }
    
    def _generate_tutorial_slide(self) -> Dict[str, Any]:
        """
        Gera slide de tutorial interativo
        """
        return {
            "topic": "Introdução a Funções em Python",
            "content": "Aprenda a criar e usar funções",
            "interactive_elements": {
                "code_example": "def saudacao(nome):\n    print(f'Olá, {nome}!')",
                "quiz_question": "O que a função acima faz?",
                "quiz_options": [
                    "Imprime uma saudação personalizada",
                    "Calcula um número",
                    "C