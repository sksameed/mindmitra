# components/results_display.py
import json
import statistics
from datetime import datetime
from typing import Dict, List, Any, Optional

class ResultsDisplay:
    """Formats and displays comprehensive career assessment results with professional presentation"""
    
    def __init__(self):
        self.display_templates = self._initialize_templates()
        self.formatting_rules = self._initialize_formatting_rules()
        self.visualization_configs = self._initialize_visualizations()
    
    def _initialize_templates(self):
        """Initialize display templates for different result types"""
        return {
            'personality_summary': {
                'title': 'Your Personality Profile',
                'sections': ['primary_traits', 'description', 'strengths', 'work_preferences'],
                'visualization': 'radar_chart'
            },
            'career_recommendations': {
                'title': 'Your Career Matches',
                'sort_by': 'match_score',
                'max_results': 10,
                'include_details': ['match_score', 'salary_range', 'growth_outlook', 'skills_required'],
                'visualization': 'match_bars'
            },
            'skills_analysis': {
                'title': 'Skills Assessment',
                'categories': ['current_skills', 'developing_skills', 'recommended_skills'],
                'visualization': 'skill_matrix'
            },
            'development_plan': {
                'title': 'Your Development Plan',
                'sections': ['immediate_actions', 'skill_gaps', 'learning_path', 'timeline'],
                'visualization': 'timeline'
            },
            'market_insights': {
                'title': 'Industry Insights',
                'sections': ['growth_trends', 'salary_analysis', 'demand_forecast'],
                'visualization': 'trend_charts'
            }
        }
    
    def _initialize_formatting_rules(self):
        """Initialize formatting rules for consistent display"""
        return {
            'match_score_colors': {
                'excellent': '#4CAF50',     # Green for 85%+
                'good': '#8BC34A',          # Light green for 70-84%
                'fair': '#FFC107',          # Yellow for 55-69%
                'potential': '#FF9800',     # Orange for 40-54%
                'low': '#F44336'            # Red for below 40%
            },
            'skill_level_colors': {
                'expert': '#1976D2',
                'advanced': '#2196F3',
                'intermediate': '#03DAC6',
                'beginner': '#FFC107',
                'none': '#9E9E9E'
            },
            'personality_trait_colors': {
                'openness': '#E91E63',
                'conscientiousness': '#3F51B5',
                'extraversion': '#FF9800',
                'agreeableness': '#4CAF50',
                'neuroticism': '#9C27B0'
            },
            'salary_format': {
                'currency': 'USD',
                'thousands_separator': ',',
                'show_ranges': True
            }
        }
    
    def _initialize_visualizations(self):
        """Initialize visualization configurations"""
        return {
            'charts_enabled': True,
            'default_chart_size': {'width': 800, 'height': 400},
            'color_scheme': 'professional',
            'interactive': True,
            'export_formats': ['PNG', 'PDF', 'SVG']
        }
    
    def format_results(self, personality_profile: Dict, career_matches: Dict, 
                      skills_analysis: Optional[Dict] = None, user_data: Optional[Dict] = None) -> Dict[str, Any]:
        """Format complete assessment results for comprehensive display"""
        
        # Generate timestamp and session info
        session_info = {
            'timestamp': datetime.now().isoformat(),
            'assessment_version': '2.1',
            'total_questions_answered': user_data.get('questions_answered', 0) if user_data else 0,
            'assessment_duration': user_data.get('duration_minutes', 0) if user_data else 0
        }
        
        # Create comprehensive results structure
        formatted_results = {
            'session_info': session_info,
            'executive_summary': self._generate_executive_summary(personality_profile, career_matches),
            'personality_profile': self._format_personality_profile(personality_profile),
            'career_recommendations': self._format_career_recommendations(career_matches),
            'skills_assessment': self._format_skills_assessment(skills_analysis) if skills_analysis else None,
            'development_roadmap': self._generate_development_roadmap(personality_profile, career_matches),
            'market_analysis': self._generate_market_analysis(career_matches),
            'action_plan': self._generate_action_plan(career_matches),
            'resources': self._compile_resources(career_matches),
            'confidence_metrics': self._calculate_confidence_metrics(personality_profile, career_matches),
            'visualization_data': self._prepare_visualization_data(personality_profile, career_matches),
            'export_options': self._get_export_options()
        }
        
        return formatted_results
    
    def _generate_executive_summary(self, personality_profile: Dict, career_matches: Dict) -> Dict[str, Any]:
        """Generate comprehensive executive summary"""
        
        # Get top career matches
        top_matches = self._get_top_matches(career_matches, 3)
        
        # Analyze personality strengths
        personality_strengths = personality_profile.get('strengths', [])
        primary_traits = personality_profile.get('primary_traits', [])
        
        # Calculate overall assessment confidence
        match_scores = [match['match_score'] for match in career_matches.values()]
        avg_match_score = statistics.mean(match_scores) if match_scores else 0
        confidence_level = self._determine_confidence_level(avg_match_score, len(career_matches))
        
        summary = {
            'headline': self._generate_headline(personality_profile, top_matches),
            'key_findings': [
                f"Your personality type shows strong {', '.join(primary_traits[:2])} characteristics",
                f"Found {len(career_matches)} potential career matches with {len(top_matches)} excellent fits",
                f"Top career recommendation: {list(top_matches.values())[0]['career_info']['title'] if top_matches else 'Multiple options'}",
                f"Average compatibility score: {int(avg_match_score * 100)}%"
            ],
            'personality_highlight': self._create_personality_highlight(personality_profile),
            'career_outlook': self._create_career_outlook(top_matches),
            'confidence_assessment': {
                'level': confidence_level,
                'factors': self._get_confidence_factors(personality_profile, career_matches)
            },
            'recommended_next_steps': self._get_immediate_next_steps(top_matches)
        }
        
        return summary
    
    def _generate_headline(self, personality_profile: Dict, top_matches: Dict) -> str:
        """Generate personalized headline for the assessment"""
        primary_traits = personality_profile.get('primary_traits', [])
        
        if not top_matches:
            return "Career Assessment Complete - Multiple Pathways Identified"
        
        top_career = list(top_matches.values())[0]['career_info']['title']
        match_score = int(list(top_matches.values())[0]['match_score'] * 100)
        
        trait_descriptor = ""
        if 'creative' in primary_traits or 'openness' in primary_traits:
            trait_descriptor = "Creative and innovative"
        elif 'analytical' in primary_traits or 'conscientiousness' in primary_traits:
            trait_descriptor = "Analytical and organized"
        elif 'social' in primary_traits or 'extraversion' in primary_traits:
            trait_descriptor = "People-focused and energetic"
        else:
            trait_descriptor = "Well-rounded"
        
        return f"{trait_descriptor} professional with {match_score}% match to {top_career}"
    
    def _format_personality_profile(self, personality_profile: Dict) -> Dict[str, Any]:
        """Format personality profile with enhanced visualizations"""
        
        scores = personality_profile.get('scores', {})
        
        # Convert scores to display format
        formatted_scores = {}
        for trait, score in scores.items():
            level = self._get_trait_level(score)
            formatted_scores[trait] = {
                'raw_score': round(score, 3),
                'percentage': round(score * 100, 1),
                'level': level,
                'description': self._get_trait_description(trait, score),
                'color': self.formatting_rules['personality_trait_colors'].get(trait, '#666666'),
                'career_implications': self._get_trait_career_implications(trait, score)
            }
        
        # Create personality insights
        insights = {
            'dominant_traits': self._identify_dominant_traits(scores),
            'trait_combinations': self._analyze_trait_combinations(scores),
            'work_style_indicators': self._derive_work_style_indicators(scores),
            'leadership_potential': self._assess_leadership_potential(scores),
            'stress_management': self._assess_stress_management(scores),
            'learning_style': self._determine_learning_style(scores)
        }
        
        return {
            'trait_scores': formatted_scores,
            'profile_summary': personality_profile.get('description', ''),
            'strengths': personality_profile.get('strengths', []),
            'development_areas': personality_profile.get('considerations', []),
            'work_preferences': personality_profile.get('work_preferences', {}),
            'personality_insights': insights,
            'compatibility_patterns': self._identify_compatibility_patterns(scores)
        }
    
    def _format_career_recommendations(self, career_matches: Dict) -> Dict[str, Any]:
        """Format career recommendations with comprehensive details"""
        
        # Sort careers by match score
        sorted_careers = sorted(
            career_matches.items(),
            key=lambda x: x[1]['match_score'],
            reverse=True
        )
        
        formatted_careers = []
        category_analysis = {}
        
        for career_id, match_data in sorted_careers:
            career_info = match_data['career_info']
            
            # Format individual career
            formatted_career = {
                'id': career_id,
                'title': career_info['title'],
                'category': career_info['category'],
                'description': career_info['description'],
                'match_analysis': self._format_match_analysis(match_data),
                'career_details': self._format_career_details(career_info),
                'financial_outlook': self._format_financial_outlook(career_info),
                'growth_prospects': self._format_growth_prospects(career_info),
                'skill_requirements': self._format_skill_requirements(career_info),
                'education_pathways': self._format_education_pathways(career_info),
                'day_in_life': self._generate_day_in_life(career_info),
                'pros_and_cons': self._generate_pros_and_cons(career_info, match_data)
            }
            
            formatted_careers.append(formatted_career)
            
            # Update category analysis
            category = career_info['category']
            if category not in category_analysis:
                category_analysis[category] = {
                    'careers': [],
                    'avg_match_score': 0,
                    'total_careers': 0
                }
            
            category_analysis[category]['careers'].append({
                'title': career_info['title'],
                'match_score': match_data['match_score']
            })
            category_analysis[category]['total_careers'] += 1
        
        # Calculate category averages
        for category in category_analysis:
            scores = [c['match_score'] for c in category_analysis[category]['careers']]
            category_analysis[category]['avg_match_score'] = statistics.mean(scores)
        
        return {
            'careers': formatted_careers[:10],  # Top 10 recommendations
            'total_matches_found': len(career_matches),
            'category_breakdown': category_analysis,
            'match_distribution': self._analyze_match_distribution(career_matches),
            'top_categories': self._identify_top_categories(category_analysis),
            'alternative_suggestions': self._generate_alternative_suggestions(sorted_careers[10:]) if len(sorted_careers) > 10 else []
        }
    
    def _format_match_analysis(self, match_data: Dict) -> Dict[str, Any]:
        """Format detailed match analysis"""
        match_score = match_data['match_score']
        breakdown = match_data.get('match_breakdown', {})
        
        return {
            'overall_score': {
                'percentage': round(match_score * 100, 1),
                'level': self._get_match_level(match_score),
                'color': self._get_match_color(match_score),
                'confidence': match_data.get('confidence_level', 'Medium')
            },
            'component_scores': self._format_component_scores(breakdown),
            'strengths': self._identify_match_strengths(breakdown),
            'areas_for_development': self._identify_development_areas(breakdown),
            'compatibility_explanation': self._generate_compatibility_explanation(breakdown),
            'recommendation_reasoning': self._generate_recommendation_reasoning(match_data)
        }
    
    def _format_career_details(self, career_info: Dict) -> Dict[str, Any]:
        """Format comprehensive career details"""
        return {
            'work_environment': career_info.get('work_environment', 'Varies'),
            'typical_responsibilities': self._generate_typical_responsibilities(career_info),
            'career_progression': self._generate_career_progression(career_info),
            'work_schedule': self._determine_work_schedule(career_info),
            'travel_requirements': self._assess_travel_requirements(career_info),
            'physical_demands': self._assess_physical_demands(career_info),
            'technology_usage': self._assess_technology_usage(career_info),
            'interpersonal_requirements': self._assess_interpersonal_requirements(career_info)
        }
    
    def _format_financial_outlook(self, career_info: Dict) -> Dict[str, Any]:
        """Format financial and compensation information"""
        salary_range = career_info.get('salary_range', {})
        
        financial_data = {
            'salary_ranges': self._format_salary_ranges(salary_range),
            'compensation_structure': self._determine_compensation_structure(career_info),
            'earning_potential': self._assess_earning_potential(career_info),
            'benefits_typical': self._get_typical_benefits(career_info),
            'geographic_variations': self._analyze_geographic_salary_variations(career_info),
            'industry_comparison': self._compare_industry_salaries(career_info)
        }
        
        return financial_data
    
    def _format_growth_prospects(self, career_info: Dict) -> Dict[str, Any]:
        """Format career growth and future prospects"""
        return {
            'job_outlook': career_info.get('growth_outlook', 'Unknown'),
            'growth_factors': self._identify_growth_factors(career_info),
            'future_trends': self._predict_future_trends(career_info),
            'automation_impact': self._assess_automation_impact(career_info),
            'skill_evolution': self._predict_skill_evolution(career_info),
            'advancement_timeline': self._create_advancement_timeline(career_info),
            'lateral_opportunities': self._identify_lateral_opportunities(career_info)
        }
    
    def _format_skill_requirements(self, career_info: Dict) -> Dict[str, Any]:
        """Format skill requirements with detailed breakdown"""
        required_skills = career_info.get('skills_required', [])
        
        # Categorize skills
        skill_categories = {
            'technical': [],
            'soft': [],
            'industry_specific': [],
            'leadership': [],
            'analytical': []
        }
        
        for skill in required_skills:
            category = self._categorize_skill(skill)
            skill_categories[category].append({
                'name': skill,
                'importance': self._assess_skill_importance(skill, career_info),
                'difficulty': self._assess_skill_difficulty(skill),
                'learning_resources': self._get_skill_learning_resources(skill)
            })
        
        return {
            'categorized_skills': skill_categories,
            'priority_skills': self._identify_priority_skills(required_skills, career_info),
            'emerging_skills': self._identify_emerging_skills(career_info),
            'skill_gap_analysis': self._perform_skill_gap_analysis(required_skills),
            'certification_recommendations': self._recommend_certifications(career_info)
        }
    
    def _generate_development_roadmap(self, personality_profile: Dict, career_matches: Dict) -> Dict[str, Any]:
        """Generate comprehensive development roadmap"""
        
        top_careers = self._get_top_matches(career_matches, 3)
        
        roadmap = {
            'assessment_date': datetime.now().strftime('%Y-%m-%d'),
            'roadmap_timeline': '12-24 months',
            'phases': {
                'phase_1': {
                    'name': 'Foundation Building',
                    'duration': '0-3 months',
                    'objectives': self._get_foundation_objectives(personality_profile, top_careers),
                    'activities': self._get_foundation_activities(top_careers),
                    'milestones': self._get_foundation_milestones(),
                    'resources_needed': self._get_foundation_resources()
                },
                'phase_2': {
                    'name': 'Skill Development',
                    'duration': '3-9 months',
                    'objectives': self._get_development_objectives(top_careers),
                    'activities': self._get_development_activities(top_careers),
                    'milestones': self._get_development_milestones(),
                    'resources_needed': self._get_development_resources()
                },
                'phase_3': {
                    'name': 'Career Transition',
                    'duration': '9-18 months',
                    'objectives': self._get_transition_objectives(top_careers),
                    'activities': self._get_transition_activities(top_careers),
                    'milestones': self._get_transition_milestones(),
                    'resources_needed': self._get_transition_resources()
                },
                'phase_4': {
                    'name': 'Optimization & Growth',
                    'duration': '18+ months',
                    'objectives': self._get_optimization_objectives(),
                    'activities': self._get_optimization_activities(),
                    'milestones': self._get_optimization_milestones(),
                    'resources_needed': self._get_optimization_resources()
                }
            },
            'success_metrics': self._define_success_metrics(top_careers),
            'risk_mitigation': self._identify_risk_mitigation_strategies(),
            'support_system': self._recommend_support_system(),
            'budget_considerations': self._estimate_development_costs()
        }
        
        return roadmap
    
    def _generate_market_analysis(self, career_matches: Dict) -> Dict[str, Any]:
        """Generate comprehensive market analysis"""
        
        all_careers = list(career_matches.values())
        
        return {
            'industry_overview': self._analyze_industry_trends(all_careers),
            'salary_analysis': self._perform_salary_analysis(all_careers),
            'job_market_conditions': self._assess_job_market_conditions(all_careers),
            'geographic_opportunities': self._analyze_geographic_opportunities(all_careers),
            'skills_demand_forecast': self._forecast_skills_demand(all_careers),
            'competitive_landscape': self._analyze_competitive_landscape(all_careers),
            'emerging_opportunities': self._identify_emerging_opportunities(all_careers),
            'market_risks': self._identify_market_risks(all_careers)
        }
    
    def _generate_action_plan(self, career_matches: Dict) -> Dict[str, Any]:
        """Generate specific, actionable career plan"""
        
        top_career = self._get_top_matches(career_matches, 1)
        if not top_career:
            return {}
        
        career_info = list(top_career.values())[0]['career_info']
        
        return {
            'immediate_actions': {
                'this_week': [
                    f"Research {career_info['title']} job market in your area",
                    "Update LinkedIn profile with relevant keywords",
                    "Identify 3 professionals in the field for informational interviews"
                ],
                'this_month': [
                    "Complete online assessment of current skills vs. requirements",
                    "Start following industry leaders and publications",
                    "Join relevant professional associations or online communities",
                    "Begin documenting transferable skills from current experience"
                ]
            },
            'short_term_goals': {
                '3_months': self._get_short_term_goals(career_info),
                '6_months': self._get_medium_term_goals(career_info)
            },
            'long_term_objectives': {
                '1_year': self._get_one_year_objectives(career_info),
                '2_years': self._get_two_year_objectives(career_info)
            },
            'networking_strategy': self._create_networking_strategy(career_info),
            'skill_building_plan': self._create_skill_building_plan(career_info),
            'job_search_strategy': self._create_job_search_strategy(career_info),
            'contingency_plans': self._create_contingency_plans(career_matches)
        }
    
    def _compile_resources(self, career_matches: Dict) -> Dict[str, Any]:
        """Compile comprehensive resources for career development"""
        
        top_careers = self._get_top_matches(career_matches, 5)
        
        return {
            'learning_platforms': {
                'online_courses': [
                    {'name': 'Coursera', 'url': 'https://coursera.org', 'focus': 'University-level courses'},
                    {'name': 'LinkedIn Learning', 'url': 'https://linkedin.com/learning', 'focus': 'Professional skills'},
                    {'name': 'Udemy', 'url': 'https://udemy.com', 'focus': 'Practical skills'},
                    {'name': 'edX', 'url': 'https://edx.org', 'focus': 'Academic courses'},
                    {'name': 'Skillshare', 'url': 'https://skillshare.com', 'focus': 'Creative skills'}
                ],
                'specialized_platforms': self._get_specialized_platforms(top_careers),
                'certification_programs': self._get_certification_programs(top_careers)
            },
            'networking_resources': {
                'professional_associations': self._get_professional_associations(top_careers),
                'networking_events': self._get_networking_events(top_careers),
                'online_communities': self._get_online_communities(top_careers),
                'mentorship_programs': self._get_mentorship_programs(top_careers)
            },
            'job_search_tools': {
                'job_boards': [
                    {'name': 'LinkedIn Jobs', 'url': 'https://linkedin.com/jobs'},
                    {'name': 'Indeed', 'url': 'https://indeed.com'},
                    {'name': 'Glassdoor', 'url': 'https://glassdoor.com'},
                    {'name': 'AngelList', 'url': 'https://angel.co', 'focus': 'Startups'},
                    {'name': 'ZipRecruiter', 'url': 'https://ziprecruiter.com'}
                ],
                'industry_specific_boards': self._get_industry_job_boards(top_careers),
                'recruitment_agencies': self._get_recruitment_agencies(top_careers)
            },
            'research_resources': {
                'industry_publications': self._get_industry_publications(top_careers),
                'market_research': [
                    {'name': 'Bureau of Labor Statistics', 'url': 'https://bls.gov'},
                    {'name': 'O*NET Interest Profiler', 'url': 'https://mynextmove.org'},
                    {'name': 'PayScale', 'url': 'https://payscale.com'},
                    {'name': 'Glassdoor Research', 'url': 'https://glassdoor.com/research/'}
                ],
                'company_research_tools': [
                    {'name': 'Crunchbase', 'url': 'https://crunchbase.com'},
                    {'name': 'Owler', 'url': 'https://owler.com'},
                    {'name': 'Vault', 'url': 'https://vault.com'}
                ]
            },
            'financial_planning': {
                'salary_negotiation': self._get_salary_negotiation_resources(),
                'career_investment': self._get_career_investment_guidance(),
                'financial_transition': self._get_financial_transition_advice()
            }
        }
    
    def _calculate_confidence_metrics(self, personality_profile: Dict, career_matches: Dict) -> Dict[str, Any]:
        """Calculate comprehensive confidence metrics for the assessment"""
        
        # Personality assessment confidence
        personality_scores = personality_profile.get('scores', {})
        personality_confidence = self._assess_personality_confidence(personality_scores)
        
        # Career matching confidence
        match_scores = [match['match_score'] for match in career_matches.values()]
        matching_confidence = self._assess_matching_confidence(match_scores, career_matches)
        
        # Data quality confidence
        data_quality = self._assess_data_quality(career_matches)
        
        # Overall confidence
        overall_confidence = (personality_confidence + matching_confidence + data_quality) / 3
        
        return {
            'overall_confidence': {
                'score': round(overall_confidence, 2),
                'level': self._get_confidence_level_description(overall_confidence),
                'explanation': self._explain_overall_confidence(overall_confidence)
            },
            'component_confidence': {
                'personality_assessment': {
                    'score': round(personality_confidence, 2),
                    'factors': self._get_personality_confidence_factors(personality_scores)
                },
                'career_matching': {
                    'score': round(matching_confidence, 2),
                    'factors': self._get_matching_confidence_factors(match_scores, career_matches)
                },
                'data_quality': {
                    'score': round(data_quality, 2),
                    'factors': self._get_data_quality_factors(career_matches)
                }
            },
            'reliability_indicators': self._get_reliability_indicators(personality_profile, career_matches),
            'limitations': self._identify_assessment_limitations(),
            'recommendations': self._get_confidence_improvement_recommendations()
        }
    
    def _prepare_visualization_data(self, personality_profile: Dict, career_matches: Dict) -> Dict[str, Any]:
        """Prepare data for various visualizations"""
        
        return {
            'personality_radar': self._prepare_personality_radar_data(personality_profile),
            'career_match_bars': self._prepare_career_match_bars_data(career_matches),
            'skills_matrix': self._prepare_skills_matrix_data(career_matches),
            'salary_comparison': self._prepare_salary_comparison_data(career_matches),
            'category_distribution': self._prepare_category_distribution_data(career_matches),
            'growth_timeline': self._prepare_growth_timeline_data(career_matches),
            'match_breakdown': self._prepare_match_breakdown_data(career_matches)
        }
    
    # Helper methods for formatting and analysis
    
    def _get_top_matches(self, career_matches: Dict, limit: int) -> Dict:
        """Get top N career matches"""
        sorted_matches = sorted(
            career_matches.items(),
            key=lambda x: x[1]['match_score'],
            reverse=True
        )
        return dict(sorted_matches[:limit])
    
    def _get_trait_level(self, score: float) -> str:
        """Convert trait score to descriptive level"""
        if score >= 0.8:
            return 'Very High'
        elif score >= 0.6:
            return 'High'
        elif score >= 0.4:
            return 'Moderate'
        elif score >= 0.2:
            return 'Low'
        else:
            return 'Very Low'
    
    def _get_match_level(self, score: float) -> str:
        """Convert match score to descriptive level"""
        if score >= 0.85:
            return 'Excellent Match'
        elif score >= 0.70:
            return 'Good Match'
        elif score >= 0.55:
            return 'Fair Match'
        elif score >= 0.40:
            return 'Potential Match'
        else:
            return 'Limited Match'
    
    def _get_match_color(self, score: float) -> str:
        """Get color for match score visualization"""
        if score >= 0.85:
            return self.formatting_rules['match_score_colors']['excellent']
        elif score >= 0.70:
            return self.formatting_rules['match_score_colors']['good']
        elif score >= 0.55:
            return self.formatting_rules['match_score_colors']['fair']
        elif score >= 0.40:
            return self.formatting_rules['match_score_colors']['potential']
        else:
            return self.formatting_rules['match_score_colors']['low']
    
    def _get_export_options(self) -> Dict[str, Any]:
        """Get available export options for results"""
        return {
            'formats': ['PDF', 'Word', 'JSON', 'CSV'],
            'templates': ['Executive Summary', 'Detailed Report', 'Action Plan', 'Development Roadmap'],
            'customization': {
                'include_charts': True,
                'include_detailed_analysis': True,
                'include_resources': True,
                'branding_options': ['Professional', 'Minimalist', 'Colorful']
            }
        }
    
    # Placeholder methods for complex analysis functions
    # These would be implemented with full business logic
    
    def _get_trait_description(self, trait: str, score: float) -> str:
        """Get description for personality trait score"""
        # Implementation would return detailed trait descriptions
        return f"Your {trait} score indicates {self._get_trait_level(score).lower()} levels in this area."
    
    def _identify_dominant_traits(self, scores: Dict) -> List[str]:
        """Identify dominant personality traits"""
        return [trait for trait, score in scores.items() if score > 0.6]
    
    def _generate_typical_responsibilities(self, career_info: Dict) -> List[str]:
        """Generate typical job responsibilities"""
        # Implementation would generate role-specific responsibilities
        return [
            "Primary responsibility based on role analysis",
            "Secondary responsibility from job market data",
            "Additional duties common to the position"
        ]
    
    def _format_salary_ranges(self, salary_range: Dict) -> Dict[str, str]:
        """Format salary ranges for display"""
        if not salary_range:
            return {'display': 'Salary information not available'}

        formatted = {}
        currency = self.formatting_rules['salary_format']['currency']
        sep = self.formatting_rules['salary_format']['thousands_separator']

        for level, (low, high) in salary_range.items():
            low_fmt = f"{currency} {low:,.0f}".replace(",", sep)
            high_fmt = f"{currency} {high:,.0f}".replace(",", sep)
            formatted[level] = f"{low_fmt} - {high_fmt}"

        return {
            'display': formatted,
            'raw': salary_range
        }

    def _determine_compensation_structure(self, career_info: Dict) -> str:
        """Guess compensation structure based on career type"""
        category = career_info.get('category', '').lower()
        if 'freelance' in category or 'creative' in category:
            return "Project-based / Freelance opportunities"
        elif 'sales' in category or 'business' in category:
            return "Base salary + performance incentives"
        else:
            return "Fixed salary with potential bonuses"

    def _assess_earning_potential(self, career_info: Dict) -> str:
        """Provide high-level statement on earning potential"""
        salary = career_info.get('salary_range', {})
        if not salary:
            return "Unknown earning potential"
        senior_max = salary.get('senior', (0, 0))[1]
        if senior_max > 150000:
            return "High earning potential"
        elif senior_max > 80000:
            return "Moderate to high earning potential"
        else:
            return "Stable earning potential"

    def _get_typical_benefits(self, career_info: Dict) -> List[str]:
        """Provide common benefits (placeholder)"""
        return [
            "Health insurance",
            "Retirement savings plan",
            "Paid time off",
            "Professional development opportunities"
        ]

    def _analyze_geographic_salary_variations(self, career_info: Dict) -> Dict[str, Any]:
        """Placeholder for location-based salary analysis"""
        return {
            'urban': "+20% above national average",
            'suburban': "Average market rates",
            'rural': "-10% below national average"
        }

    def _compare_industry_salaries(self, career_info: Dict) -> str:
        """Placeholder industry comparison"""
        category = career_info.get('category', '').lower()
        if 'technology' in category:
            return "Technology careers generally pay above average compared to other fields."
        elif 'healthcare' in category:
            return "Healthcare offers stable salaries with growth potential."
        else:
            return "Salaries vary by industry and region."
