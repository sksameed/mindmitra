
# data/skills_mapping.py
class SkillsMapping:
    """Maps user responses to skill categories and proficiency levels"""
    
    def __init__(self):
        self.skill_categories = self._initialize_skill_categories()
        self.skill_weights = self._initialize_skill_weights()
    
    def _initialize_skill_categories(self):
        """Initialize skill category mappings"""
        return {
            'technical_skills': {
                'programming': ['Python', 'Java', 'JavaScript', 'C++', 'SQL', 'HTML/CSS'],
                'data_analysis': ['Statistics', 'Excel', 'R', 'Data Visualization', 'Machine Learning'],
                'design': ['Graphic Design', 'UX/UI Design', 'Adobe Creative Suite', 'Figma'],
                'digital_marketing': ['SEO', 'Social Media', 'Google Analytics', 'Content Marketing']
            },
            'soft_skills': {
                'communication': ['Public Speaking', 'Writing', 'Presentation', 'Interpersonal'],
                'leadership': ['Team Management', 'Project Management', 'Strategic Planning', 'Mentoring'],
                'analytical': ['Problem Solving', 'Critical Thinking', 'Research', 'Decision Making'],
                'creative': ['Innovation', 'Brainstorming', 'Creative Writing', 'Art']
            },
            'industry_knowledge': {
                'business': ['Finance', 'Marketing', 'Sales', 'Operations', 'Strategy'],
                'healthcare': ['Medical Knowledge', 'Patient Care', 'Healthcare Systems'],
                'education': ['Curriculum Development', 'Teaching Methods', 'Educational Technology'],
                'technology': ['Software Development', 'System Administration', 'Cybersecurity']
            }
        }
    
    def _initialize_skill_weights(self):
        """Initialize weights for different skills in career matching"""
        return {
            'programming': 0.9,
            'data_analysis': 0.8,
            'communication': 0.7,
            'leadership': 0.7,
            'design': 0.8,
            'analytical': 0.7,
            'creative': 0.6,
            'business': 0.7,
            'healthcare': 0.9,
            'education': 0.8,
            'technology': 0.8
        }
    
    def map_response_to_skills(self, question_type, response):
        """Map questionnaire response to skills"""
        skill_mappings = {
            'enjoys_programming': {
                'strongly_agree': {'programming': 0.9, 'analytical': 0.7},
                'agree': {'programming': 0.7, 'analytical': 0.5},
                'neutral': {'programming': 0.3},
                'disagree': {},
                'strongly_disagree': {}
            },
            'likes_data_analysis': {
                'strongly_agree': {'data_analysis': 0.9, 'analytical': 0.8},
                'agree': {'data_analysis': 0.7, 'analytical': 0.6},
                'neutral': {'data_analysis': 0.3},
                'disagree': {},
                'strongly_disagree': {}
            },
            'creative_projects': {
                'strongly_agree': {'creative': 0.9, 'design': 0.7},
                'agree': {'creative': 0.7, 'design': 0.5},
                'neutral': {'creative': 0.3},
                'disagree': {},
                'strongly_disagree': {}
            },
            'leading_teams': {
                'strongly_agree': {'leadership': 0.9, 'communication': 0.7},
                'agree': {'leadership': 0.7, 'communication': 0.5},
                'neutral': {'leadership': 0.3},
                'disagree': {},
                'strongly_disagree': {}
            },
            'helping_others': {
                'strongly_agree': {'healthcare': 0.6, 'education': 0.6, 'communication': 0.5},
                'agree': {'healthcare': 0.4, 'education': 0.4, 'communication': 0.3},
                'neutral': {},
                'disagree': {},
                'strongly_disagree': {}
            },
            'business_strategy': {
                'strongly_agree': {'business': 0.9, 'analytical': 0.6},
                'agree': {'business': 0.7, 'analytical': 0.4},
                'neutral': {'business': 0.3},
                'disagree': {},
                'strongly_disagree': {}
            }
        }
        
        return skill_mappings.get(question_type, {}).get(response, {})
    
    def calculate_skill_scores(self, all_responses):
        """Calculate overall skill scores from all responses"""
        skill_scores = {}
        
        for question_id, response in all_responses.items():
            question_type = self._get_question_type(question_id)
            skills = self.map_response_to_skills(question_type, response)
            
            for skill, score in skills.items():
                if skill in skill_scores:
                    skill_scores[skill] = max(skill_scores[skill], score)
                else:
                    skill_scores[skill] = score
        
        return skill_scores
    
    def _get_question_type(self, question_id):
        """Map question ID to question type"""
        question_type_mapping = {
            '0': 'enjoys_programming',
            '1': 'likes_data_analysis',
            '2': 'creative_projects',
            '3': 'leading_teams',
            '4': 'helping_others',
            '5': 'business_strategy',
            # Add more mappings as needed
        }
        return question_type_mapping.get(str(question_id), 'general')
    
    def get_top_skills(self, skill_scores, top_n=10):
        """Get top N skills based on scores"""
        sorted_skills = sorted(skill_scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_skills[:top_n]
    
    def normalize_skill_scores(self, skill_scores):
        """Normalize skill scores to 0-1 range"""
        if not skill_scores:
            return {}
        
        max_score = max(skill_scores.values())
        if max_score == 0:
            return skill_scores
        
        return {skill: score / max_score for skill, score in skill_scores.items()}

