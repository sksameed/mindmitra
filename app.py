# app.py (Streamlit version)
import streamlit as st
from components.questionnaire import QuestionnaireManager
from components.career_matcher import CareerMatcher
from components.results_display import ResultsDisplay
from utils.data_processor import DataProcessor
from utils.recommendation_engine import RecommendationEngine

# Initialize components
questionnaire_manager = QuestionnaireManager()
career_matcher = CareerMatcher()
results_display = ResultsDisplay()
data_processor = DataProcessor()
recommendation_engine = RecommendationEngine()

# Session state to manage progress
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'assessment_started' not in st.session_state:
    st.session_state.assessment_started = False

# Title
st.title("Career Assessment Tool")

# Start Assessment Button
if not st.session_state.assessment_started:
    if st.button("Start Assessment"):
        st.session_state.assessment_started = True
        st.session_state.current_question = 0
        st.experimental_rerun()

# Questionnaire Flow
if st.session_state.assessment_started:
    total_questions = questionnaire_manager.get_total_questions()
    current_question_id = st.session_state.current_question

    if current_question_id < total_questions:
        question = questionnaire_manager.get_question(current_question_id)
        st.write(f"Question {current_question_id + 1} of {total_questions}")
        st.write(question['question'])

        # Handle different question types
        if question['type'] == 'likert':
            options = {opt['text']: opt['value'] for opt in question['options']}
            selected_answer = st.radio("Select your response:", options.keys(), key=f"q{current_question_id}")
            if st.button("Next", key=f"next_{current_question_id}"):
                st.session_state.answers[str(current_question_id)] = options[selected_answer]
                st.session_state.current_question += 1
                st.experimental_rerun()
        elif question['type'] == 'multiple_choice':
            options = {opt['text']: opt['value'] for opt in question['options']}
            selected_answer = st.selectbox("Select your response:", options.keys(), key=f"q{current_question_id}")
            if st.button("Next", key=f"next_{current_question_id}"):
                st.session_state.answers[str(current_question_id)] = options[selected_answer]
                st.session_state.current_question += 1
                st.experimental_rerun()
        # Add more question types (e.g., multiple_select, ranking) as needed

        st.write(f"Progress: {((current_question_id + 1) / total_questions) * 100:.0f}%")

    else:
        # Process Results
        st.write("Assessment Complete! Processing your results...")
        
        processed_data = data_processor.process_answers(st.session_state.answers)
        personality_profile = career_matcher.analyze_personality(processed_data)
        career_matches = recommendation_engine.get_recommendations(personality_profile, processed_data)
        formatted_results = results_display.format_results(personality_profile, career_matches)

        # Display Results
        st.write("### Your Personality Profile")
        st.write(personality_profile['description'])
        st.write("Strengths:", personality_profile['strengths'])

        st.write("### Career Recommendations")
        for match in career_matches['career_matches']:
            st.write(f"- {match['career']} (Growth Path: {', '.join(match['growth_path'])})")
            st.write("Recommended Resources:", match['resources'])

        if st.button("Restart Assessment"):
            st.session_state.assessment_started = False
            st.session_state.current_question = 0
            st.session_state.answers = {}
            st.experimental_rerun()