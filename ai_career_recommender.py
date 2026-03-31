projects = [
    {
        "title": "Document Q&A Assistant",
        "description": "Build a system that answers questions based on uploaded PDFs using semantic retrieval and LLMs.",
        "level": "intermediate",
        "tags": ["python", "llm", "nlp", "rag", "backend"],
        "goals": ["portfolio", "ai-career", "international"],
        "estimated_time": "2 weeks"
    },
    {
        "title": "Customer Feedback Classifier",
        "description": "Create a system that classifies customer feedback into categories such as positive, negative, and neutral.",
        "level": "beginner",
        "tags": ["python", "nlp", "classification", "api"],
        "goals": ["portfolio", "internship", "ai-career"],
        "estimated_time": "1 week"
    },
    {
        "title": "Discord AI Assistant",
        "description": "Develop an intelligent Discord bot capable of answering questions, automating tasks, and processing text or images.",
        "level": "intermediate",
        "tags": ["python", "bot", "automation", "llm", "api"],
        "goals": ["portfolio", "freelance", "international"],
        "estimated_time": "2 weeks"
    },
    {
        "title": "AI Resume Analyzer",
        "description": "Build a tool that analyzes resumes and compares them with job descriptions using AI techniques.",
        "level": "intermediate",
        "tags": ["python", "llm", "nlp", "career", "analysis"],
        "goals": ["portfolio", "job-search", "international"],
        "estimated_time": "2 weeks"
    },
    {
        "title": "CSV Insight Generator",
        "description": "Create a tool that reads CSV files and generates insights, summaries, and visual suggestions.",
        "level": "beginner",
        "tags": ["python", "data-analysis", "pandas", "automation"],
        "goals": ["portfolio", "internship", "productivity"],
        "estimated_time": "1 week"
    },
    {
        "title": "Support Intent Classifier",
        "description": "Classify support messages into categories like payment issue, technical problem, cancellation, or complaint.",
        "level": "intermediate",
        "tags": ["python", "nlp", "classification", "backend"],
        "goals": ["portfolio", "ai-career", "internship"],
        "estimated_time": "2 weeks"
    }
]


def calculate_score(project, user_profile):
    score = 0

    if user_profile["level"].lower() == project["level"].lower():
        score += 2

    if user_profile["goal"].lower() in [goal.lower() for goal in project["goals"]]:
        score += 3

    for interest in user_profile["interests"]:
        if interest.lower() in [tag.lower() for tag in project["tags"]]:
            score += 2

    if user_profile["preferred_time"].lower() == project["estimated_time"].lower():
        score += 1

    return score


def recommend_projects(projects, user_profile, top_n=3):
    scored_projects = []

    for project in projects:
        score = calculate_score(project, user_profile)
        scored_projects.append((project, score))

    scored_projects.sort(key=lambda item: item[1], reverse=True)

    return scored_projects[:top_n]


def show_recommendations(recommendations):
    print("\nRecommended projects for you:\n")

    for index, (project, score) in enumerate(recommendations, start=1):
        print(f"{index}. {project['title']} (score: {score})")
        print(f"   Description: {project['description']}")
        print(f"   Level: {project['level']}")
        print(f"   Tags: {', '.join(project['tags'])}")
        print(f"   Estimated time: {project['estimated_time']}")
        print()


def main():
    print("=== AI Career Recommender ===\n")

    level = input("What is your current level? (beginner/intermediate): ").strip()
    goal = input("What is your main goal? (portfolio/internship/ai-career/international/job-search): ").strip()
    interests_input = input("What are your interests? Separate by comma (example: python,llm,backend,nlp): ").strip()
    preferred_time = input("Preferred project duration? (1 week/2 weeks): ").strip()

    interests = [item.strip() for item in interests_input.split(",") if item.strip()]

    user_profile = {
        "level": level,
        "goal": goal,
        "interests": interests,
        "preferred_time": preferred_time
    }

    recommendations = recommend_projects(projects, user_profile)
    show_recommendations(recommendations)


if __name__ == "__main__":
    main()