from majors import MAJORS


def calculate_score(student_data, major_data):
    interests_score = 0
    subjects_score = 0
    skills_score = 0

    if major_data["interests"]:
        matches = set(student_data["interests"]) & set(major_data["interests"])
        interests_score = len(matches) / len(major_data["interests"])

    if major_data["subjects"]:
        matches = set(student_data["subjects"]) & set(major_data["subjects"])
        subjects_score = len(matches) / len(major_data["subjects"])

    if major_data["skills"]:
        matches = set(student_data["skills"]) & set(major_data["skills"])
        skills_score = len(matches) / len(major_data["skills"])

    final_score = (
        interests_score * 0.40 +
        subjects_score * 0.35 +
        skills_score * 0.25
    )

    return round(final_score * 100, 2)


def recommend_majors(student_data):
    results = []

    for major, details in MAJORS.items():
        score = calculate_score(student_data, details)

        results.append({
            "major": major,
            "category": details["category"],
            "score": score
        })

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return results[:5]
