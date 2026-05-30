def analyze_productivity(

    sleep,
    stress,
    work_hours,
    mood

):

    energy = 100

    if sleep < 5:
        energy -= 40

    elif sleep < 7:
        energy -= 20

    if stress >= 4:
        energy -= 25

    elif stress >= 2:
        energy -= 10

    if work_hours > 8:
        energy -= 20

    elif work_hours > 5:
        energy -= 10

    if mood <= 2:
        energy -= 15

    if energy < 0:
        energy = 0

    burnout = 100 - energy

    if energy >= 75:

        recommendation = (
            "High energy detected. "
            "Best time for difficult tasks."
        )

    elif energy >= 45:

        recommendation = (
            "Moderate energy detected. "
            "Focus on medium tasks."
        )

    else:

        recommendation = (
            "Low energy detected. "
            "Take rest and lighter tasks."
        )

    return {

        "energy": energy,

        "burnout": burnout,

        "recommendation": recommendation
    }