# data/personality_traits.py
class PersonalityTraits:
    """Defines personality traits and their mappings to careers"""
    
    def __init__(self):
        self.trait_definitions = self._initialize_traits()
        self.career_trait_mappings = self._initialize_career_mappings()
    
    def _initialize_traits(self):
        """Initialize personality trait definitions"""
        return {
            'openness': {
                'name': 'Openness to Experience',
                'description': 'Appreciation for art, emotion, adventure, unusual ideas, curiosity, and variety of experience',
                'high_characteristics': ['Creative', 'Imaginative', 'Open to new experiences', 'Intellectually curious'],
                'low_characteristics': ['Practical', 'Conventional', 'Prefers routine', 'Traditional'],
                'careers_high': ['artist', 'researcher', 'entrepreneur', 'designer', 'writer'],
                'careers_low': ['accountant', 'administrator', 'technician', 'operator']
            },
            'conscientiousness': {
                'name': 'Conscientiousness',
                'description': 'Tendency to be organized, dependable, and show self-discipline',
                'high_characteristics': ['Organized', 'Responsible', 'Dependable', 'Persistent', 'Detail-oriented'],
                'low_characteristics': ['Spontaneous', 'Flexible', 'Casual', 'Adaptable'],
                'careers_high': ['project_manager', 'accountant', 'surgeon', 'lawyer', 'engineer'],
                'careers_low': ['artist', 'salesperson', 'entertainer', 'journalist']
            },
            'extraversion': {
                'name': 'Extraversion',
                'description': 'Energy from interacting with people and the external world',
                'high_characteristics': ['Outgoing', 'Social', 'Talkative', 'Assertive', 'Energetic'],
                'low_characteristics': ['Reserved', 'Independent', 'Reflective', 'Quiet'],
                'careers_high': ['salesperson', 'teacher', 'manager', 'consultant', 'politician'],
                'careers_low': ['programmer', 'researcher', 'writer', 'analyst', 'technician']
            },
            'agreeableness': {
                'name': 'Agreeableness',
                'description': 'Tendency to be compassionate and cooperative toward others',
                'high_characteristics': ['Helpful', 'Trusting', 'Empathetic', 'Cooperative', 'Modest'],
                'low_characteristics': ['Competitive', 'Critical', 'Challenging', 'Detached'],
                'careers_high': ['counselor', 'teacher', 'nurse', 'social_worker', 'therapist'],
                'careers_low': ['lawyer', 'executive', 'scientist', 'critic', 'military_officer']
            },
            'neuroticism': {
                'name': 'Emotional Stability',
                'description': 'Tendency toward emotional stability and even-temperedness',
                'high_characteristics': ['Calm', 'Relaxed', 'Secure', 'Optimistic', 'Stress-resistant'],
                'low_characteristics': ['Anxious', 'Temperamental', 'Self-conscious', 'Emotional'],
                'careers_high': ['pilot', 'surgeon', 'executive', 'emergency_responder', 'military'],
                'careers_low': ['artist', 'writer', 'researcher', 'analyst']
            }
        }
    
    def _initialize_career_mappings(self):
        """Initialize mappings between personality traits and careers"""
        return {
            'software_engineer': {
                'openness': 0.7,
                'conscientiousness': 0.8,
                'extraversion': 0.3,
                'agreeableness': 0.5,
                'neuroticism': 0.7
            },
            'data_scientist': {
                'openness': 0.8,
                'conscientiousness': 0.7,
                'extraversion': 0.4,
                'agreeableness': 0.5,
                'neuroticism': 0.6
            },
            'marketing_manager': {
                'openness': 0.6,
                'conscientiousness': 0.7,
                'extraversion': 0.8,
                'agreeableness': 0.6,
                'neuroticism': 0.7
            },
            'ux_designer': {
                'openness': 0.9,
                'conscientiousness': 0.6,
                'extraversion': 0.5,
                'agreeableness': 0.7,
                'neuroticism': 0.6
            },
            'financial_analyst': {
                'openness': 0.4,
                'conscientiousness': 0.9,
                'extraversion': 0.3,
                'agreeableness': 0.4,
                'neuroticism': 0.8
            },
            'product_manager': {
                'openness': 0.7,
                'conscientiousness': 0.8,
                'extraversion': 0.7,
                'agreeableness': 0.6,
                'neuroticism': 0.7
            },
            'teacher': {
                'openness': 0.6,
                'conscientiousness': 0.7,
                'extraversion': 0.7,
                'agreeableness': 0.8,
                'neuroticism': 0.6
            },
            'nurse': {
                'openness': 0.5,
                'conscientiousness': 0.8,
                'extraversion': 0.6,
                'agreeableness': 0.9,
                'neuroticism': 0.7
            },
            'graphic_designer': {
                'openness': 0.9,
                'conscientiousness': 0.5,
                'extraversion': 0.4,
                'agreeableness': 0.6,
                'neuroticism': 0.5
            },
            'sales_manager': {
                'openness': 0.6,
                'conscientiousness': 0.6,
                'extraversion': 0.9,
                'agreeableness': 0.7,
                'neuroticism': 0.8
            },
            'research_scientist': {
                'openness': 0.8,
                'conscientiousness': 0.8,
                'extraversion': 0.3,
                'agreeableness': 0.4,
                'neuroticism': 0.6
            },
            'human_resources_manager': {
                'openness': 0.5,
                'conscientiousness': 0.7,
                'extraversion': 0.8,
                'agreeableness': 0.8,
                'neuroticism': 0.7
            },
            'accountant': {
                'openness': 0.3,
                'conscientiousness': 0.9,
                'extraversion': 0.3,
                'agreeableness': 0.5,
                'neuroticism': 0.8
            },
            'lawyer': {
                'openness': 0.5,
                'conscientiousness': 0.8,
                'extraversion': 0.7,
                'agreeableness': 0.3,
                'neuroticism': 0.8
            },
            'psychologist': {
                'openness': 0.7,
                'conscientiousness': 0.7,
                'extraversion': 0.5,
                'agreeableness': 0.9,
                'neuroticism': 0.6
            },
            'architect': {
                'openness': 0.8,
                'conscientiousness': 0.7,
                'extraversion': 0.4,
                'agreeableness': 0.5,
                'neuroticism': 0.6
            },
            'journalist': {
                'openness': 0.8,
                'conscientiousness': 0.6,
                'extraversion': 0.7,
                'agreeableness': 0.6,
                'neuroticism': 0.5
            },
            'chef': {
                'openness': 0.7,
                'conscientiousness': 0.6,
                'extraversion': 0.5,
                'agreeableness': 0.6,
                'neuroticism': 0.7
            },
            'doctor': {
                'openness': 0.6,
                'conscientiousness': 0.9,
                'extraversion': 0.6,
                'agreeableness': 0.8,
                'neuroticism': 0.8
            },
            'entrepreneur': {
                'openness': 0.9,
                'conscientiousness': 0.6,
                'extraversion': 0.8,
                'agreeableness': 0.5,
                'neuroticism': 0.8
            }
        }
    
    def calculate_personality_scores(self, responses):
        """Calculate Big Five personality scores from responses"""
        trait_scores = {
            'openness': 0,
            'conscientiousness': 0,
            'extraversion': 0,
            'agreeableness': 0,
            'neuroticism': 0
        }
        
        # Question mappings to traits - expanded version
        question_trait_mapping = {
            '0': {'openness': 0.3, 'conscientiousness': 0.2},  # Technology interest
            '1': {'conscientiousness': 0.4, 'openness': 0.3},  # Data analysis
            '2': {'openness': 0.6, 'extraversion': 0.1},      # Creative activities
            '3': {'extraversion': 0.5, 'agreeableness': 0.3}, # Leadership
            '4': {'agreeableness': 0.5, 'conscientiousness': 0.2}, # Helping others
            '5': {'extraversion': -0.4, 'conscientiousness': 0.2}, # Independent work
            '6': {'openness': 0.2, 'extraversion': 0.1},      # Work environment
            '7': {'conscientiousness': 0.3, 'neuroticism': 0.2}, # Work values
            '8': {'extraversion': 0.3, 'agreeableness': 0.2}, # Communication skills
            '9': {'extraversion': 0.6, 'agreeableness': 0.3}, # Networking
            '10': {'conscientiousness': 0.4, 'neuroticism': 0.2}, # Organization
            '11': {'openness': 0.5, 'conscientiousness': 0.2}, # Problem solving
            '12': {'agreeableness': 0.4, 'extraversion': 0.3}, # Team work
            '13': {'neuroticism': 0.4, 'conscientiousness': 0.2}, # Stress handling
            '14': {'openness': 0.4, 'extraversion': 0.2},     # New experiences
            '15': {'conscientiousness': 0.5, 'neuroticism': 0.2}, # Deadlines
            '16': {'extraversion': 0.5, 'agreeableness': 0.2}, # Social situations
            '17': {'openness': 0.3, 'conscientiousness': 0.4}, # Routine vs variety
            '18': {'agreeableness': 0.5, 'extraversion': 0.2}, # Conflict resolution
            '19': {'conscientiousness': 0.4, 'openness': 0.2}  # Detail orientation
        }
        
        response_values = {
            'strongly_disagree': 1,
            'disagree': 2,
            'neutral': 3,
            'agree': 4,
            'strongly_agree': 5
        }
        
        for question_id, response in responses.items():
            if str(question_id) in question_trait_mapping:
                response_value = response_values.get(response, 3)
                traits = question_trait_mapping[str(question_id)]
                
                for trait, weight in traits.items():
                    # Convert 1-5 scale to -2 to +2, then apply weight
                    normalized_response = (response_value - 3) * weight
                    trait_scores[trait] += normalized_response
        
        # Normalize scores to 0-1 range
        max_possible_score = 2.0  # Maximum possible accumulated score
        min_possible_score = -2.0  # Minimum possible accumulated score
        
        for trait in trait_scores:
            # Normalize from [-2, 2] to [0, 1]
            normalized_score = (trait_scores[trait] - min_possible_score) / (max_possible_score - min_possible_score)
            trait_scores[trait] = max(0, min(1, normalized_score))
        
        return trait_scores
    
    def get_personality_profile(self, trait_scores):
        """Get personality profile description"""
        profile = {
            'scores': trait_scores,
            'primary_traits': [],
            'description': '',
            'strengths': [],
            'considerations': [],
            'work_preferences': {}
        }
        
        # Identify primary traits (scores > 0.6)
        for trait, score in trait_scores.items():
            if score > 0.6:
                profile['primary_traits'].append(trait)
        
        # Generate description based on scores
        descriptions = []
        strengths = []
        considerations = []
        
        if trait_scores['openness'] > 0.6:
            descriptions.append("creative and open to new experiences")
            strengths.append("Innovation and creative problem-solving")
        elif trait_scores['openness'] < 0.4:
            descriptions.append("practical and detail-focused")
            strengths.append("Attention to detail and systematic thinking")
            
        if trait_scores['conscientiousness'] > 0.6:
            descriptions.append("organized and reliable")
            strengths.append("Strong work ethic and dependability")
        elif trait_scores['conscientiousness'] < 0.4:
            descriptions.append("flexible and adaptable")
            considerations.append("May benefit from structured environments")
            
        if trait_scores['extraversion'] > 0.6:
            descriptions.append("outgoing and energetic")
            strengths.append("Strong communication and leadership skills")
        elif trait_scores['extraversion'] < 0.4:
            descriptions.append("thoughtful and independent")
            strengths.append("Deep focus and analytical thinking")
            
        if trait_scores['agreeableness'] > 0.6:
            descriptions.append("cooperative and trusting")
            strengths.append("Team collaboration and empathy")
        elif trait_scores['agreeableness'] < 0.4:
            descriptions.append("assertive and competitive")
            strengths.append("Strategic thinking and negotiation")
            
        if trait_scores['neuroticism'] > 0.6:
            descriptions.append("emotionally stable and calm")
            strengths.append("Stress management and composure")
        elif trait_scores['neuroticism'] < 0.4:
            descriptions.append("emotionally sensitive and reactive")
            considerations.append("May benefit from stress management techniques")
        
        profile['description'] = f"You are {', '.join(descriptions)}."
        profile['strengths'] = strengths
        profile['considerations'] = considerations
        profile['work_preferences'] = self._generate_work_preferences(trait_scores)
        
        return profile
    
    def _generate_work_preferences(self, trait_scores):
        """Generate work environment preferences based on personality"""
        preferences = {}
        
        # Work environment preferences
        if trait_scores['extraversion'] > 0.6:
            preferences['environment'] = 'Collaborative, team-oriented environments'
        else:
            preferences['environment'] = 'Quiet, focused work spaces'
            
        # Task preferences
        if trait_scores['openness'] > 0.6:
            preferences['tasks'] = 'Varied, creative, and innovative projects'
        else:
            preferences['tasks'] = 'Structured, well-defined assignments'
            
        # Management style preferences
        if trait_scores['agreeableness'] > 0.6:
            preferences['management'] = 'Supportive, collaborative leadership'
        else:
            preferences['management'] = 'Direct, results-oriented leadership'
            
        # Work pace preferences
        if trait_scores['conscientiousness'] > 0.6:
            preferences['pace'] = 'Planned, deadline-driven work'
        else:
            preferences['pace'] = 'Flexible, adaptable schedules'
            
        return preferences
    
    def match_careers_to_personality(self, personality_scores, career_database):
        """Match careers based on personality scores"""
        career_matches = {}
        
        for career_id, career_traits in self.career_trait_mappings.items():
            if career_id in career_database:
                # Calculate personality match score using weighted differences
                match_score = 0
                trait_weights = {
                    'openness': 0.20,
                    'conscientiousness': 0.25,
                    'extraversion': 0.20,
                    'agreeableness': 0.20,
                    'neuroticism': 0.15
                }
                
                for trait, career_requirement in career_traits.items():
                    user_score = personality_scores.get(trait, 0.5)
                    # Calculate how well user matches career requirement
                    trait_difference = abs(user_score - career_requirement)
                    trait_match = 1 - trait_difference
                    weighted_match = trait_match * trait_weights.get(trait, 0.2)
                    match_score += weighted_match
                
                career_matches[career_id] = {
                    'match_score': match_score,
                    'career_info': career_database[career_id],
                    'personality_fit': self._analyze_personality_fit(
                        personality_scores, career_traits
                    )
                }
        
        return career_matches
    
    def _analyze_personality_fit(self, user_scores, career_requirements):
        """Analyze how user personality fits with career requirements"""
        fit_analysis = {
            'strong_matches': [],
            'good_matches': [],
            'potential_challenges': [],
            'development_areas': []
        }
        
        for trait, required_level in career_requirements.items():
            user_level = user_scores.get(trait, 0.5)
            difference = abs(user_level - required_level)
            
            if difference <= 0.1:
                fit_analysis['strong_matches'].append(trait)
            elif difference <= 0.3:
                fit_analysis['good_matches'].append(trait)
            elif difference > 0.5:
                fit_analysis['potential_challenges'].append(trait)
                if user_level < required_level:
                    fit_analysis['development_areas'].append(trait)
        
        return fit_analysis
    
    def get_trait_description(self, trait, score):
        """Get detailed description for a specific trait score"""
        if trait not in self.trait_definitions:
            return "Unknown trait"
            
        trait_def = self.trait_definitions[trait]
        
        if score > 0.7:
            return {
                'level': 'High',
                'description': trait_def['description'],
                'characteristics': trait_def['high_characteristics'],
                'career_implications': f"Well-suited for {', '.join(trait_def['careers_high'])}"
            }
        elif score < 0.3:
            return {
                'level': 'Low',
                'description': trait_def['description'],
                'characteristics': trait_def['low_characteristics'],
                'career_implications': f"Well-suited for {', '.join(trait_def['careers_low'])}"
            }
        else:
            return {
                'level': 'Moderate',
                'description': trait_def['description'],
                'characteristics': trait_def['high_characteristics'][:2] + trait_def['low_characteristics'][:2],
                'career_implications': "Flexible across various career types"
            }
    
    def generate_development_recommendations(self, personality_scores):
        """Generate personality development recommendations"""
        recommendations = []
        
        for trait, score in personality_scores.items():
            if trait == 'conscientiousness' and score < 0.4:
                recommendations.append({
                    'trait': 'Conscientiousness',
                    'suggestion': 'Practice time management and organizational skills',
                    'activities': ['Use task management apps', 'Set daily routines', 'Break large tasks into smaller steps']
                })
            elif trait == 'extraversion' and score < 0.4:
                recommendations.append({
                    'trait': 'Extraversion',
                    'suggestion': 'Gradually build communication and social skills',
                    'activities': ['Join professional groups', 'Practice public speaking', 'Participate in team activities']
                })
            elif trait == 'neuroticism' and score < 0.4:
                recommendations.append({
                    'trait': 'Emotional Stability',
                    'suggestion': 'Develop stress management and emotional regulation skills',
                    'activities': ['Practice mindfulness', 'Learn relaxation techniques', 'Seek feedback on stress reactions']
                })
        
        return recommendations