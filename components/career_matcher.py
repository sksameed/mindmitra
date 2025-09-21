from data.career_database import CareerDatabase
from data.personality_traits import PersonalityTraits
from data.skills_mapping import SkillsMapping
import math
import statistics


class CareerMatcher:
    """Matches user profiles with suitable careers using advanced algorithms"""

    def __init__(self):
        self.career_db = CareerDatabase()
        self.personality_traits = PersonalityTraits()
        self.skills_mapping = SkillsMapping()
        self.matching_weights = {
            'personality': 0.35,
            'skills': 0.25,
            'interests': 0.20,
            'values': 0.15,
            'work_style': 0.05
        }

    def analyze_personality(self, processed_data):
        """Analyze user personality from processed data"""
        personality_scores = self.personality_traits.calculate_personality_scores(
            processed_data.get('responses', {})
        )
        personality_profile = self.personality_traits.get_personality_profile(personality_scores)
        return personality_profile

    def calculate_career_matches(self, personality_profile, processed_data):
        """Calculate comprehensive match scores for all careers"""
        career_matches = {}
        all_careers = self.career_db.get_all_careers()

        # Extract data components
        skill_scores = processed_data.get('skills', {})
        interests = processed_data.get('interests', [])
        values = processed_data.get('values', [])
        work_style = processed_data.get('work_style', {})

        for career_id, career_info in all_careers.items():
            match_score = self._calculate_individual_match(
                career_id, career_info, personality_profile,
                skill_scores, interests, values, work_style
            )

            if match_score > 0.25:  # Only include careers with reasonable matches
                career_matches[career_id] = {
                    'career_info': career_info,
                    'match_score': match_score,
                    'match_breakdown': self._get_detailed_match_breakdown(
                        career_info, personality_profile, skill_scores,
                        interests, values, work_style
                    ),
                    'confidence_level': self._calculate_confidence_level(
                        match_score, career_info
                    ),
                    'growth_potential': self._calculate_growth_potential(
                        career_info, skill_scores
                    )
                }

        return career_matches

    # ---------- Core Match Calculations ----------

    def _calculate_individual_match(self, career_id, career_info, personality_profile,
                                    skill_scores, interests, values, work_style):
        """Calculate comprehensive match score for individual career"""

        # Component scores
        personality_match = self._calculate_personality_match(
            career_id, personality_profile['scores']
        )
        skills_match = self._calculate_skills_match(
            career_info.get('skills_required', []), skill_scores
        )
        interests_match = self._calculate_interests_match(
            career_info.get('interests', []), interests
        )
        values_match = self._calculate_values_match(
            career_info.get('values', []), values
        )
        work_style_match = self._calculate_work_style_match(
            career_info.get('work_style', []), work_style
        )

        # Calculate weighted total with dynamic weight adjustment
        weights = self._adjust_weights_dynamically(
            personality_match, skills_match, interests_match,
            values_match, work_style_match
        )

        total_match = (
            personality_match * weights['personality'] +
            skills_match * weights['skills'] +
            interests_match * weights['interests'] +
            values_match * weights['values'] +
            work_style_match * weights['work_style']
        )

        # Apply career-specific bonuses
        total_match = self._apply_career_bonuses(total_match, career_info, skill_scores)

        return min(1.0, max(0.0, total_match))

    def _calculate_personality_match(self, career_id, user_personality):
        """Calculate personality compatibility score with advanced matching"""
        career_traits = self.personality_traits.career_trait_mappings.get(career_id, {})

        if not career_traits:
            return 0.5  # Neutral match if no data

        total_match = 0
        trait_importance = {
            'conscientiousness': 1.2,
            'openness': 1.1,
            'extraversion': 1.0,
            'agreeableness': 1.0,
            'neuroticism': 0.9
        }

        total_weight = 0
        for trait, required_level in career_traits.items():
            user_level = user_personality.get(trait, 0.5)

            # Calculate match with tolerance
            difference = abs(user_level - required_level)
            if difference <= 0.1:
                trait_match = 1.0
            elif difference <= 0.2:
                trait_match = 0.8
            elif difference <= 0.4:
                trait_match = 0.6
            else:
                trait_match = max(0.2, 1 - difference)

            weight = trait_importance.get(trait, 1.0)
            total_match += trait_match * weight
            total_weight += weight

        return total_match / total_weight if total_weight > 0 else 0.5

    def _calculate_skills_match(self, required_skills, user_skills):
        """Calculate skills compatibility with skill level weighting"""
        if not required_skills:
            return 0.5

        total_match = 0
        matched_skills = 0

        for required_skill in required_skills:
            best_match = 0
            skill_lower = required_skill.lower()

            for user_skill, proficiency in user_skills.items():
                if self._skills_are_related(skill_lower, user_skill.lower()):
                    match_strength = self._calculate_skill_similarity(skill_lower, user_skill.lower())
                    weighted_match = match_strength * proficiency
                    best_match = max(best_match, weighted_match)

            total_match += best_match
            if best_match > 0.3:
                matched_skills += 1

        base_score = total_match / len(required_skills)
        coverage_bonus = matched_skills / len(required_skills) * 0.2

        return min(1.0, base_score + coverage_bonus)

    def _skills_are_related(self, skill1, skill2):
        """Check if two skills are related"""
        if skill1 == skill2 or skill1 in skill2 or skill2 in skill1:
            return True

        skill_relations = {
            'python': ['programming', 'coding', 'software development'],
            'javascript': ['web development', 'frontend', 'programming'],
            'communication': ['presentation', 'writing', 'interpersonal'],
            'leadership': ['management', 'team lead', 'supervision'],
            'analytics': ['analysis', 'data analysis', 'statistics'],
            'design': ['creative', 'visual design', 'ui/ux'],
            'problem solving': ['critical thinking', 'analytical', 'troubleshooting']
        }

        for base_skill, related in skill_relations.items():
            if base_skill in skill1 and any(rel in skill2 for rel in related):
                return True
            if base_skill in skill2 and any(rel in skill1 for rel in related):
                return True

        return False

    def _calculate_skill_similarity(self, skill1, skill2):
        if skill1 == skill2:
            return 1.0
        elif skill1 in skill2 or skill2 in skill1:
            return 0.8
        else:
            return 0.6

    def _calculate_interests_match(self, career_interests, user_interests):
        if not career_interests or not user_interests:
            return 0.5

        career_set = set(career_interests)
        user_set = set(user_interests)

        direct_matches = len(career_set & user_set)

        related_matches = 0
        interest_categories = {
            'technology': ['programming', 'computers', 'software', 'digital'],
            'creative': ['art', 'design', 'writing', 'music', 'innovation'],
            'people': ['helping', 'teaching', 'healthcare', 'social'],
            'business': ['finance', 'marketing', 'sales', 'entrepreneurship'],
            'science': ['research', 'analysis', 'experiments', 'data']
        }

        for category, keywords in interest_categories.items():
            career_in_category = any(keyword in ' '.join(career_interests) for keyword in keywords)
            user_in_category = any(keyword in ' '.join(user_interests) for keyword in keywords)
            if career_in_category and user_in_category:
                related_matches += 0.5

        total_matches = direct_matches + related_matches
        max_possible = len(career_interests)

        return min(1.0, total_matches / max_possible) if max_possible > 0 else 0.5

    def _calculate_values_match(self, career_values, user_values):
        if not career_values or not user_values:
            return 0.5

        value_weights = {
            'helping_others': 1.2,
            'stability': 1.1,
            'growth': 1.1,
            'creativity': 1.0,
            'innovation': 1.0,
            'flexibility': 0.9,
            'achievement': 1.0,
            'collaboration': 0.9
        }

        total_match = 0
        total_weight = 0

        for career_value in career_values:
            weight = value_weights.get(career_value, 1.0)
            if career_value in user_values:
                total_match += 1.0 * weight
            else:
                related_match = self._find_related_values(career_value, user_values)
                total_match += related_match * weight
            total_weight += weight

        return total_match / total_weight if total_weight > 0 else 0.5

    def _find_related_values(self, target_value, user_values):
        value_relations = {
            'helping_others': ['service', 'impact', 'social_good'],
            'stability': ['security', 'predictability', 'steady_income'],
            'growth': ['advancement', 'learning', 'development'],
            'creativity': ['innovation', 'artistic', 'original'],
            'flexibility': ['work_life_balance', 'autonomy', 'freedom']
        }
        related_values = value_relations.get(target_value, [])
        for user_value in user_values:
            if user_value in related_values:
                return 0.7
        return 0.0

    def _calculate_work_style_match(self, career_work_style, user_work_style):
        if not career_work_style or not user_work_style:
            return 0.5

        match_score = 0
        total_factors = 0

        style_factors = ['independent', 'collaborative', 'structured', 'flexible',
                         'detail_oriented', 'big_picture', 'fast_paced', 'methodical']

        for factor in style_factors:
            if factor in career_work_style and factor in user_work_style:
                career_level = user_work_style.get(factor, 0.5)
                user_level = user_work_style.get(factor, 0.5)
                factor_match = 1 - abs(career_level - user_level)
                match_score += factor_match
                total_factors += 1

        return match_score / total_factors if total_factors > 0 else 0.5

    # ---------- Weighting, Bonuses, Confidence ----------

    def _adjust_weights_dynamically(self, personality_match, skills_match,
                                    interests_match, values_match, work_style_match):
        base_weights = self.matching_weights.copy()

        if personality_match > 0.8:
            base_weights['personality'] += 0.1
            base_weights['skills'] -= 0.05
            base_weights['interests'] -= 0.05

        if skills_match > 0.8:
            base_weights['skills'] += 0.1
            base_weights['personality'] -= 0.05
            base_weights['values'] -= 0.05

        total_weight = sum(base_weights.values())
        for key in base_weights:
            base_weights[key] /= total_weight

        return base_weights

    def _apply_career_bonuses(self, base_score, career_info, skill_scores):
        bonus = 0
        growth_outlook = career_info.get('growth_outlook', '').lower()
        if 'excellent' in growth_outlook:
            bonus += 0.05
        elif 'good' in growth_outlook:
            bonus += 0.02

        high_demand_skills = ['python', 'machine learning', 'data analysis',
                              'digital marketing', 'project management']
        required_skills = [s.lower() for s in career_info.get('skills_required', [])]
        for skill in high_demand_skills:
            if any(skill in req for req in required_skills):
                if skill.replace(' ', '_') in skill_scores:
                    bonus += 0.02

        salary_range = career_info.get('salary_range', {})
        if salary_range:
            senior_max = salary_range.get('senior', (0, 0))[1]
            if senior_max > 150000:
                bonus += 0.03

        return base_score + bonus

    # ---------- Public APIs ----------

    def get_top_matches(self, career_matches, limit=10):
        sorted_matches = sorted(
            career_matches.items(),
            key=lambda x: x[1]['match_score'],
            reverse=True
        )
        return dict(sorted_matches[:limit])

    def get_matches_by_category(self, career_matches):
        categories = {}
        for career_id, match_data in career_matches.items():
            category = match_data['career_info']['category']
            if category not in categories:
                categories[category] = []
            categories[category].append((career_id, match_data))

        for category in categories:
            categories[category].sort(key=lambda x: x[1]['match_score'], reverse=True)
        return categories

    def _compile_resources(self, top_matches):
        """Compile relevant resources for career exploration"""
        resources = {
            'learning_platforms': [
                'Coursera', 'LinkedIn Learning', 'Udemy', 'edX',
                'Skillshare', 'Pluralsight', 'Khan Academy'
            ],
            'networking_platforms': [
                'LinkedIn', 'Professional associations', 'Meetup groups',
                'Industry conferences', 'Alumni networks'
            ],
            'job_search_platforms': [
                'LinkedIn Jobs', 'Indeed', 'Glassdoor', 'AngelList',
                'ZipRecruiter', 'Monster', 'CareerBuilder'
            ],
            'career_research': [
                'Bureau of Labor Statistics', 'O*NET Interest Profiler',
                'Glassdoor company reviews', 'Industry reports',
                'Professional association websites'
            ]
        }

        if top_matches:
            top_career = list(top_matches.values())[0]
            category = top_career['career_info']['category'].lower()

            if 'technology' in category:
                resources['specialized_platforms'] = [
                    'GitHub', 'Stack Overflow', 'HackerRank',
                    'Codecademy', 'FreeCodeCamp'
                ]
            elif 'business' in category:
                resources['specialized_platforms'] = [
                    'Harvard Business Review', 'McKinsey Insights',
                    'Business networking events', 'MBA programs'
                ]
            elif 'healthcare' in category:
                resources['specialized_platforms'] = [
                    'Healthcare professional associations',
                    'Medical journals', 'Healthcare conferences'
                ]
            elif 'education' in category:
                resources['specialized_platforms'] = [
                    'Edutopia', 'Teachers Pay Teachers',
                    'Education conferences', 'Online teaching forums'
                ]
            elif 'design' in category:
                resources['specialized_platforms'] = [
                    'Behance', 'Dribbble', 'AIGA Design',
                    'UX Collective', 'Design workshops'
                ]

        return resources
