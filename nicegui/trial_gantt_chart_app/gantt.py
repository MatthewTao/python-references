from datetime import date

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def build_gantt(tasks: list[dict]) -> go.Figure:
    if not tasks:
        fig = go.Figure()
        fig.update_layout(
            title="Project Gantt Chart",
            xaxis_title="Date",
            yaxis_title="Task",
            annotations=[{
                "text": "No tasks yet — add a task to get started.",
                "xref": "paper", "yref": "paper",
                "x": 0.5, "y": 0.5,
                "showarrow": False,
                "font": {"size": 16, "color": "grey"},
            }],
        )
        return fig

    df = pd.DataFrame(tasks)
    df["depends_on"] = df["depends_on"].fillna("")

    fig = px.timeline(
        df,
        x_start="start_date",
        x_end="end_date",
        y="task_name",
        color="task_name",
        hover_data={"duration": True, "depends_on": True, "task_name": False},
        title="Project Gantt Chart",
    )
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(showlegend=False, xaxis_title="Date", yaxis_title="Task")
    _add_today_line(fig)
    return fig


def _add_today_line(fig: go.Figure) -> None:
    today = date.today().isoformat()
    fig.add_shape(
        type="line",
        x0=today, x1=today,
        y0=0, y1=1,
        xref="x", yref="paper",
        line={"dash": "dash", "color": "red", "width": 1.5},
    )
    fig.add_annotation(
        x=today, y=1,
        xref="x", yref="paper",
        text="Today",
        showarrow=False,
        yshift=10,
        font={"color": "red"},
    )
