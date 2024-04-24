class Rule:
    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

class KnowledgeBase:
    def __init__(self):
        self.rules = []

    def add_rule(self, antecedent, consequent):
        rule = Rule(antecedent, consequent)
        self.rules.append(rule)

    def forward_chaining(self, initial_facts):
        inferred_facts = set(initial_facts)
        print("Initial facts:", inferred_facts)
        while True:
            new_facts = set()
            for rule in self.rules:
                if all(antecedent in inferred_facts for antecedent in rule.antecedent):
                    new_fact = rule.consequent
                    if new_fact not in inferred_facts:  # Only add if it's a new fact
                        new_facts.add(new_fact)
                        print("Inferred new fact:", new_fact)
            if not new_facts:
                break
            inferred_facts |= new_facts
        return inferred_facts

    def backward_chaining(self, goal, inferred_facts=None, visited=None):
        if inferred_facts is None:
            inferred_facts = set()
        if visited is None:
            visited = set()

        print("Goal:", goal)

        if goal in inferred_facts:
            return True

        if goal in visited:
            return False

        visited.add(goal)

        for rule in self.rules:
            if rule.consequent == goal:
                if all(self.backward_chaining(antecedent, inferred_facts, visited) for antecedent in rule.antecedent):
                    inferred_facts.add(goal)
                    print("Inferred new fact:", goal)
                    return True

        return False

    def backward_chaining_inference(self, goal, initial_facts):
        inferred_facts = set(initial_facts)
        self.backward_chaining(goal, inferred_facts)
        return inferred_facts

# Example usage:
kb = KnowledgeBase()

# Add rules to the knowledge base
kb.add_rule(['flu', 'cough'], 'fever')
kb.add_rule(['fever'], 'sickness')

# Forward chaining example
initial_facts = ['flu', 'cough']
print("Forward chaining result:")
print(kb.forward_chaining(initial_facts))

# Backward chaining example
goal = 'sickness'
print("\nBackward chaining result:")
print(kb.backward_chaining_inference(goal, initial_facts))
