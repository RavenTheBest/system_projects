def calculate_bmi(height, weight):
    bmi = weight / height ** 2
    return bmi
def classify_bmi(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "healthy weight"
    elif bmi >= 25 and bmi < 30:
        return "overweight"
    else:
        return "obese"

def format_bmi_output(bmi, bmi_category):
    bmi_string = f"{bmi:.2f}"
    bmi_category_string = bmi_category.title()
    return f"Your BMI is {bmi_string} ({bmi_category_string})"
while True:
    try:
        height = float(input("Height (m): "))
        weight = float(input("Weight (kg): "))
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive values.")
        bmi = calculate_bmi(height, weight)
        bmi_category = classify_bmi(bmi)
        bmi_output = format_bmi_output(bmi, bmi_category)
        print(bmi_output)
    except:
        print("Invalid input")
        continue
