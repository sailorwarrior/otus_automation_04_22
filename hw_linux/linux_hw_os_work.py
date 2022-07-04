import collections
from datetime import datetime
from subprocess import run


def ps_aux_parser():
    newline = '\n'
    ps = run(["ps", "aux"], capture_output=True)
    out = str(ps.stdout)[2:-3]
    rows = out.split(r'\n')
    filtered_rows = [list(filter(None, row.split(' '))) for row in rows]
    new_filtered_rows = [row[:10] + [' '.join(row[10:])] for row in filtered_rows]
    users = [row[0] for row in new_filtered_rows[1:]]
    counts = collections.Counter(users)
    sorted_users = sorted(users, key=lambda x: -counts[x])
    unique_users = []
    for user in sorted_users:
        if user not in unique_users:
            unique_users.append(user)
    process_names = [row[-1] for row in new_filtered_rows[1:]]
    cpu_usages = [float(row[2]) for row in new_filtered_rows[1:]]
    mem_usages = [float(row[5]) / 1024 for row in new_filtered_rows[1:]]
    max_cpu_index = cpu_usages.index(max(cpu_usages))
    max_ram_index = mem_usages.index(max(mem_usages))

    report = f"""Пользователи системы: '{"','".join(unique_users)}'
Процессов запущено: {len(new_filtered_rows) - 1}
Пользовательских процессов:{newline} {" ".join([f"{user} : {counts[user]},{newline}" for user in unique_users])}
Всего памяти используется: {round(sum(mem_usages), 2)} Mb
Всего CPU используется: {round(sum(cpu_usages), 2)}%
Больше всего памяти использует: {process_names[max_ram_index][:20]}, используется {round(mem_usages[max_ram_index], 2)} Mb
Больше всего CPU использует: {process_names[max_cpu_index][:20]}  используется {round(cpu_usages[max_cpu_index], 2)}%
    """

    date_format = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")
    file_object = open(f'{date_format}-scan.txt', 'w')
    file_object.write(report)


if __name__ == '__main__':
    ps_aux_parser()
