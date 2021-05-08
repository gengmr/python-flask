import requests
import json


def post(number_list, number):
    """
    输入post请求，获取结果
    :param input:
    :return:
    """
    dict = {'number_list': number_list, 'number': number}
    json_data = json.dumps(dict)
    # 可以通过{本机ip}:{端口} + // {rounting}网址调用
    result = requests.post("http://192.168.43.38:8090//app", data={'data':json_data})
    result = json.loads(result.text)
    sum_number = result['sum_number']

    return sum_number


if __name__ == '__main__':
    number_list = [1, 2]
    number = 3
    sum_number = post(number_list=number_list, number=number)
    print(sum_number)