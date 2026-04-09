from crewai import Crew

from agents import interview_specialist
from tasks import interview_question_task

crew = Crew(
    agents=[interview_specialist],
    tasks=[interview_question_task],
)

role = "Backend Developer"
level = "senior"

result = crew.kickoff(inputs={"role": role, "level": level})

print("Response:", result)
