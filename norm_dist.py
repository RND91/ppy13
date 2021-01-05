import statistics as st
import plotly.figure_factory as ff
import pandas as pd 
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
mean = sum(df["math score"])/len(df["math score"])
median = st.median(df["math score"])
mode = st.mode(df["math score"])
print(mean,median,mode)

stdev = st.stdev(df["math score"])
range1s,range1e = mean - stdev,mean+stdev
range2s,range2e = mean - stdev*2,mean+stdev*2
range3s,range3e = mean - stdev*3,mean +stdev*3

range1 = [result for result in df["math score"] if result > range1s and result < range1e]
p1 = len(range1)*100/len(df["math score"])
range2 = [result for result in df["math score"] if result > range2s and result < range2e]
p2 = len(range2)*100/len(df["math score"])
range3 = [result for result in df["math score"] if result > range3s and result < range3e]
p3 = len(range3)*100/len(df["math score"])

print(f"{p1:f}% of data falls within first standard deviation")
print(f"{p2:f}% of data falls within second standard deviation")
print(f"{p3:f}% of data falls within third standard deviation")

fig = ff.create_distplot([df["math score"]],["Math Scores"],show_hist=True)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.04], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[range1s, range1s], y=[0, 0.04], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[range1e, range1e], y=[0, 0.04], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[range2s, range2s], y=[0, 0.04], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[range2e, range2e], y=[0, 0.04], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()