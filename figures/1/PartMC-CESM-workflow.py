from graphviz import Digraph

f = Digraph('PartMC-CESM-workflow', filename='PartMC-CESM-workflow')

# method
f.attr('node', shape='box')
f.node('Latin hypercube sampling')
f.node('Aerosol mixing state indexes emulator')

# data
f.attr('node', shape='cylinder')
f.node('PartMC-MOSAIC training data (scenarios)')
f.node('PartMC-MOSAIC testing data (scenarios)')
f.node('CESM (CAM) outputs')

# output
f.attr('node', shape='folder')
f.node('Global aerosol mixing state indexes')

# Get PartMC scenarios
with f.subgraph(name='cluster_1') as c:
    c.attr(color='blue')
    c.node_attr['style'] = 'filled'
    c.edges([('Latin hypercube sampling', 'PartMC-MOSAIC training data (scenarios)'), 
             ('Latin hypercube sampling', 'PartMC-MOSAIC testing data (scenarios)')])
    c.attr(label='Blue Waters (scalable simulations)')


# Machine Learning
f.edge('PartMC-MOSAIC training data (scenarios)', 'Aerosol mixing state indexes emulator', label='Machine Learning')
f.edge('Aerosol mixing state indexes emulator', 'PartMC-MOSAIC testing data (scenarios)', label='Validation')
f.edge('Aerosol mixing state indexes emulator', 'Global aerosol mixing state indexes', label='Application')

# Application
"""
with f.subgraph(name='cluster_2') as b:
    b.attr(color='purple')
    b.node_attr['style'] = 'filled'
    b.edges([('CESM (CAM) outputs', 'Global aerosol mixing state indexes'), 
             ('Aerosol mixing state indexes emulator', 'Global aerosol mixing state indexes')])
    b.attr(label='Cheyenne')
""" 
with f.subgraph(name='cluster_2') as b:
    b.attr(color='purple')
    b.node_attr['style'] = 'filled'
    b.edges([('CESM (CAM) outputs', 'Global aerosol mixing state indexes')])
    b.attr(label='Cheyenne or Blue Waters')


    
f.view()
