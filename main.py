import json
import time
from flask import Flask, request


app = Flask(__name__)


routing = 'app'
@app.route('/{}'.format(routing), methods=['POST'])
def test_api():
    """
    用于测试
    :return:
    """
    data = request.form.get('data')
    data = json.loads(data)
    number_list = data['number_list']
    number = data['number']
    sum_number = sum(number_list) + number
    result = {'sum_number':sum_number}
    result = json.dumps(result)
    time.sleep(60)

    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090) # 运行之后可以通过{本机ip}:{端口} + // {routing}网址调用, 可以参考get.py内容
