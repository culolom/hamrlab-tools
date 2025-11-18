import plotly.graph_objects as go

COLOR_MAP = {
    "VOO": "#2563EB",   # 藍
    "VTI": "#1D4ED8",
    "VT":  "#22C55E",   # 綠
    "QQQ": "#A855F7",   # 紫
    "BTC": "#F97316",   # 橘
    "BTC-USD": "#F97316",
    "0050": "#F59E0B",
}

def plot_equity(series, name="Equity", ticker=None):
    color = COLOR_MAP.get(ticker, "#0EA5E9")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=series.index,
        y=series.values,
        mode="lines",
        name=name,
        line=dict(width=2.2, color=color),
    ))
    fig.update_layout(
        template="plotly_white",
        height=430,
        margin=dict(l=10, r=10, t=40, b=10),
        showlegend=False,
    )
    return fig
