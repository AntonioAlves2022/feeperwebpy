import openai
from typing import Dict, Any

class CodeEvaluationService:
    def __init__(self, openai_api_key: str):
        openai.api_key = openai_api_key
    
    def evaluate_code(self, student_code: str, expected_output: str) -> Dict[str, Any]:
        """
        Avalia o código do estudante usando GPT
        """
        prompt = f"""
        Avalie o seguinte código de programação:
        
        Código do Estudante:
        {student_code}
        
        Saída Esperada:
        {expected_output}
        
        Por favor, forneça:
        1. Correções necessárias
        2. Comentários sobre boas práticas
        3. Pontuação de 0-10
        4. Sugestões de melhoria
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            
            evaluation = response.choices[0].message.content
            return {
                "evaluation": evaluation,
                "score": self._extract_score(evaluation)
            }
        
        except Exception as e:
            return {"error": str(e)}
    
    def _extract_score(self, evaluation: str) -> float:
        # Lógica para extrair a pontuação da avaliação
        pass
