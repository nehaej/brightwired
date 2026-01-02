import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

def urgent(deadline) :
            
            try :
                if deadline <= 24*60 :
                    return f"Very Very Urgent"
                elif 24*60 <= deadline <= 48*60 :
                    return f"Very Urgent"
                elif 48*60 <= deadline <= 96*60 :
                    return f"Urgent"
                elif 96*60 <= deadline <= 168*60 :
                    return f"Medium Urgency"
                else :
                    return f"Low Urgency"
                
            except (ValueError,UnboundLocalError) :
                return f"Please enter a deadline"

def time_chunk(focus) :
            
            if focus == "low":
                work_block = 25
                break_block = 10
            elif focus == "medium":
                work_block = 30
                break_block = 5
            else:
                work_block = 45
                break_block = 5
            return f"Work in {work_block} minute chunks. After that make sure to take a {break_block} minute break b4 starting the next cycle!"

def per_task_duration(task_urgency,total_weight,duration) :
            
            mapping_weight = {"Very Very Urgent":5,
                              "Very Urgent":4,
                              "Urgent":3,
                              "Medium Urgency":2,
                              "Low Urgency":1}
            task_weight = mapping_weight.get(task_urgency, 1)  
            task_time = max(1, round((task_weight / total_weight) * duration))
            return task_time

def task_order(vv_urg, v_urg, urg, med_urg, low_urg, task_info):

            try :
                result = ""
                task_list = vv_urg+v_urg+urg+med_urg+low_urg
                for i, task in enumerate(task_list, start=1) :
                    if task in task_info :
                        result += f"{i}.Work on {task} for {task_info[task]} minutes.\n"
                return result
            except IndexError as e :
                return f"Something's wrong with task ordering: {e}"
            

#planner route 2
#change braindump into todo list


def dump(text) :
    try:
        completion = client.chat.completions.create(
            extra_body={},
            model="mistralai/devstral-2512:free",
            messages=[
            {
                "role": "user",
                "content": f"Based on this user's braindump : '{text}' return short tasks. Use only simple words. COMPULSORY FORMAT: 1 Task PER line ONLY. Tasks must be ordered vertically in bulleted format. No numbering or extra text allowed."
            }
            ]
        )
        todo = completion.choices[0].message.content 
        todo = re.sub(r"<s>[OUT]","",todo)
        todo_list = re.split(r'\n| - |^- ',  todo)
        clean_tasks = [item.strip() for item in todo_list if item.strip()]

        result = "\n".join([f"- {task.lstrip('- ')}" for task in clean_tasks])

        return result
    except Exception as e :
          print(f"Error:{e}")
          return f"Please try again"


