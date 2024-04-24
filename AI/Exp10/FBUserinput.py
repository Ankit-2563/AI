class ForwardChainingDiagnosis:
    def __init__(self):
        self.rules = {
            "Flu": ["Fever", "Cough"],
            "Common Cold": ["Cough", "Fatigue"],
            "Fatigue Syndrome": ["Fever", "Fatigue"],
        }

    def forward_chain(self, symptoms):
        possible_diseases = []
        for disease, required_symptoms in self.rules.items():
            if all(symptom in symptoms for symptom in required_symptoms):
                possible_diseases.append(disease)
        return possible_diseases


def forward_chaining_test():
    diagnosis = ForwardChainingDiagnosis()
    user_input = input("Enter your symptoms separated by commas (e.g., Fever, Cough, Fatigue): ")
    symptoms = [s.strip().title() for s in user_input.split(",")]

    possible_diseases = diagnosis.forward_chain(symptoms)
    if possible_diseases:
        print("Possible diseases based on your symptoms:")
        for disease in possible_diseases:
            print(f"- {disease}")
    else:
        print("No matching diseases found.")


class BackwardChainingDiagnosis:
    def __init__(self):
        self.rules = {
            "Flu": ["Fever", "Cough", "Fatigue"],
            "Common Cold": ["Cough", "Fatigue"],
            "Fatigue Syndrome": ["Fever", "Fatigue"],
        }

    def backward_chain(self, disease):
        required_symptoms = self.rules.get(disease, [])
        print(f"To confirm {disease}, check for the following symptoms: {', '.join(required_symptoms)}")
        user_input = input(f"Enter 'yes' if the patient has the symptom, separated by commas for these symptoms - {', '.join(required_symptoms)}: ")
        symptoms_present = [s.strip().lower() == 'yes' for s in user_input.split(",")]

        if all(symptoms_present):
            print(f"The hypothesis that the patient might have {disease} is supported.")
        else:
            print(f"The hypothesis that the patient might have {disease} is not supported.")

def backward_chaining_test():
    diagnosis = BackwardChainingDiagnosis()
    user_input = input("Enter the disease you want to diagnose: ")
    disease = user_input.strip().title()

    diagnosis.backward_chain(disease)

def main():
    while True:
        approach = input("Enter 'f' for Forward Chaining or 'b' for Backward Chaining (q to quit): ").strip().lower()
        if approach == 'f':
            forward_chaining_test()
        elif approach == 'b':
            backward_chaining_test()
        elif approach == 'q':
            break
        else:
            print("Invalid input. Please enter 'f' for Forward Chaining, 'b' for Backward Chaining, or 'q' to quit.")

if __name__ == "__main__":
    main()
