# Add your code here
def analyze_smoker(smoker_status):
    if smoker_status == 1:
        print("To lower your cost, you should consider quitting smoking.")
    else:
        print("Smoking is not an issue for you.")


def analyze_bmi(bmi_value):
    healthy_low = round(abs(bmi_value - 25), 2)
    healthy_high = round(abs(bmi_value - 18.5), 2)
    message_low = "You can fall into a healthy range by lowering your BMI by " + str(healthy_low) + " points."
    message_high = "You can fall into a healthy range by raising your BMI by " + str(healthy_high) + " points."
    if bmi_value > 30:
        print(message_low)
    elif bmi_value <= 30 and bmi_value >= 25:
        print(message_low)
    elif bmi_value >= 18.5 and bmi < 25:
        print("Your BMI is in a healthy range.")
    elif bmi_value < 18.5:
        print(message_high)


def analyze_age(age_years):
    if age_years >= 50:
        print("Consider getting younger to lower your costs! Thanks for using Insuresponse(C).")


# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    analyze_smoker(smoker)
    analyze_bmi(bmi)
    analyze_age(age)
    print("\n")
    return estimated_cost


# Estimate Keanu's insurance cost
try:
    keanu_insurance_cost = estimate_insurance_cost(name='Keanu', age=59, sex=1, bmi=26.2, num_of_children=3, smoker=1)

    adam_insurance_cost = estimate_insurance_cost("Adam", "forced_error", 1, 26.6, 0, 0)

except:
    print("Uh oh, provided value(s) caused an error.")





