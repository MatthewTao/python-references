from nicegui import ui


def declarative_method():
    # Using the dictionary declarative method is more performant according to docs
    fig = {
        "data": [
            {
                "type": "pie",
                "name": "Testing",
                "values": [1, 2, 3, 4],
                "labels": ["something", "else", "blah", "foo"],
            },
        ],
        "layout": {
            "margin": {"l": 0, "r": 0, "t": 30, "b": 15},
            "plot_bgcolor": "#E5ECF6",
            "title": {"text": "sample figure"},
        },
    }
    ui.plotly(fig).classes("h-200")


if __name__ == "__main__":
    declarative_method()
    ui.run(reload=False, dark=True, show=False)
