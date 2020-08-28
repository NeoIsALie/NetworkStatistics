import os
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from parse.xmlParse import *
from collections import Counter
import plotly.io

# collect data for plotting
def make_data():
    audits_path = "F:\\networkCourse\\audits"
    file_names = os.listdir(audits_path)
    values = []
    os_result = []
    proc_result = []
    video_result = []
    audio_result = []

    for f in file_names:
        osf, proc, video, audio = parse_data(f)
        os_result.append(osf)
        proc_result.append(proc)
        video_result.extend(video)
        audio_result.append(audio)

    values.append(os_result)
    values.append(proc_result)
    values.append(video_result)
    values.append(audio_result)
    for i in range(len(values)):
        counter = Counter(values[i])
        values[i] = counter
    return values

# draw hardware statistics plot 
def make_plot():
    values = make_data()
    fig = make_subplots(rows=2, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}], [{"type": "pie"}, {"type": "pie"}]],
                        subplot_titles=("OS", "Processor",
                                        "Video Card Model", "Sound"))

    fig.add_trace(
        go.Pie(labels=list(values[0].keys()), values=list(values[0].values())),
        row=1, col=1
    )

    fig.add_trace(
        go.Pie(labels=list(values[1].keys()), values=list(values[1].values())),
        row=1, col=2
    )

    fig.add_trace(
        go.Pie(labels=list(values[2].keys()), values=list(values[2].values())),
        row=2, col=1
    )

    fig.add_trace(
        go.Pie(labels=list(values[3].keys()), values=list(values[3].values())),
        row=2, col=2
    )

    fig.update_layout(height=600, width=800, title_text="Stats")
    fig.show()
    # plotly.io.write_image(fig, "F:\\networkCourse\\stats.png")
