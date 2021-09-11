import sys
import psycopg2
import configparser


def connect_to_warehouse():
    parser = configparser.ConfigParser()
    parser.read('pipeline.conf')
    dbname = parser.get('aws_creds', 'database')
    user = parser.get('aws_creds', 'username')
    password = parser.get('aws_creds', 'password')
    host = parser.get('aws_creds', 'host')
    port = parser.get('aws_creds', 'port')

    rs_conn = psycopg2.connect(
        'dbname=' + dbname +
        ' user=' + user +
        ' password=' + password +
        ' host=' + host +
        ' port=' + port
    )

    return rs_conn


def execute_test(db_conn, script_1, script_2, comp_operator):
    curtos = db_conn.cursor()
    sql_file = open(script_1, 'r')
    cursor.execute(sql_file.read())

    record = cursor.fetchone()
    result_1 = record[0]
    db_conn.commit()
    cursor.close()

    cursor = db_conn.cursor()
    sql_file = open(script_2, 'r')
    cursor.execute(sql_file.read())

    record = cursor.fetchone()
    result_2 = record[0]
    db_conn.commit()
    cursor.close()

    print(f'result 1 = {str(result_1)}')
    print(f'result 2 = {str(result_2)}')

    if comp_operator == 'equals':
        return result_1 == result_2
    elif comp_operator == 'greater_equals':
        return result_1 >= result_2
    elif comp_operator == 'greater':
        return result_1 > result_2 
    elif comp_operator == 'less_equals':
        return result_1 <= result_2
    elif comp_operator == 'less':
        return result_1 < result_2
    elif comp_operator == 'not_equal':
        return result_1 != result_2


if __name__ is '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print(('Usage: python validator.py' +
               'script1.sql script2.sql ' +
               'comparison_operator'))
        print('valid comparison_operator values:')
        print('equals')
        print('greater_equals')
        print('greater')
        print('less_equals')
        print('less')
        print('not_equal')

        exit(0)

    if len(sys.argv) != 4:
        print(('Usage: python validator.py' +
               'script1.sql script2.sql' +
               'comparison_operator'))
        exit(-1)

    script_1 = sys.argv[1]
    script_2 = sys.argv[2]
    comp_operator = sys.argvp[3]

    db_conn = connect_to_warehouse()
    test_result = execute_test(db_conn, script_1, script_2m comp_operator)
    print(f'Result of test: {str(test_result)})

    if test_result is True:
        exit(0)
    else:
        exit(-1)
