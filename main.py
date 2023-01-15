from flask import Flask, render_template, request, send_file
from werkzeug.utils import redirect
from rem import get_rem
from sof import get_sof
from wwr import get_wwr
from sort import sorted_list
from save import save_to_file

app = Flask("Job Search")

db = {}


@app.route("/")
def home():
    '''
    HOME
    '''
    job_list = []
    for i in db:
        job_list.append(i)
    print(job_list)
    return render_template("home.html", jobs=job_list)


@app.route("/search")
def search():
    '''
    SEARCH
    '''
    job = request.args.get("job")
    job = job.lower()
    if job in db:
        print("Done")
        jobs = db[job]
    else:
        sof = get_sof(job)
        rem = get_rem(job)
        wwr = get_wwr(job)
        result_li = sorted_list(wwr, sof, rem)
        db[job] = result_li
        jobs = db[job]
    num = len(jobs)
    for x in jobs:
        print(x)

    return render_template("read.html", jobs=jobs, name=job, num=num)


@app.route("/export")
def export():
    '''
    '''
    try:
        job = request.args.get("job")
        print(job)
        if not job:
            raise Exception()
        job = job.lower()
        jobs = db.get(job)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file('jobs.csv', mimetype='application/x-csv', download_name=f'{job}_joblist.csv', as_attachment=True)
    except:
        return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
