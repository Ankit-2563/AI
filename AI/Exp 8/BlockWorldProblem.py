class BlockWorldAgent:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def plan(self):
        # Implement a planning algorithm here to generate a plan to reach the goal state
        plan = self.generate_plan()
        return plan

    def generate_plan(self):
        # Implement a planning algorithm (e.g., STRIPS) to generate a plan dynamically
        # This is just a placeholder; replace it with your planning algorithm
        # For simplicity, let's return a simple plan to move each block to its goal position
        plan = []
        for block, goal_location in self.goal_state.items():
            current_location = self.initial_state[block]
            if current_location != goal_location:
                if goal_location == "on table":
                    plan.append(f"Move block {block} to the table")
                else:
                    plan.append(f"Stack block {block} on top of block {goal_location}")
        return plan

# Define initial and goal states with 4-5 blocks
initial_state = {"A": "on table", "B": "on table", "C": "on table", "D": "on E", "E": "on table"}
goal_state = {"A": "on table", "B": "on C", "C": "on D", "D": "on table", "E": "on table"}

# Create a BlockWorldAgent instance
agent = BlockWorldAgent(initial_state, goal_state)

# Print the initial state
print("Initial State:")
for block, location in initial_state.items():
    print(f"Block {block} is {location}")

# Print the goal state
print("\nGoal State:")
for block, location in goal_state.items():
    print(f"Block {block} should be {location}")

# Generate and execute the plan
plan = agent.plan()
print("\nPlan to Achieve Goal State:")
for action in plan:
    print(action)
