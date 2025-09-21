from typing import Dict, Any, List


class RecommendationEngine:
    def __init__(self):
        self.skill_resources = {
            "python": ["Codecademy Python", "LeetCode", "Automate the Boring Stuff"],
            "data analysis": ["Kaggle", "Coursera Data Science"],
            "design": ["Figma Tutorials", "UX Collective"],
            "leadership": ["Harvard Business Review", "LinkedIn Learning Leadership"]
        }

        self.career_growth_paths = {
            "software engineer": ["Junior Developer", "Mid-Level Engineer", "Senior Engineer", "Tech Lead"],
            "data scientist": ["Data Analyst", "Junior DS", "Senior DS", "ML Engineer"],
            "ux designer": ["UI Designer", "UX Specialist", "Senior Designer", "Design Manager"],
        }

    def recommend_skills(self, missing_skills: List[str]) -> Dict[str, List[str]]:
        recommendations = {}
        for skill in missing_skills:
            resources = self.skill_resources.get(skill.lower(), ["General skill-building resources"])
            recommendations[skill] = resources
        return recommendations

    def suggest_growth_path(self, career: str) -> List[str]:
        return self.career_growth_paths.get(
            career.lower(),
            ["Entry-level role", "Mid-level role", "Senior role", "Leadership role"]
        )

    def generate_action_plan(self, user_profile: Dict[str, Any]) -> Dict[str, Any]:
        skills = user_profile.get("skills", [])
        missing_skills = user_profile.get("missing_skills", [])
        career_goal = user_profile.get("career_goal", "general professional development")

        return {
            "career_goal": career_goal,
            "current_skills": skills,
            "recommended_skills": self.recommend_skills(missing_skills),
            "growth_path": self.suggest_growth_path(career_goal),
            "next_steps": [
                f"Complete one project applying {skill}" for skill in missing_skills
            ] or ["Continue building expertise in your current skills."]
        }

    # 🔑 This is what app.py expects
    def get_recommendations(self, personality_profile: Dict[str, Any], processed_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate career recommendations based on personality profile and processed answers.
        """
        scores = processed_data.get("scores", {})
        dominant_traits = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:2]

        # Very simple rule-based mapping
        top_careers = []
        if dominant_traits:
            top = dominant_traits[0][0]
            if "1" in top or "2" in top:
                top_careers.append("Software Engineer")
            if "3" in top or "4" in top:
                top_careers.append("UX Designer")
            if "5" in top or "6" in top:
                top_careers.append("Data Scientist")

        if not top_careers:
            top_careers = ["General Professional Roles"]

        return {
            "personality_profile": personality_profile,
            "career_matches": [
                {
                    "career": career,
                    "growth_path": self.suggest_growth_path(career),
                    "resources": self.recommend_skills(["python", "data analysis"])  # sample
                }
                for career in top_careers
            ]
        }
