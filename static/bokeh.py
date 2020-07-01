x = np.random.uniform(-1, 1, 100)
y = np.random.uniform(-1, 1, 100)
s = np.random.uniform(1, 10, 100)

p = figure

p.scatter(x, y, s)

save(p, 'bokeh.html')

script, div = components(p)

div

#  IFrame(.../static/bokeh.html)
