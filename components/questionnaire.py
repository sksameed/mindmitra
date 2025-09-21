# components/questionnaire.py
import random
from typing import Dict, List, Any, Optional

class QuestionnaireManager:
    """Manages comprehensive career assessment questionnaire with advanced question logic"""
    
    def __init__(self):
        self.questions = self._initialize_questions()
        self.question_categories = self._initialize_categories()
        self.adaptive_logic = AdaptiveQuestionLogic()
        
    def _initialize_categories(self):
        """Initialize question categories with weights and descriptions"""
        return {
            'personality': {
                'name': 'Personality Traits',
                'description': 'Understanding your core personality characteristics',
                'weight': 0.30,
                'question_count': 15
            },
            'interests': {
                'name': 'Career Interests',
                'description': 'What activities and subjects engage you most',
                'weight': 0.25,
                'question_count': 12
            },
            'skills': {
                'name': 'Skills & Abilities',
                'description': 'Your current and potential skill areas',
                'weight': 0.20,
                'question_count': 10
            },
            'values': {
                'name': 'Work Values',
                'description': 'What matters most to you in a career',
                'weight': 0.15,
                'question_count': 8
            },
            'work_style': {
                'name': 'Work Style Preferences',
                'description': 'Your preferred work environment and approach',
                'weight': 0.10,
                'question_count': 5
            }
        }
    
    def _initialize_questions(self):
        """Initialize comprehensive questionnaire with 50 professionally designed questions"""
        return [
            # PERSONALITY QUESTIONS (0-14) - Big Five Traits
            {
                'id': 0,
                'category': 'personality',
                'trait': 'openness',
                'type': 'likert',
                'question': 'I enjoy exploring new ideas and concepts, even if they seem unconventional.',
                'options': self._get_likert_options(),
                'weight': 0.8
            },
            {
                'id': 1,
                'category': 'personality',
                'trait': 'openness',
                'type': 'likert',
                'question': 'I prefer trying new approaches rather than sticking to proven methods.',
                'options': self._get_likert_options(),
                'weight': 0.7
            },
            {
                'id': 2,
                'category': 'personality',
                'trait': 'conscientiousness',
                'type': 'likert',
                'question': 'I am very organized and like to plan things in advance.',
                'options': self._get_likert_options(),
                'weight': 0.9
            },
            {
                'id': 3,
                'category': 'personality',
                'trait': 'conscientiousness',
                'type': 'likert',
                'question': 'I always complete tasks thoroughly, even when no one is checking my work.',
                'options': self._get_likert_options(),
                'weight': 0.8
            },
            {
                'id': 4,
                'category': 'personality',
                'trait': 'extraversion',
                'type': 'likert',
                'question': 'I feel energized when working with groups of people.',
                'options': self._get_likert_options(),
                'weight': 0.9
            },
            {
                'id': 5,
                'category': 'personality',
                'trait': 'extraversion',
                'type': 'likert',
                'question': 'I often take the lead in group discussions and meetings.',
                'options': self._get_likert_options(),
                'weight': 0.7
            },
            {
                'id': 6,
                'category': 'personality',
                'trait': 'agreeableness',
                'type': 'likert',
                'question': 'I prioritize maintaining harmony in team relationships.',
                'options': self._get_likert_options(),
                'weight': 0.8
            },
            {
                'id': 7,
                'category': 'personality',
                'trait': 'agreeableness',
                'type': 'likert',
                'question': 'I find it easy to trust others and assume positive intentions.',
                'options': self._get_likert_options(),
                'weight': 0.6
            },
            {
                'id': 8,
                'category': 'personality',
                'trait': 'neuroticism',
                'type': 'likert',
                'question': 'I remain calm and composed even in stressful situations.',
                'options': self._get_likert_options(),
                'weight': 0.9,
                'reverse_scored': True  # Higher score = lower neuroticism
            },
            {
                'id': 9,
                'category': 'personality',
                'trait': 'openness',
                'type': 'likert',
                'question': 'I enjoy creative activities like art, music, or writing.',
                'options': self._get_likert_options(),
                'weight': 0.6
            },
            {
                'id': 10,
                'category': 'personality',
                'trait': 'conscientiousness',
                'type': 'likert',
                'question': 'I set high standards for myself and work hard to meet them.',
                'options': self._get_likert_options(),
                'weight': 0.7
            },
            {
                'id': 11,
                'category': 'personality',
                'trait': 'extraversion',
                'type': 'likert',
                'question': 'I prefer working alone rather than in large groups.',
                'options': self._get_likert_options(),
                'weight': 0.8,
                'reverse_scored': True
            },
            {
                'id': 12,
                'category': 'personality',
                'trait': 'agreeableness',
                'type': 'likert',
                'question': 'I enjoy helping others succeed, even if it means less recognition for myself.',
                'options': self._get_likert_options(),
                'weight': 0.9
            },
            {
                'id': 13,
                'category': 'personality',
                'trait': 'neuroticism',
                'type': 'likert',
                'question': 'I worry frequently about making mistakes or failing.',
                'options': self._get_likert_options(),
                'weight': 0.7
            },
            {
                'id': 14,
                'category': 'personality',
                'trait': 'openness',
                'type': 'likert',
                'question': 'I enjoy learning about diverse cultures and perspectives.',
                'options': self._get_likert_options(),
                'weight': 0.5
            },
            
            # INTERESTS QUESTIONS (15-26) - Career Interest Areas
            {
                'id': 15,
                'category': 'interests',
                'interest_area': 'technology',
                'type': 'likert',
                'question': 'I find working with computers and technology fascinating.',
                'options': self._get_likert_options(),
                'weight': 1.0
            },
            {
                'id': 16,
                'category': 'interests',
                'interest_area': 'creative',
                'type': 'likert',
                'question': 'I enjoy creative problem-solving and artistic expression.',
                'options': self._get_likert_options(),
                'weight': 1.0
            },
            {
                'id': 17,
                'category': 'interests',
                'interest_area': 'people',
                'type': 'likert',
                'question': 'I am drawn to careers that involve helping and supporting others.',
                'options': self._get_likert_options(),
                'weight': 1.0
            },
            {
                'id': 18,
                'category': 'interests',
                'interest_area': 'business',
                'type': 'likert',
                'question': 'I am interested in business strategy and entrepreneurship.',
                'options': self._get_likert_options(),
                'weight': 1.0
            },
            {
                'id': 19,
                'category': 'interests',
                'interest_area': 'science',
                'type': 'likert',
                'question': 'I enjoy conducting research and analyzing data to find insights.',
                'options': self._get_likert_options(),
                'weight': 1.0
            },
            {
                'id': 20,
                'category': 'interests',
                'interest_area': 'healthcare',
                'type': 'likert',
                'question': 'I am passionate about health, wellness, and medical care.',
                'options': self._get_likert_options(),
                'weight': 1.0
            },
            {
                'id': 21,
                'category': 'interests',
                'interest_area': 'education',
                'type': 'likert',
                'question': 'I enjoy teaching and sharing knowledge with others.',
                'options': self._get_likert_options(),
                'weight': 1.0
            },
            {
                'id': 22,
                'category': 'interests',
                'interest_area': 'finance',
                'type': 'likert',
                'question': 'I find financial markets and economic analysis interesting.',
                'options': self._get_likert_options(),
                'weight': 1.0
            },
            {
                'id': 23,
                'category': 'interests',
                'interest_area': 'communication',
                'type': 'likert',
                'question': 'I enjoy writing, speaking, and communicating ideas effectively.',
                'options': self._get_likert_options(),
                'weight': 1.0
            },
            {
                'id': 24,
                'category': 'interests',
                'type': 'multiple_choice',
                'question': 'Which type of work environment appeals to you most?',
                'options': [
                    {'value': 'office_traditional', 'text': 'Traditional office with colleagues'},
                    {'value': 'office_modern', 'text': 'Modern, flexible office space'},
                    {'value': 'remote', 'text': 'Remote work from home'},
                    {'value': 'hybrid', 'text': 'Hybrid office and remote'},
                    {'value': 'field', 'text': 'Field work or travel-based'},
                    {'value': 'laboratory', 'text': 'Laboratory or research facility'},
                    {'value': 'healthcare', 'text': 'Hospital or medical facility'}
                ],
                'weight': 0.8
            },
            {
                'id': 25,
                'category': 'interests',
                'type': 'multiple_choice',
                'question': 'What type of work schedule do you prefer?',
                'options': [
                    {'value': 'standard', 'text': 'Standard business hours (9-5)'},
                    {'value': 'flexible', 'text': 'Flexible hours with core requirements'},
                    {'value': 'early', 'text': 'Early morning start'},
                    {'value': 'evening', 'text': 'Evening or night shifts'},
                    {'value': 'varies', 'text': 'Variable schedule based on projects'},
                    {'value': 'seasonal', 'text': 'Seasonal work patterns'}
                ],
                'weight': 0.6
            },
            {
                'id': 26,
                'category': 'interests',
                'interest_area': 'innovation',
                'type': 'likert',
                'question': 'I am excited by cutting-edge technologies and innovations.',
                'options': self._get_likert_options(),
                'weight': 0.9
            },
            
            # SKILLS QUESTIONS (27-36) - Skill Assessment
            {
                'id': 27,
                'category': 'skills',
                'skill_type': 'technical',
                'type': 'self_assessment',
                'question': 'Rate your current level of programming/coding skills:',
                'options': self._get_skill_level_options(),
                'weight': 1.0
            },
            {
                'id': 28,
                'category': 'skills',
                'skill_type': 'analytical',
                'type': 'self_assessment',
                'question': 'Rate your ability to analyze data and identify patterns:',
                'options': self._get_skill_level_options(),
                'weight': 1.0
            },
            {
                'id': 29,
                'category': 'skills',
                'skill_type': 'communication',
                'type': 'self_assessment',
                'question': 'Rate your verbal and written communication skills:',
                'options': self._get_skill_level_options(),
                'weight': 1.0
            },
            {
                'id': 30,
                'category': 'skills',
                'skill_type': 'leadership',
                'type': 'self_assessment',
                'question': 'Rate your leadership and team management abilities:',
                'options': self._get_skill_level_options(),
                'weight': 1.0
            },
            {
                'id': 31,
                'category': 'skills',
                'skill_type': 'creative',
                'type': 'self_assessment',
                'question': 'Rate your creative and design abilities:',
                'options': self._get_skill_level_options(),
                'weight': 1.0
            },
            {
                'id': 32,
                'category': 'skills',
                'skill_type': 'problem_solving',
                'type': 'likert',
                'question': 'I excel at breaking down complex problems into manageable parts.',
                'options': self._get_likert_options(),
                'weight': 0.9
            },
            {
                'id': 33,
                'category': 'skills',
                'skill_type': 'learning',
                'type': 'likert',
                'question': 'I quickly learn new skills and adapt to new technologies.',
                'options': self._get_likert_options(),
                'weight': 0.8
            },
            {
                'id': 34,
                'category': 'skills',
                'skill_type': 'attention_to_detail',
                'type': 'likert',
                'question': 'I consistently catch errors and maintain high accuracy in my work.',
                'options': self._get_likert_options(),
                'weight': 0.7
            },
            {
                'id': 35,
                'category': 'skills',
                'skill_type': 'multitasking',
                'type': 'likert',
                'question': 'I effectively manage multiple projects and deadlines simultaneously.',
                'options': self._get_likert_options(),
                'weight': 0.6
            },
            {
                'id': 36,
                'category': 'skills',
                'type': 'multiple_select',
                'question': 'Which technical tools are you comfortable using? (Select all that apply)',
                'options': [
                    {'value': 'microsoft_office', 'text': 'Microsoft Office Suite'},
                    {'value': 'google_workspace', 'text': 'Google Workspace'},
                    {'value': 'adobe_creative', 'text': 'Adobe Creative Suite'},
                    {'value': 'programming_languages', 'text': 'Programming Languages'},
                    {'value': 'database_tools', 'text': 'Database Management Tools'},
                    {'value': 'analytics_tools', 'text': 'Data Analytics Tools'},
                    {'value': 'design_software', 'text': 'Design Software'},
                    {'value': 'project_management', 'text': 'Project Management Tools'},
                    {'value': 'social_media', 'text': 'Social Media Management'},
                    {'value': 'crm_systems', 'text': 'CRM Systems'}
                ],
                'weight': 0.5
            },
            
            # VALUES QUESTIONS (37-44) - Work Values and Motivations
            {
                'id': 37,
                'category': 'values',
                'type': 'ranking',
                'question': 'Rank these work values in order of importance to you (1 = most important):',
                'options': [
                    {'value': 'high_salary', 'text': 'High salary and financial rewards'},
                    {'value': 'job_security', 'text': 'Job security and stability'},
                    {'value': 'work_life_balance', 'text': 'Work-life balance'},
                    {'value': 'career_growth', 'text': 'Career advancement opportunities'},
                    {'value': 'meaningful_work', 'text': 'Meaningful, impactful work'},
                    {'value': 'creativity', 'text': 'Creative freedom and expression'},
                    {'value': 'autonomy', 'text': 'Independence and autonomy'},
                    {'value': 'recognition', 'text': 'Recognition and prestige'}
                ],
                'weight': 1.0
            },
            {
                'id': 38,
                'category': 'values',
                'value_type': 'impact',
                'type': 'likert',
                'question': 'It is important for me to make a positive impact on society through my work.',
                'options': self._get_likert_options(),
                'weight': 0.9
            },
            {
                'id': 39,
                'category': 'values',
                'value_type': 'innovation',
                'type': 'likert',
                'question': 'I value working in innovative, forward-thinking organizations.',
                'options': self._get_likert_options(),
                'weight': 0.8
            },
            {
                'id': 40,
                'category': 'values',
                'value_type': 'collaboration',
                'type': 'likert',
                'question': 'I prefer collaborative environments over competitive ones.',
                'options': self._get_likert_options(),
                'weight': 0.7
            },
            {
                'id': 41,
                'category': 'values',
                'value_type': 'stability',
                'type': 'likert',
                'question': 'I value predictability and routine in my work environment.',
                'options': self._get_likert_options(),
                'weight': 0.6
            },
            {
                'id': 42,
                'category': 'values',
                'value_type': 'learning',
                'type': 'likert',
                'question': 'Continuous learning and professional development are essential to me.',
                'options': self._get_likert_options(),
                'weight': 0.8
            },
            {
                'id': 43,
                'category': 'values',
                'type': 'multiple_choice',
                'question': 'What motivates you most in your career?',
                'options': [
                    {'value': 'achievement', 'text': 'Achieving challenging goals and objectives'},
                    {'value': 'service', 'text': 'Serving others and making a difference'},
                    {'value': 'expertise', 'text': 'Becoming an expert in my field'},
                    {'value': 'leadership', 'text': 'Leading teams and organizations'},
                    {'value': 'creativity', 'text': 'Creating something new and original'},
                    {'value': 'variety', 'text': 'Having variety and new experiences'}
                ],
                'weight': 0.9
            },
            {
                'id': 44,
                'category': 'values',
                'type': 'multiple_choice',
                'question': 'How important is salary compared to other job factors?',
                'options': [
                    {'value': 'primary', 'text': 'Primary consideration - most important factor'},
                    {'value': 'important', 'text': 'Important but not the only factor'},
                    {'value': 'moderate', 'text': 'Moderately important'},
                    {'value': 'secondary', 'text': 'Secondary to other factors like fulfillment'},
                    {'value': 'minimal', 'text': 'Not a major consideration'}
                ],
                'weight': 0.7
            },
            
            # WORK STYLE QUESTIONS (45-49) - Work Preferences
            {
                'id': 45,
                'category': 'work_style',
                'style_type': 'pace',
                'type': 'likert',
                'question': 'I prefer fast-paced, dynamic work environments over steady, methodical ones.',
                'options': self._get_likert_options(),
                'weight': 0.8
            },
            {
                'id': 46,
                'category': 'work_style',
                'style_type': 'structure',
                'type': 'likert',
                'question': 'I work better with clear guidelines and structured processes.',
                'options': self._get_likert_options(),
                'weight': 0.7
            },
            {
                'id': 47,
                'category': 'work_style',
                'style_type': 'collaboration',
                'type': 'multiple_choice',
                'question': 'How do you prefer to work on projects?',
                'options': [
                    {'value': 'individual', 'text': 'Independently with minimal supervision'},
                    {'value': 'small_team', 'text': 'In small teams (2-4 people)'},
                    {'value': 'large_team', 'text': 'In larger teams (5+ people)'},
                    {'value': 'leadership', 'text': 'Leading and directing others'},
                    {'value': 'flexible', 'text': 'Flexible - depends on the project'}
                ],
                'weight': 0.9
            },
            {
                'id': 48,
                'category': 'work_style',
                'style_type': 'risk_tolerance',
                'type': 'likert',
                'question': 'I am comfortable taking calculated risks for potentially greater rewards.',
                'options': self._get_likert_options(),
                'weight': 0.6
            },
            {
                'id': 49,
                'category': 'work_style',
                'style_type': 'feedback',
                'type': 'multiple_choice',
                'question': 'How often do you prefer to receive feedback on your work?',
                'options': [
                    {'value': 'daily', 'text': 'Daily check-ins and feedback'},
                    {'value': 'weekly', 'text': 'Weekly progress reviews'},
                    {'value': 'monthly', 'text': 'Monthly formal reviews'},
                    {'value': 'project_based', 'text': 'At major project milestones'},
                    {'value': 'minimal', 'text': 'Minimal feedback - prefer autonomy'}
                ],
                'weight': 0.5
            }
        ]
    
    def _get_likert_options(self):
        """Standard 5-point Likert scale options"""
        return [
            {'value': 'strongly_disagree', 'text': 'Strongly Disagree'},
            {'value': 'disagree', 'text': 'Disagree'},
            {'value': 'neutral', 'text': 'Neutral'},
            {'value': 'agree', 'text': 'Agree'},
            {'value': 'strongly_agree', 'text': 'Strongly Agree'}
        ]
    
    def _get_skill_level_options(self):
        """Skill proficiency level options"""
        return [
            {'value': 'none', 'text': 'No experience'},
            {'value': 'beginner', 'text': 'Beginner - Basic knowledge'},
            {'value': 'intermediate', 'text': 'Intermediate - Some experience'},
            {'value': 'advanced', 'text': 'Advanced - Extensive experience'},
            {'value': 'expert', 'text': 'Expert - Could teach others'}
        ]
    
    def get_question(self, question_id: int) -> Dict[str, Any]:
        """Get specific question by ID with enhanced metadata"""
        for question in self.questions:
            if question['id'] == question_id:
                # Add dynamic metadata
                enhanced_question = question.copy()
                enhanced_question['category_info'] = self.question_categories[question['category']]
                enhanced_question['progress_info'] = self._calculate_progress_info(question_id)
                
                # Add contextual hints for better user experience
                if question['type'] == 'likert':
                    enhanced_question['instruction'] = "Please indicate how much you agree with this statement:"
                elif question['type'] == 'ranking':
                    enhanced_question['instruction'] = "Drag and drop to rank these items in order of preference:"
                elif question['type'] == 'multiple_select':
                    enhanced_question['instruction'] = "Select all options that apply to you:"
                elif question['type'] == 'self_assessment':
                    enhanced_question['instruction'] = "Honestly assess your current ability level:"
                
                return enhanced_question
        
        raise ValueError(f"Question with ID {question_id} not found")
    
    def _calculate_progress_info(self, question_id: int) -> Dict[str, Any]:
        """Calculate progress information for the question"""
        total_questions = len(self.questions)
        current_category = self.questions[question_id]['category']
        
        # Calculate category progress
        category_questions = [q for q in self.questions if q['category'] == current_category]
        category_position = len([q for q in category_questions if q['id'] <= question_id])
        
        return {
            'overall_progress': ((question_id + 1) / total_questions) * 100,
            'category_progress': (category_position / len(category_questions)) * 100,
            'questions_remaining': total_questions - question_id - 1,
            'current_category': current_category,
            'category_name': self.question_categories[current_category]['name']
        }
    
    def get_total_questions(self) -> int:
        """Get total number of questions"""
        return len(self.questions)
    
    def get_questions_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Get all questions in a specific category"""
        return [q for q in self.questions if q['category'] == category]
    
    def get_category_info(self, category: str) -> Dict[str, Any]:
        """Get information about a specific category"""
        return self.question_categories.get(category, {})
    
    def validate_response(self, question_id: int, response: Any) -> Dict[str, Any]:
        """Validate user response for a question with detailed feedback"""
        question = self.get_question(question_id)
        validation_result = {
            'is_valid': False,
            'error_message': '',
            'processed_response': None,
            'confidence_score': 1.0
        }
        
        question_type = question['type']
        
        if question_type == 'likert':
            valid_values = [option['value'] for option in question['options']]
            if response in valid_values:
                validation_result['is_valid'] = True
                validation_result['processed_response'] = response
                # Lower confidence for neutral responses
                if response == 'neutral':
                    validation_result['confidence_score'] = 0.7
            else:
                validation_result['error_message'] = f"Response must be one of: {', '.join(valid_values)}"
        
        elif question_type in ['multiple_choice', 'self_assessment']:
            valid_values = [option['value'] for option in question['options']]
            if response in valid_values:
                validation_result['is_valid'] = True
                validation_result['processed_response'] = response
            else:
                validation_result['error_message'] = f"Response must be one of: {', '.join(valid_values)}"
        
        elif question_type == 'multiple_select':
            if isinstance(response, list):
                valid_values = [option['value'] for option in question['options']]
                if all(r in valid_values for r in response):
                    validation_result['is_valid'] = True
                    validation_result['processed_response'] = response
                    # Higher confidence for multiple selections
                    validation_result['confidence_score'] = min(1.0, 0.8 + len(response) * 0.1)
                else:
                    validation_result['error_message'] = "All selected options must be valid"
            else:
                validation_result['error_message'] = "Response must be a list of values"
        
        elif question_type == 'ranking':
            if isinstance(response, list):
                valid_values = [option['value'] for option in question['options']]
                if (len(response) == len(valid_values) and 
                    set(response) == set(valid_values)):
                    validation_result['is_valid'] = True
                    validation_result['processed_response'] = response
                    validation_result['confidence_score'] = 0.95  # High confidence for complete rankings
                else:
                    validation_result['error_message'] = "Must rank all provided options exactly once"
            else:
                validation_result['error_message'] = "Response must be a ranked list of all options"
        
        return validation_result
    
    def get_next_question_id(self, current_id: int, user_responses: Dict[int, Any]) -> Optional[int]:
        """Get next question ID with adaptive logic"""
        return self.adaptive_logic.get_next_question(current_id, user_responses, self.questions)
    
    def get_assessment_completion_status(self, user_responses: Dict[int, Any]) -> Dict[str, Any]:
        """Get detailed completion status of the assessment"""
        total_questions = len(self.questions)
        answered_questions = len(user_responses)
        
        # Calculate category completion
        category_completion = {}
        for category, info in self.question_categories.items():
            category_questions = [q['id'] for q in self.questions if q['category'] == category]
            answered_in_category = len([qid for qid in category_questions if qid in user_responses])
            category_completion[category] = {
                'answered': answered_in_category,
                'total': len(category_questions),
                'percentage': (answered_in_category / len(category_questions)) * 100,
                'name': info['name']
            }
        
        # Calculate confidence score based on response quality
        confidence_scores = []
        for question_id, response in user_responses.items():
            validation = self.validate_response(question_id, response)
            if validation['is_valid']:
                confidence_scores.append(validation['confidence_score'])
        
        avg_confidence = sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0
        
        # Determine if assessment is complete enough for results
        min_completion_threshold = 0.8  # 80% minimum completion
        is_complete_enough = (answered_questions / total_questions) >= min_completion_threshold
        
        # Check if all categories have minimum representation
        category_min_threshold = 0.6  # 60% minimum per category
        all_categories_represented = all(
            comp['percentage'] >= category_min_threshold * 100
            for comp in category_completion.values()
        )
        
        return {
            'total_questions': total_questions,
            'answered_questions': answered_questions,
            'completion_percentage': (answered_questions / total_questions) * 100,
            'category_completion': category_completion,
            'average_confidence': avg_confidence,
            'is_complete_enough': is_complete_enough and all_categories_represented,
            'all_categories_represented': all_categories_represented
        }
