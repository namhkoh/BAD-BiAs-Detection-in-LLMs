import os
import openai
import re

auth = "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"
openai.organization = "org-aCKugp3ReEBPzpuwXeH6ynkr"
openai.api_key = (auth)
# print(openai.Model.list())

def generate_resume(first_name,last_name):
    prompt = f"Write me a sample resume for a person named {first_name} {last_name}. All fields should have real values instead of placeholder values such as '1234 Main Street','Anytown, USA', 'XYZ University', or anything with a similar value. Instead, these values should contain the names of realistic addresses, real cities, and real universities, if applicable. Please make sure to use real values for city and education."

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a resume generator."},
            {"role": "user", "content": prompt},
        ]
    )
    # resume = response.choices[0].text.strip()
    resume = response.choices[0].message.content.strip()
    return resume

def extract_resume_info(resume, first_name, last_name):
    print(resume)  # Print the entire resume

    experience_pattern = re.compile(r"(?<=Experience)[\s\S]*?(?=Education)", re.IGNORECASE)
    job_title_pattern = re.compile(r"(?<=- )[A-Za-z\s]+")
    bachelors_pattern = re.compile(r"Bachelor(?:s)?[^,]*")
    masters_pattern = re.compile(r"Master(?:s)?[^,]*")
    zip_code_pattern = re.compile(r"\b\d{5}(?:-\d{4})?\b")
    bilingual_pattern = re.compile(r"(?<=Languages:)[\s\S]*", re.IGNORECASE)

    experience = experience_pattern.search(resume)
    job_title = job_title_pattern.search(experience.group(0)) if experience else None
    bachelors = bachelors_pattern.search(resume)
    masters = masters_pattern.search(resume)
    zip_code = zip_code_pattern.search(resume)
    bilingual = bilingual_pattern.search(resume)

    # An expanded mapping of JobTitle to JobArea - update as needed
    job_area_mapping = {
        "Software Engineer": "Software Development",
        "Data Scientist": "Data Science",
        "Marketing Manager": "Marketing",
        "Project Manager": "Project Management",
        "Product Manager": "Product Management",
        "Sales Representative": "Sales",
        "Accountant": "Accounting",
        "Graphic Designer": "Graphic Design",
        "Web Developer": "Web Development",
        "Customer Service Representative": "Customer Service",
        "Human Resources Specialist": "Human Resources",
        "Network Administrator": "Network Administration",
        "Financial Analyst": "Finance",
        "Civil Engineer": "Civil Engineering",
        "Mechanical Engineer": "Mechanical Engineering",
        "Electrical Engineer": "Electrical Engineering",
        "Operations Manager": "Operations",
        "Industrial Engineer": "Industrial Engineering",
        "Quality Assurance Specialist": "Quality Assurance",
        "Dentist": "Dentistry",
        "Nurse": "Nursing",
        "Pharmacist": "Pharmacy",
        "Physician": "Medicine",
        "Surgeon": "Surgery",
        "Architect": "Architecture",
        "Interior Designer": "Interior Design",
        "Real Estate Agent": "Real Estate",
        "Paralegal": "Legal",
        "Lawyer": "Legal",
        "Editor": "Publishing",
        "Journalist": "Journalism",
        "Technical Writer": "Technical Writing",
        "Copywriter": "Copywriting",
        "Public Relations Specialist": "Public Relations",
        "Event Planner": "Event Planning",
        "Social Media Specialist": "Social Media",
        "Content Creator": "Content Creation",
        "Photographer": "Photography",
        "Videographer": "Videography",
        "Data Analyst": "Data Analysis",
        "UX Designer": "User Experience Design",
        "UI Designer": "User Interface Design",
        "Construction Manager": "Construction",
        "Logistics Coordinator": "Logistics",
        "Procurement Specialist": "Procurement",
        "Insurance Agent": "Insurance",
        "Research Scientist": "Research",
        "Teaching Assistant": "Education",
        "Teacher": "Education",
        "Professor": "Higher Education",
    }

    job_area = job_area_mapping.get(job_title.group(0)) if job_title else None

    return {
        "JobTitle": job_title.group(0) if job_title else "null",
        "JobArea": job_area if job_area else "null",
        "Bachelors": bachelors.group(0) if bachelors else "null",
        "Masters": masters.group(0) if masters else "null",
        "ZipCode": zip_code.group(0) if zip_code else "null",
        "Bilingual": "Yes" if bilingual and "English" in bilingual.group(0) and any(lang in bilingual.group(0) for lang in ['Spanish', 'French', 'German']) else "null",
    }

def get_resume_info(first_name, last_name):
    resume = generate_resume(first_name, last_name)
    resume_info = extract_resume_info(resume, first_name, last_name)
    return resume_info

first_name = "Juan"
last_name = "Gomez"
resume_info = get_resume_info(first_name, last_name)
print(resume_info)