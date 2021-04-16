from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series=[{"name":'line',"data":[{"x":2,"y":7},{"x":5,"y":19},{"x":7,"y":10},{"x":13,"y":45},{"x":17,"y":6},{"x":21,"y":66},{"x":28,"y":28},{"x":30,"y":51},{"x":39,"y":44},{"x":50,"y":91}]}]
    title={"text":'My chart'}
    xAxis={"type":'linear',"title":{"text":'X-Axis data'}}
    yAxis={"type":'linear',"title":{"text":'Y-Axis data'}}
    legend={"enabled": 'true'}

    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis, legend=legend)


if __name__ == "__main__":
    app.run(debug = True, host='127.0.0.1', port=5000, passthrough_errors=True)