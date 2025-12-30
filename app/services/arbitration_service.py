# app/services/arbitration_service.py
from typing import List, Dict
import random

class ArbitrationService:
    """
    ArbitrationService collects responses from multiple models (cloud/local)
    and decides the best response based on confidence, relevance, or multi-model voting.
    """

    def __init__(self, model_adapter):
        """
        model_adapter: A unified interface to your LLMs (OpenAI, Grok, Anthropic, OLAMA, etc.)
        """
        self.model_adapter = model_adapter

    def collect(self, message: str, context: List[Dict]) -> List[Dict]:
        """
        Collects responses from multiple models.
        Returns a list of dicts:
        [
            {"model": "openai", "response": "...", "confidence": 0.9},
            {"model": "grok", "response": "...", "confidence": 0.8},
            ...
        ]
        """
        models_to_query = self.model_adapter.available_models()

        responses = []
        for model_name in models_to_query:
            try:
                reply, confidence = self.model_adapter.generate(
                    model_name=model_name,
                    message=message,
                    context=context
                )
                responses.append({
                    "model": model_name,
                    "response": reply,
                    "confidence": confidence
                })
            except Exception as e:
                # Log failure per model but continue
                print(f"[ArbitrationService] {model_name} failed: {e}")

        return responses

    def decide(self, responses: List[Dict]) -> str:
        """
        Decide the best response from collected responses.
        Can implement:
          - Highest confidence
          - Multi-model consensus
          - Mixed factual aggregation
        """

        if not responses:
            return "I'm sorry, I cannot generate a response at this time."

        # First, try to find consensus (responses with exact match)
        response_texts = [r["response"] for r in responses]
        consensus_response = max(set(response_texts), key=response_texts.count)
        count = response_texts.count(consensus_response)

        if count > 1:
            # If multiple models agree, return consensus
            return consensus_response

        # If no consensus, pick the one with highest confidence
        sorted_by_conf = sorted(responses, key=lambda x: x.get("confidence", 0), reverse=True)
        best_response = sorted_by_conf[0]["response"]

        # Optional: Mix multiple responses (basic aggregation)
        # For now, we just append secondary info if any
        if len(sorted_by_conf) > 1:
            secondary_response = sorted_by_conf[1]["response"]
            if secondary_response not in best_response:
                best_response = f"{best_response} \n\nAlso consider: {secondary_response}"

        return best_response