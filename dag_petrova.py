from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator
import random

def hello():
    print ("Airflow")
    
def int_random():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    with open('file.txt', 'a', encoding='utf-8') as fout:
        print(*[a, b], file=fout)

def dif_column():
    with open('file.txt', 'r', encoding='utf-8') as f:
        for i in f:
           a = i.strip().split(' ')
        x = int(a[0])
        ar_x = np.array(x)
        y = int(a[1])
        ar_y = np.array(y)
        sum_x = np.sum(ar_x)
        sum_y = np.sum(ar_y)
        dif_xy = sum_x - sum_y
    with open ('file.txt', 'a', encoding='utf-8') as f:
        print(*[dif_xy], file=f)
        
# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="petrova_dag", start_date=datetime(2022, 12, 20), schedule="55/1 0 * * *") as dag:
    #tasks are represented as operators
    bash_task = BashOperator(task_id="hello", bash_command="echo hello")
    python_task = PythonOperator(task_id="world", python_callable = hello)
    python_task_random = PythonOperator(task_id="int", python_callable = int_random)
    python_task_dif = PythonOperator(task_id="dif", python_callable = dif_column)
    #set dependencies between tasks
    bash_task >> python_task >> python_task_random >> python_task_dif