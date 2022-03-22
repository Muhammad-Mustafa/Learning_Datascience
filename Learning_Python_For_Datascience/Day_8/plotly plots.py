
# %%
import plotly.express as px
from plotly.offline import plot
import matplotlib.pyplot as plt
df = px.data.gapminder()
newPlot =px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
plot(newPlot)

