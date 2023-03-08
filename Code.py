import pygal
line_chart = pygal.StackedLine(fill=True)
line_chart.title = 'Crop yield changes from 2002 to 2012'
line_chart.x_labels = map(str, range(2002, 2013))
line_chart.add('Wheat', [None, None, 0, 3562,   3648,   3758, 3452, 3365, 2758, 3100, 3900])
line_chart.add('Barley',  [None, None, None, None, None, None,    2010,  2510, 2685, 2896, 2335])
line_chart.add('Canola',      [2800, 2852, 2954, 2750,   2666, 2516, 2657, 2410, 2300, 2100, 1900])
line_chart.add('Soybean',  [2500, 1520, 1652,  1800,    1865, 1758,  1798,  1658,  1954,  2100,  1950])
line_chart.render()
line_chart.render_to_file('line_chart.svg')
