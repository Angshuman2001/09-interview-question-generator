from crewai import Crew

from agents import interview_specialist
from tasks import interview_question_task

crew = Crew(
    agents=[interview_specialist],
    tasks=[interview_question_task],
)

role = "AI Engineer"
level = "senior"

result = crew.kickoff(inputs={"role": role, "level": level})

print("Response:", result)
