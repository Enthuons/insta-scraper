from flask import Flask, render_template, request, redirect, url_for, send_from_directory, send_file
from main import download_post

UPLOAD_FOLDER = 'download_post'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        post_url = request.form.get('post_url')
        post_url_list = post_url.split('/')
        print(post_url_list[len(post_url_list)-2])
        url = post_url_list[len(post_url_list)-2]
        media_type = post_url_list[len(post_url_list)-3]
        fn = download_post(url,media_type)
        #download_file(fn)
        #return redirect(url_for('index'))
        return render_template('index.html', fn=fn)
    return render_template('index.html')

@app.route('/download_post',methods=['GET'])
def download_file():
    #return send_from_directory(app.config['UPLOAD_FOLDER'],
                                #'shipping_plan.tsv')

    args = request.args
    fn = args.get("fn")
    try:
        return send_file(app.config['UPLOAD_FOLDER']+'/'+fn, as_attachment=True)
    except:
        fn = fn[:-6]
        fn += '.jpg'
        return send_file(app.config['UPLOAD_FOLDER'] + '/' + fn, as_attachment=True)

if __name__ == "__main__" :
    app.run(debug=True)