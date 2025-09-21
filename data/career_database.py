
# data/career_database.py
class CareerDatabase:
    """Central database of career information and requirements"""
    
    def __init__(self):
        self.careers = self._initialize_careers()
    
    def _initialize_careers(self):
        """Initialize comprehensive career database"""
        return {
            'software_engineer': {
                'title': 'Software Engineer',
                'category': 'Technology',
                'description': 'Design, develop, and maintain software applications and systems.',
                'requirements': {
                    'education': "Bachelor's degree in Computer Science or related field",
                    'experience': '0-2 years for entry level',
                    'skills': ['Programming', 'Problem Solving', 'Algorithms', 'Data Structures']
                },
                'salary_range': {
                    'entry': (60000, 80000),
                    'mid': (80000, 120000),
                    'senior': (120000, 180000)
                },
                'growth_outlook': 'Excellent (22% growth expected)',
                'work_environment': 'Office/Remote',
                'personality_match': ['analytical', 'logical', 'creative', 'detail-oriented'],
                'skills_required': ['Python', 'Java', 'JavaScript', 'SQL', 'Git', 'Problem Solving'],
                'interests': ['technology', 'problem_solving', 'innovation'],
                'values': ['innovation', 'continuous_learning', 'flexibility'],
                'work_style': ['independent', 'collaborative', 'analytical']
            },
            
            'data_scientist': {
                'title': 'Data Scientist',
                'category': 'Technology/Analytics',
                'description': 'Analyze complex data to help organizations make informed decisions.',
                'requirements': {
                    'education': "Master's degree in Statistics, Mathematics, or Computer Science preferred",
                    'experience': '2-4 years in data analysis',
                    'skills': ['Statistics', 'Machine Learning', 'Data Visualization', 'Programming']
                },
                'salary_range': {
                    'entry': (70000, 90000),
                    'mid': (90000, 130000),
                    'senior': (130000, 200000)
                },
                'growth_outlook': 'Excellent (35% growth expected)',
                'work_environment': 'Office/Remote',
                'personality_match': ['analytical', 'curious', 'methodical', 'innovative'],
                'skills_required': ['Python', 'R', 'SQL', 'Machine Learning', 'Statistics', 'Data Visualization'],
                'interests': ['data', 'research', 'problem_solving', 'technology'],
                'values': ['innovation', 'accuracy', 'continuous_learning'],
                'work_style': ['analytical', 'independent', 'research-oriented']
            },
            
            'marketing_manager': {
                'title': 'Marketing Manager',
                'category': 'Business/Marketing',
                'description': 'Develop and execute marketing strategies to promote products or services.',
                'requirements': {
                    'education': "Bachelor's degree in Marketing, Business, or Communications",
                    'experience': '3-5 years in marketing roles',
                    'skills': ['Strategic Planning', 'Communication', 'Analytics', 'Creativity']
                },
                'salary_range': {
                    'entry': (50000, 65000),
                    'mid': (65000, 95000),
                    'senior': (95000, 150000)
                },
                'growth_outlook': 'Good (10% growth expected)',
                'work_environment': 'Office/Hybrid',
                'personality_match': ['creative', 'outgoing', 'strategic', 'persuasive'],
                'skills_required': ['Digital Marketing', 'Analytics', 'Communication', 'Project Management', 'Creativity'],
                'interests': ['people', 'creativity', 'business', 'communication'],
                'values': ['creativity', 'impact', 'growth', 'collaboration'],
                'work_style': ['collaborative', 'creative', 'strategic']
            },
            
            'ux_designer': {
                'title': 'UX Designer',
                'category': 'Design/Technology',
                'description': 'Design user experiences for digital products and services.',
                'requirements': {
                    'education': "Bachelor's degree in Design, Psychology, or related field",
                    'experience': '1-3 years in design',
                    'skills': ['User Research', 'Prototyping', 'Design Thinking', 'Empathy']
                },
                'salary_range': {
                    'entry': (55000, 75000),
                    'mid': (75000, 105000),
                    'senior': (105000, 140000)
                },
                'growth_outlook': 'Excellent (13% growth expected)',
                'work_environment': 'Office/Remote',
                'personality_match': ['creative', 'empathetic', 'analytical', 'user-focused'],
                'skills_required': ['Figma', 'Sketch', 'User Research', 'Prototyping', 'Design Thinking'],
                'interests': ['design', 'people', 'technology', 'creativity'],
                'values': ['user_focus', 'creativity', 'innovation', 'collaboration'],
                'work_style': ['creative', 'empathetic', 'collaborative']
            },
            
            'financial_analyst': {
                'title': 'Financial Analyst',
                'category': 'Finance',
                'description': 'Analyze financial data to help businesses make investment decisions.',
                'requirements': {
                    'education': "Bachelor's degree in Finance, Economics, or Accounting",
                    'experience': '1-3 years in finance',
                    'skills': ['Financial Modeling', 'Analytics', 'Excel', 'Attention to Detail']
                },
                'salary_range': {
                    'entry': (55000, 70000),
                    'mid': (70000, 95000),
                    'senior': (95000, 130000)
                },
                'growth_outlook': 'Good (6% growth expected)',
                'work_environment': 'Office',
                'personality_match': ['analytical', 'detail-oriented', 'logical', 'methodical'],
                'skills_required': ['Excel', 'Financial Modeling', 'SQL', 'Analytics', 'Accounting'],
                'interests': ['numbers', 'business', 'analysis', 'economics'],
                'values': ['accuracy', 'stability', 'growth', 'achievement'],
                'work_style': ['analytical', 'detail-oriented', 'independent']
            },
            
            'product_manager': {
                'title': 'Product Manager',
                'category': 'Technology/Business',
                'description': 'Guide product development from conception to launch.',
                'requirements': {
                    'education': "Bachelor's degree in Business, Engineering, or related field",
                    'experience': '3-5 years in product or project management',
                    'skills': ['Strategic Thinking', 'Communication', 'Analytics', 'Leadership']
                },
                'salary_range': {
                    'entry': (70000, 90000),
                    'mid': (90000, 130000),
                    'senior': (130000, 180000)
                },
                'growth_outlook': 'Excellent (19% growth expected)',
                'work_environment': 'Office/Hybrid',
                'personality_match': ['strategic', 'leadership', 'analytical', 'communication'],
                'skills_required': ['Product Strategy', 'Analytics', 'Project Management', 'Communication'],
                'interests': ['technology', 'business', 'strategy', 'innovation'],
                'values': ['innovation', 'leadership', 'impact', 'growth'],
                'work_style': ['strategic', 'collaborative', 'leadership']
            },
            
            'teacher': {
                'title': 'Teacher',
                'category': 'Education',
                'description': 'Educate and inspire students in various subjects and grade levels.',
                'requirements': {
                    'education': "Bachelor's degree in Education or subject area, Teaching certification",
                    'experience': 'Student teaching required',
                    'skills': ['Communication', 'Patience', 'Creativity', 'Organization']
                },
                'salary_range': {
                    'entry': (35000, 45000),
                    'mid': (45000, 60000),
                    'senior': (60000, 80000)
                },
                'growth_outlook': 'Good (8% growth expected)',
                'work_environment': 'School/Classroom',
                'personality_match': ['nurturing', 'patient', 'communicative', 'organized'],
                'skills_required': ['Curriculum Development', 'Classroom Management', 'Communication', 'Patience'],
                'interests': ['education', 'people', 'helping_others', 'knowledge'],
                'values': ['making_difference', 'growth', 'service', 'stability'],
                'work_style': ['nurturing', 'organized', 'patient']
            },
            
            'nurse': {
                'title': 'Registered Nurse',
                'category': 'Healthcare',
                'description': 'Provide patient care and support in various healthcare settings.',
                'requirements': {
                    'education': 'Associate or Bachelor degree in Nursing, RN license',
                    'experience': 'Clinical training required',
                    'skills': ['Compassion', 'Communication', 'Critical Thinking', 'Physical Stamina']
                },
                'salary_range': {
                    'entry': (50000, 65000),
                    'mid': (65000, 80000),
                    'senior': (80000, 100000)
                },
                'growth_outlook': 'Excellent (15% growth expected)',
                'work_environment': 'Hospital/Clinic',
                'personality_match': ['caring', 'compassionate', 'detail-oriented', 'resilient'],
                'skills_required': ['Patient Care', 'Medical Knowledge', 'Communication', 'Critical Thinking'],
                'interests': ['healthcare', 'helping_others', 'science', 'people'],
                'values': ['helping_others', 'service', 'stability', 'growth'],
                'work_style': ['caring', 'detail-oriented', 'collaborative']
            }
        }
    
    def get_career(self, career_id):
        """Get specific career information"""
        return self.careers.get(career_id)
    
    def get_all_careers(self):
        """Get all careers in database"""
        return self.careers
    
    def search_careers(self, category=None, keywords=None):
        """Search careers by category or keywords"""
        results = {}
        for career_id, career in self.careers.items():
            if category and career['category'].lower() != category.lower():
                continue
            if keywords:
                career_text = f"{career['title']} {career['description']} {' '.join(career['skills_required'])}".lower()
                if not any(keyword.lower() in career_text for keyword in keywords):
                    continue
            results[career_id] = career
        return results
    
    def get_careers_by_skills(self, skills):
        """Get careers matching specific skills"""
        matching_careers = {}
        for career_id, career in self.careers.items():
            skill_matches = len(set(skills) & set([skill.lower() for skill in career['skills_required']]))
            if skill_matches > 0:
                career_copy = career.copy()
                career_copy['skill_match_count'] = skill_matches
                matching_careers[career_id] = career_copy
        return matching_careers
