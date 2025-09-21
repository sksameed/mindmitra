from typing import Dict, Any, List
import re


class DataProcessor:
    def __init__(self):
        self.text_cleaning_rules = {
            "strip_whitespace": True,
            "lowercase": True,
            "remove_special_chars": True
        }

    def clean_text(self, text: str) -> str:
        if not text:
            return ""
        cleaned = text.strip() if self.text_cleaning_rules["strip_whitespace"] else text
        if self.text_cleaning_rules["lowercase"]:
            cleaned = cleaned.lower()
        if self.text_cleaning_rules["remove_special_chars"]:
            cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", cleaned)
        return cleaned

    def validate_user_input(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        validated = {}
        for key, value in user_data.items():
            if isinstance(value, str):
                validated[key] = self.clean_text(value)
            elif isinstance(value, (int, float)):
                validated[key] = value
            elif isinstance(value, list):
                validated[key] = [self.clean_text(str(v)) for v in value]
            else:
                validated[key] = str(value)
        return validated

    def normalize_scores(self, scores: Dict[str, float], scale: int = 100) -> Dict[str, float]:
        if not scores:
            return {}
        max_val = max(scores.values()) or 1
        return {k: round((v / max_val) * scale, 2) for k, v in scores.items()}

    def aggregate_responses(self, responses: List[Dict[str, Any]]) -> Dict[str, Any]:
        aggregated = {}
        for response in responses:
            for key, value in response.items():
                if key not in aggregated:
                    aggregated[key] = []
                aggregated[key].append(value)
        return aggregated

    # 🔑 This is what app.py expects
    def process_answers(self, answers: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process raw answers from session into a cleaned, normalized profile.
        """
        validated = self.validate_user_input(answers)

        # Example transformation: count agreement levels
        personality_scores = {}
        for qid, ans in validated.items():
            if isinstance(ans, str):
                if ans in ["Agree", "Strongly Agree"]:
                    personality_scores[qid] = 1
                elif ans in ["Disagree", "Strongly Disagree"]:
                    personality_scores[qid] = -1
                else:
                    personality_scores[qid] = 0

        normalized = self.normalize_scores(personality_scores)
        return {
            "raw": validated,
            "scores": normalized
        }
