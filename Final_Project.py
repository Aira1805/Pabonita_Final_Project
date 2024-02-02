class BMIAnalyzer:
    UNDERWEIGHT = 18.5
    NORMAL_WEIGHT = 24.9
    OVERWEIGHT = 29.9

    def __init__(self, height, weight, age):
        self.height = height
        self.weight = weight
        self.age = age

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def analyze_bmi(self, bmi):
        if bmi < self.UNDERWEIGHT:
            return "underweight"
        elif self.UNDERWEIGHT <= bmi <= self.NORMAL_WEIGHT:
            return "normal weight"
        elif self.NORMAL_WEIGHT < bmi <= self.OVERWEIGHT:
            return "overweight"
        else:
            return "obese"

    def weight_recommendation(self, current_bmi):
        if current_bmi < self.UNDERWEIGHT:
            target_weight = self.NORMAL_WEIGHT * (self.height ** 2)
            weight_to_gain = target_weight - self.weight
            return f"To reach a normal weight, you need to gain approximately {weight_to_gain:.2f} kilograms."
        elif self.NORMAL_WEIGHT < current_bmi <= self.OVERWEIGHT:
            target_weight = self.NORMAL_WEIGHT * (self.height ** 2)
            weight_to_lose = self.weight - target_weight
            return f"To reach a normal weight, you need to lose approximately {weight_to_lose:.2f} kilograms."
        else:
            return "Maintain a healthy lifestyle."


def get_user_input():
    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))
        age = int(input("Enter your age: "))
        return height, weight, age
    except ValueError:
        print("Invalid input. Please enter numeric values for height, weight, and age.")
        return get_user_input()


def main():
    print("Hey! Welcome to the BMI Calculator and Weight Recommendation Program!")

    height, weight, age = get_user_input()

    user_profile = BMIAnalyzer(height, weight, age)
    bmi = user_profile.calculate_bmi()

    print("\nBMI Result:")
    print(f"Your BMI is: {bmi:.2f}")

    bmi_category = user_profile.analyze_bmi(bmi)
    print(f"You are {bmi_category}.")

    if bmi_category in ["underweight", "overweight"]:
        recommendation = user_profile.weight_recommendation(bmi)
        print(recommendation)

    print("\nThank you for using the BMI Calculator and Weight Recommendation Program!")


if __name__ == "__main__":
    main()
