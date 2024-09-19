import matplotlib.pyplot as plt

# Define enthalpy changes (in kJ/mol) for each reaction step
# Example reaction: A + B -> C
# Step 1: A -> X
# Step 2: X + B -> C
enthalpy_steps = {
    "Step 1: A -> X": 50,   # Enthalpy change for step 1
    "Step 2: X + B -> C": -30,  # Enthalpy change for step 2
}

# Define the overall reaction
overall_enthalpy_change = sum(enthalpy_steps.values())

# Create the plot
fig, ax = plt.subplots()

# Create a bar plot for each step
steps = list(enthalpy_steps.keys())
values = list(enthalpy_steps.values())
colors = ['blue', 'green']
ax.bar(steps, values, color=colors)

# Add a horizontal line for the overall reaction enthalpy change
ax.axhline(y=overall_enthalpy_change, color='red', linestyle='--', label=f'Overall Enthalpy Change: {overall_enthalpy_change} kJ/mol')

# Set labels and title
ax.set_xlabel('Reaction Steps')
ax.set_ylabel('Enthalpy Change (kJ/mol)')
ax.set_title('Visual Representation of Hess\'s Law')
ax.legend()

# Show the plot
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
