import os
import json
import requests
from flask import Flask, request, Response

ding_api = "替换成你自己的机器人api地址"
app = Flask(__name__)

def make_dingtalk_message(data):
    if data["status"] == "firing":
        return {
            "msgtype": "markdown",
            "markdown": {
                "title": "Prometheus告警信息",
                "text": f"#### 监控指标【{data['alerts'][0]['labels']['alertname']}】\n"
                + f"> 监控描述信息【{data['alerts'][0]['annotations']['description']}】\n\n"
                + f"> ###### 告警时间【{data['alerts'][0]['startsAt']}】\n",
            },
        }
    else:
        return {
            "msgtype": "markdown",
            "markdown": {
                "title": "Prometheus告警信息",
                "text": f"#### 监控指标【{data['alerts'][0]['labels']['alertname']}】\n"
                + f"> 已解决\n\n"
                + f"> ###### 解决时间【{data['alerts'][0]['endsAt']}】\n",
            },
        }


@app.route("/message", methods=["POST", "GET"])
def handle_alertmanager_message():
    request_data = request.data.decode("utf-8")
    ding_message = make_dingtalk_message(json.loads(request_data))
    requests.post(ding_api, json=ding_message)
    return Response(json.dumps(request_data), status=200, mimetype="application/json")


if __name__ == "__main__":
    os.environ.setdefault("FLASK_ENV", "development")
    app.run(host="0.0.0.0", port=5000, debug=True)
