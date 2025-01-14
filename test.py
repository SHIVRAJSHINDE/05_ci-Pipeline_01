from graphviz import Digraph

# Define the flowchart
dot = Digraph(comment='CI Workflow')

# Add nodes for each step
dot.node('A', 'Push Code to GitHub')
dot.node('B', 'Checkout Code (actions/checkout@v3)')
dot.node('C', 'Setup Python 3.9 (actions/setup-python@v2)')
dot.node('D', 'Install flake8')
dot.node('E', 'Run flake8')

# Add edges to define the flow
dot.edge('A', 'B')  # Push -> Checkout
dot.edge('B', 'C')  # Checkout -> Setup Python
dot.edge('C', 'D')  # Setup Python -> Install flake8
dot.edge('D', 'E')  # Install flake8 -> Run flake8

# Save and render the flowchart to a file
dot.render('ci_workflow', format='png', view=True)

print("Flowchart created and saved as ci_workflow.png")
