import random
import math

knowledge_base = {

    "sleep": {

        "high": 8,
        "medium": 6,
        "low": 4

    },

    "stress": {

        "high": 8,
        "medium": 5,
        "low": 2

    },

    "mood": {

        "high": 8,
        "medium": 5,
        "low": 2

    },

    "workload": {

        "high": 8,
        "medium": 5,
        "low": 3

    }

}

rule_base = [

    "IF sleep < 5 THEN energy = low",

    "IF sleep >= 7 THEN energy = high",

    "IF stress > 8 THEN burnout = high",

    "IF work_hours > 8 THEN fatigue = high",

    "IF mood < 3 THEN motivation = low",

    "IF mood > 7 THEN motivation = high"

]

def evaluate_energy(sleep, stress, work_hours, mood):

    energy_score = 100

    # Sleep Rules
    if sleep < 5:

        energy_score -= 35

    elif sleep < 7:

        energy_score -= 15

    # Stress Rules
    if stress >= 8:

        energy_score -= 30

    elif stress >= 5:

        energy_score -= 15

    # Workload Rules
    if work_hours > 8:

        energy_score -= 20

    elif work_hours > 5:

        energy_score -= 10

    # Mood Rules
    if mood <= 2:

        energy_score -= 20

    elif mood <= 5:

        energy_score -= 10

    if energy_score < 0:

        energy_score = 0

    return energy_score

def analyze_motivation(mood):

    if mood >= 8:

        return "Highly Motivated"

    elif mood >= 5:

        return "Moderately Motivated"

    else:

        return "Low Motivation"

def analyze_fatigue(work_hours):

    if work_hours > 8:

        return "High Fatigue"

    elif work_hours > 5:

        return "Moderate Fatigue"

    else:

        return "Low Fatigue"

def analyze_stress(stress):

    if stress >= 8:

        return "High Stress"

    elif stress >= 5:

        return "Moderate Stress"

    else:

        return "Low Stress"

def infer_burnout(energy, stress):

    facts = []

    if energy < 40:

        facts.append("low_energy")

    if stress > 7:

        facts.append("high_stress")

    if "low_energy" in facts and "high_stress" in facts:

        burnout_level = "High"

    elif "low_energy" in facts:

        burnout_level = "Moderate"

    else:

        burnout_level = "Low"

    return burnout_level

def productivity_level(energy):

    if energy >= 80:

        return "Excellent"

    elif energy >= 60:

        return "Good"

    elif energy >= 40:

        return "Average"

    else:

        return "Poor"

def concentration_level(energy):

    if energy >= 75:

        return "High Concentration"

    elif energy >= 50:

        return "Moderate Concentration"

    else:

        return "Low Concentration"

def health_status(energy):

    if energy >= 80:

        return "Healthy"

    elif energy >= 50:

        return "Moderate"

    else:

        return "Needs Recovery"

task_database = [

    {
        "task": "Coding Assignment",
        "difficulty": 9,
        "deadline": 8
    },

    {
        "task": "Project Work",
        "difficulty": 8,
        "deadline": 9
    },

    {
        "task": "Reading Notes",
        "difficulty": 4,
        "deadline": 5
    },

    {
        "task": "Exercise",
        "difficulty": 3,
        "deadline": 4
    },

    {
        "task": "Meditation",
        "difficulty": 1,
        "deadline": 2
    },

    {
        "task": "Revision",
        "difficulty": 5,
        "deadline": 6
    },

    {
        "task": "Research Work",
        "difficulty": 7,
        "deadline": 8
    }

]

def generate_possible_tasks():

    states = []

    for task in task_database:

        states.append(task)

    return states

def heuristic_score(task, energy, mood):

    difficulty_score = task["difficulty"]

    deadline_score = task["deadline"]

    score = (

        (energy * 0.4)
        + (mood * 10 * 0.2)
        + (deadline_score * 5 * 0.3)
        - (difficulty_score * 4 * 0.1)

    )

    return round(score, 2)

def search_best_tasks(energy, mood):

    states = generate_possible_tasks()

    evaluated_tasks = []

    for task in states:

        score = heuristic_score(

            task,
            energy,
            mood

        )

        evaluated_tasks.append(

            {

                "task": task["task"],
                "score": score

            }

        )

    evaluated_tasks.sort(

        key=lambda x: x["score"],
        reverse=True

    )

    return evaluated_tasks

def priority_level(score):

    if score >= 70:

        return "High Priority"

    elif score >= 50:

        return "Medium Priority"

    else:

        return "Low Priority"

def rank_tasks(energy, mood):

    tasks = search_best_tasks(

        energy,
        mood

    )

    ranked = []

    for task in tasks:

        ranked.append(

            {

                "task": task["task"],

                "score": task["score"],

                "priority": priority_level(

                    task["score"]

                )

            }

        )

    return ranked

def best_task(energy, mood):

    ranked_tasks = rank_tasks(

        energy,
        mood

    )

    return ranked_tasks[0]["task"]

def avoid_task(energy):

    if energy < 40:

        return "Project Work"

    elif energy < 60:

        return "Research Work"

    else:

        return "No Restrictions"

def goal_completion_score(energy):

    probability = (

        energy * 0.85

    )

    return round(

        probability,
        2

    )

def productivity_score(energy, mood):

    score = (

        energy * 0.7

        +

        mood * 5

    )

    return round(

        score,
        2

    )

def efficiency_score(energy, stress):

    score = (

        energy

        -

        stress * 5

    )

    if score < 0:

        score = 0

    return round(

        score,
        2

    )

def burnout_probability(energy, stress):

    probability = (

        (100 - energy) * 0.6

        +

        stress * 5

    )

    if probability > 100:

        probability = 100

    return round(

        probability,
        2

    )

def success_probability(energy, mood):

    probability = (

        energy * 0.7

        +

        mood * 3

    )

    if probability > 100:

        probability = 100

    return round(

        probability,
        2

    )

def productivity_confidence(energy):

    confidence = (

        energy * 0.9

    )

    if confidence > 100:

        confidence = 100

    return round(

        confidence,
        2

    )

def decision_engine(energy):

    if energy >= 80:

        return {

            "recommended_tasks": [

                "Coding Assignment",

                "Project Work",

                "Research Work"

            ],

            "avoid_tasks": [

                "No Restrictions"

            ]

        }

    elif energy >= 50:

        return {

            "recommended_tasks": [

                "Revision",

                "Reading Notes",

                "Exercise"

            ],

            "avoid_tasks": [

                "Research Work"

            ]

        }

    else:

        return {

            "recommended_tasks": [

                "Meditation",

                "Exercise",

                "Light Reading"

            ],

            "avoid_tasks": [

                "Project Work",

                "Coding Assignment"

            ]

        }

def explain_reasoning(

    sleep,

    stress,

    work_hours,

    mood,

    energy

):

    reasons = []

    if sleep < 5:

        reasons.append(

            "Low sleep reduced energy."

        )

    elif sleep >= 7:

        reasons.append(

            "Good sleep improved productivity."

        )

    if stress >= 8:

        reasons.append(

            "High stress increased burnout risk."

        )

    if work_hours > 8:

        reasons.append(

            "Heavy workload caused fatigue."

        )

    if mood <= 3:

        reasons.append(

            "Low mood affected motivation."

        )

    if energy >= 75:

        reasons.append(

            "High energy allows difficult tasks."

        )

    elif energy < 40:

        reasons.append(

            "Low energy suggests lighter tasks."

        )

    return reasons

def performance_analysis(

    energy,

    burnout

):

    traditional_planning = 65

    energy_based_planning = (

        energy

        -

        burnout * 0.1

    )

    improvement = (

        energy_based_planning

        -

        traditional_planning

    )

    return {

        "traditional_score":

            traditional_planning,

        "energy_score":

            round(

                energy_based_planning,

                2

            ),

        "improvement":

            round(

                improvement,

                2

            )

    }

def hybrid_ai_model(

    sleep,

    stress,

    work_hours,

    mood,

    energy

):

    rule_based_output = infer_burnout(

        energy,

        stress

    )

    probability_output = burnout_probability(

        energy,

        stress

    )

    decision_output = decision_engine(

        energy

    )

    return {

        "rule_system":

            rule_based_output,

        "probability":

            probability_output,

        "decision":

            decision_output

    }

def utility_function(energy, burnout):

    utility = (

        energy

        -

        burnout * 0.5

    )

    if utility < 0:

        utility = 0

    return round(

        utility,

        2

    )

def goal_based_agent(energy):

    if energy >= 80:

        goal = "Complete High Priority Tasks"

    elif energy >= 50:

        goal = "Maintain Balanced Productivity"

    else:

        goal = "Recover and Avoid Burnout"

    return goal

def learning_component(productivity_score):

    if productivity_score >= 80:

        return "Excellent productivity pattern detected."

    elif productivity_score >= 60:

        return "Good productivity pattern detected."

    else:

        return "Productivity pattern needs improvement."

def generate_recommendation(

    energy,

    burnout,

    mood

):

    if energy >= 80:

        recommendation = (

            "High energy detected. "

            "Best time for difficult tasks, "

            "coding and project work."

        )

    elif energy >= 50:

        recommendation = (

            "Moderate energy detected. "

            "Focus on revision, reading "

            "and medium difficulty tasks."

        )

    else:

        recommendation = (

            "Low energy detected. "

            "Rest, exercise and meditation "

            "are recommended."

        )

    return recommendation

def explanation_summary(

    reasons

):

    summary = " ".join(

        reasons

    )

    return summary

def analyze_productivity(

    sleep,

    stress,

    work_hours,

    mood

):

    # Rule-Based Energy Analysis
    energy = evaluate_energy(

        sleep,

        stress,

        work_hours,

        mood

    )

    # Forward Chaining
    burnout_level = infer_burnout(

        energy,

        stress

    )

    # Burnout Probability
    burnout_probability_score = burnout_probability(

        energy,

        stress

    )

    # Motivation
    motivation = analyze_motivation(

        mood

    )

    # Fatigue
    fatigue = analyze_fatigue(

        work_hours

    )

    # Stress
    stress_status = analyze_stress(

        stress

    )

    # Productivity
    productivity = productivity_level(

        energy

    )

    # Concentration
    concentration = concentration_level(

        energy

    )

    # Health
    health = health_status(

        energy

    )

    # Best Task Search
    best = best_task(

        energy,

        mood

    )

    # Avoid Task
    avoid = avoid_task(

        energy

    )

    # Goal Completion
    completion_score = goal_completion_score(

        energy

    )

    # Productivity Score
    prod_score = productivity_score(

        energy,

        mood

    )

    # Efficiency Score
    efficiency = efficiency_score(

        energy,

        stress

    )

    # Success Probability
    success = success_probability(

        energy,

        mood

    )

    # Confidence
    confidence = productivity_confidence(

        energy

    )

    # Decision Engine
    decision = decision_engine(

        energy

    )

    # Explainable AI
    reasons = explain_reasoning(

        sleep,

        stress,

        work_hours,

        mood,

        energy

    )

    explanation = explanation_summary(

        reasons

    )

    # Performance Analysis
    performance = performance_analysis(

        energy,

        burnout_probability_score

    )

    # Utility Function
    utility = utility_function(

        energy,

        burnout_probability_score

    )

    # Goal Agent
    goal = goal_based_agent(

        energy

    )

    # Learning Component
    learning = learning_component(

        prod_score

    )

    # Recommendation
    recommendation = generate_recommendation(

        energy,

        burnout_probability_score,

        mood

    )

    return {

        "energy": energy,

        "burnout": burnout_probability_score,

        "recommendation":

            recommendation +

            "\n\nBest Task: " + best +

            "\nAvoid Task: " + avoid +

            "\nBurnout Level: " + burnout_level +

            "\nMotivation: " + motivation +

            "\nFatigue: " + fatigue +

            "\nStress Status: " + stress_status +

            "\nProductivity: " + productivity +

            "\nConcentration: " + concentration +

            "\nHealth Status: " + health +

            "\nGoal Completion Score: " + str(completion_score) +

            "\nEfficiency Score: " + str(efficiency) +

            "\nSuccess Probability: " + str(success) +

            "\nConfidence Level: " + str(confidence) +

            "\nUtility Value: " + str(utility) +

            "\nGoal: " + goal +

            "\nLearning Component: " + learning +

            "\nExplanation: " + explanation

    }
