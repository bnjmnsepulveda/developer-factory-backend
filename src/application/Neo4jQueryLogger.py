
def log_query(query, params):
    # format query
    formatted_query = ''
    for x in query.strip().split('\n'):
        formatted_query += f'{x.strip()}\n'
    query = formatted_query.strip()
    # append properties
    for k, v in params.items():
        key = f'${k}'
        value = f'"{v}"' if not v.isdigit() else f'{v}'
        query = query.replace(key, value)
    # write logfile
    with open('queries.log', 'a') as f:
        close_query = ';' if query[-1] != ';' else ''
        final_query = f'{query}{close_query}\n'
        print(final_query)
        f.write(final_query)
