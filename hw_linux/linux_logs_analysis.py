import argparse
import os
import re
import json
from collections import defaultdict

dict_ip = defaultdict(
    lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0, 'CONNECT': 0, 'OPTIONS': 0, 'TRACE': 0}
)


def process_line(line, method, ip):
    time = int(line.split(' ')[-1][:-1])
    method = method.group(1)
    url = line.split('"')[3]
    ip = ip
    datetime = line.split('[')[1].split(']')[0]
    return (time, method, url, ip, datetime)


def process_log_file(filename):
    results_dict = {}
    with open(filename) as file:

        all_requests = []
        for line in file:
            ip_match = re.search(r"(\d{1,3}\.){3}\d{1,3}", line)
            if ip_match is not None:
                ip = ip_match.group()
                method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE)", line)
                if method is not None:
                    dict_ip[ip][method.group(1)] += 1
                    result_line = process_line(line, method, ip)
                    all_requests.append(result_line)
    for ip in dict_ip.keys():
        inner_dict = dict_ip[ip]
        dict_ip[ip]['total_requests'] = sum([inner_dict[key] for key in inner_dict.keys()])
    # Считаем сумму всех реквестов
    completed_requests = sum([dict_ip[ip]['total_requests'] for ip in dict_ip.keys()])
    # Собираем суммы реквестов по айпи в отдельный словарь
    total_count_dict = {ip: dict_ip[ip]['total_requests'] for ip in dict_ip.keys()}
    # Пересобираем словарь в кортеж
    pairs = ((v, k) for k, v in total_count_dict.items())
    # Сортируем кортеж по убыванию, берем первые три позиции
    pairs = sorted(pairs, reverse=True)
    top_3 = pairs[:3]
    sum_dict = {}
    # Считаем сумму по каждому типу реквеста
    for type in ['POST', 'GET', 'PUT', 'DELETE', 'HEAD', 'CONNECT', 'OPTIONS', 'TRACE']:
        sum_dict[type] = sum([dict_ip[ip][type] for ip in dict_ip.keys()])
    all_requests = sorted(all_requests, reverse=True)
    results_dict['Numbet of completed requests'] = completed_requests
    results_dict['Top 3 IPs'] = {}
    for placement, index in zip(['First', 'Second', 'Third'], [0, 1, 2]):
        results_dict['Top 3 IPs'][placement] = {'IP': '', 'Total number of requests': ''}
        results_dict['Top 3 IPs'][placement]['IP'] = top_3[index][1]
        results_dict['Top 3 IPs'][placement]['Total number of requests'] = top_3[index][0]
    results_dict['Total requests by method'] = sum_dict
    results_dict['Longest requests'] = {}
    for placement, index in zip(['First', 'Second', 'Third'], [0, 1, 2]):
        results_dict['Longest requests'][placement] = {'Method': '', 'URL': '', "IP": '', 'Duration': '',
                                                       'Datetime': ''}
        results_dict['Longest requests'][placement] = {}
        results_dict['Longest requests'][placement]['Method'] = all_requests[index][1]
        results_dict['Longest requests'][placement]['URL'] = all_requests[index][2]
        results_dict['Longest requests'][placement]['IP'] = all_requests[index][3]
        results_dict['Longest requests'][placement]['Duration'] = all_requests[index][0]
        results_dict['Longest requests'][placement]['Datetime'] = all_requests[index][4]
    result_json = json.dumps(results_dict, indent=4)
    print(result_json)
    with open(f'{filename.split(".")[-2]}_analysis.json', mode='w') as f:
        f.write(result_json)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process access.log')
    parser.add_argument('-f', dest='file', action='store', help='Path to logfile')
    parser.add_argument('-d', dest='dir', action='store', help='Path to logdir')
    args = parser.parse_args()
    if args.file is None and args.dir is None:
        raise AttributeError('File or directory for logs analysis should be provided')
    if args.dir is not None:
        directory = args.dir
        list_of_files = os.listdir(directory)
        list_of_files = [file for file in list_of_files if '.log' in file]
        for file in list_of_files:
            process_log_file(f'{directory}/{file}')
    if args.file is not None:
        process_log_file(f"{args.file}")
