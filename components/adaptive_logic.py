class AdaptiveQuestionLogic:
    def __init__(self):
        self.question_order = []
        self.answer_thresholds = {}  # Store thresholds for adaptive branching

    def initialize(self, total_questions, thresholds=None):
        self.question_order = list(range(total_questions))
        if thresholds:
            self.answer_thresholds = thresholds  # e.g., {question_id: {value: next_id}}

    def get_next_question(self, current_question_id, user_answers):
        if current_question_id + 1 < len(self.question_order):
            # Simple adaptive logic: Check if there's a threshold-based jump
            if current_question_id in self.answer_thresholds:
                answer = user_answers.get(str(current_question_id))
                if answer and answer in self.answer_thresholds[current_question_id]:
                    return self.answer_thresholds[current_question_id][answer]
            return current_question_id + 1
        return None