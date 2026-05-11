from google import genai

client = genai.Client(
    api_key="AIzaSyDxcp8_v7DRIm3svvjrM4h1H87oQVorUSY"
)

def get_resume_suggestions(resume_text, missing_skills):

    prompt = f"""
    You are an expert ATS resume reviewer.

    Analyze this resume and provide improvement suggestions.

    Resume:
    {resume_text}

    Missing Skills:
    {missing_skills}

    Give concise ATS improvement suggestions.
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print("\nGemini API unavailable.")
        print("Using fallback suggestions...\n")

        fallback = f"""
1. Add projects related to: {", ".join(missing_skills)}

2. Improve ATS keyword optimization.

3. Add measurable achievements in projects.

4. Include deployment and frontend integration.

5. Add more industry-relevant technical skills.
"""

        return fallback