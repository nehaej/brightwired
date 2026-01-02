from flask import Flask, render_template, request, jsonify
from summarizer import summary, read_improve, keyword_extrct
from planners import urgent, time_chunk, per_task_duration, task_order, dump
from enco import chat
from functools import lru_cache 


app = Flask(__name__)

print("I warm up ollama first to shorten time taken to gen first output")
try:
    chat("hi")
    summary("tldr","HELlO","Child Core")

except Exception as e:
    print("Error occured:",e)


@lru_cache(maxsize=50)
def cached_chat(prompt):
    return chat(prompt)


@lru_cache(maxsize=50)
def cached_summary(length, text, mode):
    return summary(length, text, mode)


@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/about')
def info():
    return render_template("info.html")

@app.route("/features")
def features():
    return render_template('features.html')


@app.route("/planner", methods=["GET","POST"])
def planner():
        if request.method == "GET" :
            return render_template("planner-final.html", plan="Plan will be here aft submission")
        vv_urg = []
        v_urg = []
        urg = []
        med_urg = []
        low_urg = []
        task_info ={}
        urgency_list = []

        focus_lvl = request.form.get(f"focus-level")
        duration = int(request.form.get("duration", 0) or 0)
        for i in range(1,6) :
            task_name = request.form.get(f"task{i}")
            deadline_days = int(request.form.get(f"days-{i}",0) or 0)
            deadline_hours = int(request.form.get(f"hours-{i}",0) or 0)
            deadline = deadline_days * 24 * 60 + deadline_hours * 60
            if not task_name or not deadline:
                continue
            urgency = urgent(deadline)
            urgency_list.append((task_name, urgency))
        mapping_weight = {"Very Very Urgent": 5,"Very Urgent": 4,"Urgent": 3,"Medium Urgency": 2,"Low Urgency": 1}
        total_weight = sum(mapping_weight.get(urgency, 0) for _, urgency in urgency_list)

        time_chunks = time_chunk(focus_lvl)
        for task_name, urgency in urgency_list:
            if urgency == "Very Very Urgent" :
                vv_urg.append(task_name)
            elif urgency == "Very Urgent" :
                v_urg.append(task_name)
            elif urgency == "Urgent" :
                urg.append(task_name)
            elif urgency == "Medium Urgency" :
                med_urg.append(task_name)
            else :
                low_urg.append(task_name)
            time_per_task = per_task_duration(urgency,total_weight,duration)
            task_info[task_name] = time_per_task
        tasks = task_order(vv_urg, v_urg, urg, med_urg, low_urg, task_info)
        if total_weight == 0 :
            return render_template("planner-final.html", plan="Please enter at least one task with a valid deadline.")
        else :
            return render_template("planner-final.html", plan=tasks + "\n" + time_chunks)
        
@app.route("/sorter", methods=["GET","POST"])
def sorter() :
    todo = ""
    if request.method == "POST" :
        thought = request.form.get("text")
        todo = dump(thought)
        if request.headers.get("X-Requested-With") == "fetch":
            return jsonify({"tasks": todo})

    return render_template("sorter.html", todo=[])


@app.route("/timer")
def timer():
    return render_template("timer.html")

@app.route("/enco", methods=["GET", "POST"])
def enco(): 
    reply = ""
    if request.method == "POST" :
        prompt = request.form.get("enco-input")
        reply = cached_chat(prompt)

    return render_template("enco-bot.html", reply=reply)


@app.route("/summarizer", methods=["GET","POST"])
def summarizer():
    if request.method == "POST" :
        mode = request.form.get("mode")
        summary_length = request.form.get("length")
        text = request.form.get("text")
        output = cached_summary(summary_length,text,mode)
        improve = read_improve(text,output)
        keywords = keyword_extrct(output)

        if request.headers.get("X-Requested-With") == "fetch":
            return jsonify({"output": output, "improve": improve, "keywords": keywords})
        
    return render_template("summarizer.html", output=None, improve=None, keywords=[])

        
if __name__ == '__main__':
    app.run(debug=True,port=5000)