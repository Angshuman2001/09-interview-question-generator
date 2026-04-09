from crewai import Task

from agents import interview_specialist

interview_question_task = Task(
    description=(
        "Generate 10 targeted interview questions for the specified role and seniority level.\n"
        "Follow these steps:\n"
        "1. Consider what skills and competencies matter most for this role at this level.\n"
        "2. Create a balanced mix:\n"
        "   - 4 technical questions (role-specific knowledge and skills)\n"
        "   - 3 behavioral questions (past experience, teamwork, conflict resolution)\n"
        "   - 3 situational questions (hypothetical scenarios relevant to the role)\n"
        "3. Scale difficulty to the seniority level:\n"
        "   - Junior: fundamentals, learning ability, eagerness\n"
        "   - Mid: practical application, independence, problem-solving\n"
        "   - Senior: system design, mentorship, technical leadership\n"
        "   - Lead: architecture decisions, team management, strategic thinking\n"
        "4. For each question, include a brief note on what a strong answer looks like.\n\n"
        "Role: {role}\n"
        "Seniority Level: {level}"
    ),
    expected_output=(
        "A structured list of 10 interview questions:\n"
        "- Each question numbered with its category (Technical / Behavioral / Situational)\n"
        "- A 'What to look for' note under each question\n"
        "- Questions scaled to the specified seniority level"
    ),
    agent=interview_specialist,
)
