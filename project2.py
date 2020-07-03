from flask import *

from newsapi import NewsApiClient

import sqlite3

app = Flask(__name__)

app.secret_key = "very-secret-key"


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key='25a61f99d2984d0686d50bd728e1a1f2')

    topheadlines = newsapi.get_top_headlines(country='in')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    by = []
    time = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        by.append(myarticles['author'])
        time.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, by, time)

    conn=sqlite3.connect('news.db')

    temp1=conn.execute("select * from header")

    temp2=conn.execute("select * from footer")

    
    temp3=conn.execute("select * from metatags")

    temp4=conn.execute("select * from metadescription")

    return render_template('index.html', context=mylist, data1=temp1, data2=temp2, data3=temp3, data4=temp4)


@app.route('/technology/<Technology>')
def technology(Technology):
    newsapi = NewsApiClient(api_key='25a61f99d2984d0686d50bd728e1a1f2')

    all_articles = newsapi.get_top_headlines(
        category='technology', language='en', country='in')

    articles = all_articles['articles']

    desc = []
    news = []
    img = []
    by = []
    time = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        by.append(myarticles['author'])
        time.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, by, time)

    conn=sqlite3.connect('news.db')

    temp1=conn.execute("select * from header")

    temp2=conn.execute("select * from footer")

    temp3=conn.execute("select * from metatags")

    temp4=conn.execute("select * from metadescription")

    return render_template('ctechnology.html', context=mylist, content=Technology, data1=temp1, data2=temp2, data3=temp3, data4=temp4)


@app.route('/sports/<Sports>')
def sports(Sports):
    newsapi = NewsApiClient(api_key='25a61f99d2984d0686d50bd728e1a1f2')

    all_articles = newsapi.get_top_headlines(
        category='sports', language='en', country='in')

    articles = all_articles['articles']

    desc = []
    news = []
    img = []
    by = []
    time = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        by.append(myarticles['author'])
        time.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, by, time)

    conn=sqlite3.connect('news.db')

    temp1=conn.execute("select * from header")

    temp2=conn.execute("select * from footer")

    temp3=conn.execute("select * from metatags")

    temp4=conn.execute("select * from metadescription")

    return render_template('csports.html', context=mylist, content=Sports, data1=temp1, data2=temp2, data3=temp3, data4=temp4)


@app.route('/business/<Business>')
def business(Business):
    newsapi = NewsApiClient(api_key='25a61f99d2984d0686d50bd728e1a1f2')

    all_articles = newsapi.get_top_headlines(
        category='business', language='en', country='in')

    articles = all_articles['articles']

    desc = []
    news = []
    img = []
    by = []
    time = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        by.append(myarticles['author'])
        time.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, by, time)

    conn=sqlite3.connect('news.db')

    temp1=conn.execute("select * from header")

    temp2=conn.execute("select * from footer")

    temp3=conn.execute("select * from metatags")

    temp4=conn.execute("select * from metadescription")

    return render_template('cbusiness.html', context=mylist, content=Business, data1=temp1, data2=temp2, data3=temp3, data4=temp4)


@app.route('/health/<Health>')
def health(Health):
    newsapi = NewsApiClient(api_key='25a61f99d2984d0686d50bd728e1a1f2')

    all_articles = newsapi.get_top_headlines(
        category='health', language='en', country='in')

    articles = all_articles['articles']

    desc = []
    news = []
    img = []
    by = []
    time = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        by.append(myarticles['author'])
        time.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, by, time)

    conn=sqlite3.connect('news.db')

    temp1=conn.execute("select * from header")

    temp2=conn.execute("select * from footer")

    temp3=conn.execute("select * from metatags")

    temp4=conn.execute("select * from metadescription")

    return render_template('chealth.html', context=mylist, content=Health, data1=temp1, data2=temp2, data3=temp3, data4=temp4)


@app.route('/science/<Science>')
def design(Science):
    newsapi = NewsApiClient(api_key='25a61f99d2984d0686d50bd728e1a1f2')

    all_articles = newsapi.get_top_headlines(
        category='science', language='en', country='in')

    articles = all_articles['articles']

    desc = []
    news = []
    img = []
    by = []
    time = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        by.append(myarticles['author'])
        time.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, by, time)

    conn=sqlite3.connect('news.db')

    temp1=conn.execute("select * from header")

    temp2=conn.execute("select * from footer")

    temp3=conn.execute("select * from metatags")

    temp4=conn.execute("select * from metadescription")

    return render_template('cscience.html', context=mylist, content=Science, data1=temp1, data2=temp2, data3=temp3, data4=temp4)


@app.route('/entertainment/<Entertainment>')
def sport(Entertainment):
    newsapi = NewsApiClient(api_key='25a61f99d2984d0686d50bd728e1a1f2')

    all_articles = newsapi.get_top_headlines(
        category='entertainment', language='en', country='in')

    articles = all_articles['articles']

    desc = []
    news = []
    img = []
    by = []
    time = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        by.append(myarticles['author'])
        time.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img, by, time)

    conn=sqlite3.connect('news.db')

    temp1=conn.execute("select * from header")

    temp2=conn.execute("select * from footer")

    temp3=conn.execute("select * from metatags")

    temp4=conn.execute("select * from metadescription")

    return render_template('centertainment.html', context=mylist, content=Entertainment, data1=temp1, data2=temp2, data3=temp3, data4=temp4)


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":

        name = request.form['nm']

        email = request.form['em']

        phone = request.form['ph']

        message = request.form['msg']

        conn = sqlite3.connect('news.db')

        input = "insert into contact(name,email,phone,message)values(?,?,?,?)"

        conn.execute(input, (name, email, phone, message))

        conn.commit()

        flash('Your record is submitted. Thankyou for contacting us!')

        return redirect('/contact')

    else:

        conn=sqlite3.connect('news.db')

        temp1=conn.execute("select * from header")

        temp2=conn.execute("select * from footer")

        temp3=conn.execute("select * from metatags")

        temp4=conn.execute("select * from metadescription")

        return render_template('contact.html', data1=temp1, data2=temp2, data3=temp3, data4=temp4)


@app.route('/homepost/<time>')
def homepost(time):
    ptime = time

    newsapi = NewsApiClient(api_key='25a61f99d2984d0686d50bd728e1a1f2')

    topheadlines = newsapi.get_top_headlines(country='in')

    articles = topheadlines['articles']

    cont = []
    news = []
    img = []
    by = []
    time = []
    desc = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        cont.append(myarticles['content'])
        img.append(myarticles['urlToImage'])
        by.append(myarticles['author'])
        time.append(myarticles['publishedAt'])
        desc.append(myarticles['description'])

    mylist = zip(news, cont, img, by, time, desc)

    conn=sqlite3.connect('news.db')

    temp1=conn.execute("select * from header")

    temp2=conn.execute("select * from footer")

    temp3=conn.execute("select * from metatags")

    temp4=conn.execute("select * from metadescription")

    return render_template('post.html', context=mylist, ptime=ptime, data1=temp1, data2=temp2, data3=temp3, data4=temp4)


@app.route('/technologypost/<time>')
def technologypost(time):
    ptime = time

    newsapi = NewsApiClient(api_key='25a61f99d2984d0686d50bd728e1a1f2')

    topheadlines = newsapi.get_top_headlines(
        category='technology', language='en', country='in')

    articles = topheadlines['articles']

    cont = []
    news = []
    img = []
    by = []
    time = []
    desc = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        cont.append(myarticles['content'])
        img.append(myarticles['urlToImage'])
        by.append(myarticles['author'])
        time.append(myarticles['publishedAt'])
        desc.append(myarticles['description'])

    mylist = zip(news, cont, img, by, time, desc)

    conn=sqlite3.connect('news.db')

    temp1=conn.execute("select * from header")

    temp2=conn.execute("select * from footer")

    temp3=conn.execute("select * from metatags")

    temp4=conn.execute("select * from metadescription")

    return render_template('post.html', context=mylist, ptime=ptime, data1=temp1, data2=temp2, data3=temp3, data4=temp4)


@app.route('/sportspost/<time>')
def sportspost(time):
    ptime = time

    newsapi = NewsApiClient(api_key='25a61f99d2984d0686d50bd728e1a1f2')

    topheadlines = newsapi.get_top_headlines(
        category='sports', language='en', country='in')

    articles = topheadlines['articles']

    cont = []
    news = []
    img = []
    by = []
    time = []
    desc = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        cont.append(myarticles['content'])
        img.append(myarticles['urlToImage'])
        by.append(myarticles['author'])
        time.append(myarticles['publishedAt'])
        desc.append(myarticles['description'])

    mylist = zip(news, cont, img, by, time, desc)

    conn=sqlite3.connect('news.db')

    temp1=conn.execute("select * from header")

    temp2=conn.execute("select * from footer")

    temp3=conn.execute("select * from metatags")

    temp4=conn.execute("select * from metadescription")

    return render_template('post.html', context=mylist, ptime=ptime, data1=temp1, data2=temp2, data3=temp3, data4=temp4)


@app.route('/businesspost/<time>')
def businesspost(time):
    ptime = time

    newsapi = NewsApiClient(api_key='25a61f99d2984d0686d50bd728e1a1f2')

    topheadlines = newsapi.get_top_headlines(
        category='business', language='en', country='in')

    articles = topheadlines['articles']

    cont = []
    news = []
    img = []
    by = []
    time = []
    desc = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        cont.append(myarticles['content'])
        img.append(myarticles['urlToImage'])
        by.append(myarticles['author'])
        time.append(myarticles['publishedAt'])
        desc.append(myarticles['description'])

    mylist = zip(news, cont, img, by, time, desc)

    conn=sqlite3.connect('news.db')

    temp1=conn.execute("select * from header")

    temp2=conn.execute("select * from footer")

    temp3=conn.execute("select * from metatags")

    temp4=conn.execute("select * from metadescription")

    return render_template('post.html', context=mylist, ptime=ptime, data1=temp1, data2=temp2, data3=temp3, data4=temp4)


@app.route('/healthpost/<time>')
def healthpost(time):
    ptime = time

    newsapi = NewsApiClient(api_key='25a61f99d2984d0686d50bd728e1a1f2')

    topheadlines = newsapi.get_top_headlines(
        category='health', language='en', country='in')

    articles = topheadlines['articles']

    cont = []
    news = []
    img = []
    by = []
    time = []
    desc = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        cont.append(myarticles['content'])
        img.append(myarticles['urlToImage'])
        by.append(myarticles['author'])
        time.append(myarticles['publishedAt'])
        desc.append(myarticles['description'])

    mylist = zip(news, cont, img, by, time, desc)

    conn=sqlite3.connect('news.db')

    temp1=conn.execute("select * from header")

    temp2=conn.execute("select * from footer")

    temp3=conn.execute("select * from metatags")

    temp4=conn.execute("select * from metadescription")

    return render_template('post.html', context=mylist, ptime=ptime, data1=temp1, data2=temp2, data3=temp3, data4=temp4)


@app.route('/sciencepost/<time>')
def sciencepost(time):
    ptime = time

    newsapi = NewsApiClient(api_key='25a61f99d2984d0686d50bd728e1a1f2')

    topheadlines = newsapi.get_top_headlines(
        category='science', language='en', country='in')

    articles = topheadlines['articles']

    cont = []
    news = []
    img = []
    by = []
    time = []
    desc = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        cont.append(myarticles['content'])
        img.append(myarticles['urlToImage'])
        by.append(myarticles['author'])
        time.append(myarticles['publishedAt'])
        desc.append(myarticles['description'])

    mylist = zip(news, cont, img, by, time, desc)

    conn=sqlite3.connect('news.db')

    temp1=conn.execute("select * from header")

    temp2=conn.execute("select * from footer")

    temp3=conn.execute("select * from metatags")

    temp4=conn.execute("select * from metadescription")

    return render_template('post.html', context=mylist, ptime=ptime, data1=temp1, data2=temp2, data3=temp3, data4=temp4)


@app.route('/entertainmentpost/<time>')
def entertainmentpost(time):
    ptime = time

    newsapi = NewsApiClient(api_key='25a61f99d2984d0686d50bd728e1a1f2')

    topheadlines = newsapi.get_top_headlines(
        category='entertainment', language='en', country='in')

    articles = topheadlines['articles']

    cont = []
    news = []
    img = []
    by = []
    time = []
    desc = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        cont.append(myarticles['content'])
        img.append(myarticles['urlToImage'])
        by.append(myarticles['author'])
        time.append(myarticles['publishedAt'])
        desc.append(myarticles['description'])

    mylist = zip(news, cont, img, by, time, desc)

    conn=sqlite3.connect('news.db')

    temp1=conn.execute("select * from header")

    temp2=conn.execute("select * from footer")

    temp3=conn.execute("select * from metatags")

    temp4=conn.execute("select * from metadescription")

    return render_template('post.html', context=mylist, ptime=ptime, data1=temp1, data2=temp2, data3=temp3, data4=temp4)


# Admin Panel Routes#


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None

    if request.method == 'POST':

        username = request.form['un']

        session["username"] = username

        password = request.form['pass']

        conn = sqlite3.connect('news.db')

        data = conn.execute("select * from login")

        for row in data:

            if (username == row[1]) and (password == row[2]):

                flash('You were successfully logged in')

                return redirect('/dashboard')

            else:

                error = 'Invalid username or password. Please try again!'

                return render_template('login.html', error=error)

    else:

        return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' in session:

        conn=sqlite3.connect('news.db')

        temp1=conn.execute("select * from header")

        temp2=conn.execute("select * from footer")

        return render_template('dashboard.html', data1=temp1, data2=temp2)

    else:

        return render_template('login.html')


@app.route('/managecontacts')
def managecontacts():
    if 'username' in session:

        conn = sqlite3.connect('news.db')

        temp = conn.execute("select * from contact")

        conn.commit()

        temp1=conn.execute("select * from header")

        temp2=conn.execute("select * from footer")

        return render_template('managecontacts.html', data=temp, data1=temp1, data2=temp2)

    else:

        return render_template('/login.html')


@app.route('/deletecontact/<int:id>')
def deletecontact(id):
    if 'username' in session:
        conn = sqlite3.connect('news.db')

        conn.execute("delete from contact where id=?", (id,))

        conn.commit()

        flash('Deleted successfully')

        return redirect('/managecontacts')

    else:

        return render_template('login.html')


@app.route('/settings')
def settings():
    if 'username' in session:

        conn = sqlite3.connect('news.db')

        temp1 = conn.execute("select * from header")

        temp2 = conn.execute("select * from footer")

        return render_template('setting.html', data1=temp1, data2=temp2)

    else:

        return render_template('login.html')


@app.route('/editheader/<int:id>')
def editheader(id):
    if 'username' in session:

        conn = sqlite3.connect('news.db')

        temp1 = conn.execute("select * from header where id=?", (id,))

        temp2 = conn.execute("select * from footer")

        return render_template('editheader.html', data1=temp1, data2=temp2)

    else:

        return render_template('login.html')


@app.route('/updateheader/<int:id>', methods=['POST', 'GET'])
def updateheader(id):

    update1 = None

    if 'username' in session:

        

        if request.method == 'POST':
            header = request.form['hd']

            conn = sqlite3.connect('news.db')

            change = "update header set title=? where Id=?"
            data = (header, id)

            conn.execute(change, data)

            conn.commit()

            update1 = 'Updated Successfully'

            temp1=conn.execute("select * from header")

            temp2=conn.execute("select * from footer")

            return render_template('setting.html', update1=update1, data1=temp1, data2=temp2)

    else:

        return render_template('login.html')


@app.route('/editfooter/<int:id>')
def editfooter(id):
    if 'username' in session:

        conn = sqlite3.connect('news.db')

        temp1 = conn.execute("select * from header")

        temp2 = conn.execute("select * from footer where id=?", (id,))

        return render_template('editfooter.html', data1=temp1, data2=temp2)

    else:

        return render_template('login.html')


@app.route('/updatefooter/<int:id>', methods=['POST', 'GET'])
def updatefooter(id):

    update2 = None
    if 'username' in session:

        

        if request.method == 'POST':
            footer = request.form['ft']

            conn = sqlite3.connect('news.db')

            change = "update footer set title=? where Id=?"
            data = (footer, id)

            conn.execute(change, data)

            conn.commit()

            update2 = 'Updated Successfully'

            temp1=conn.execute("select * from header")

            temp2=conn.execute("select * from footer")

            return render_template('setting.html', update2=update2, data1=temp1, data2=temp2)

    else:

        return render_template('login.html')


@app.route('/seo')
def seo():
    if 'username' in session:

        conn = sqlite3.connect('news.db')

        temp1 = conn.execute("select * from metatags")

        conn.commit()

        temp2 = conn.execute("select * from metadescription")

        conn.commit()

        temp3=conn.execute("select * from header")

        temp4=conn.execute("select * from footer")

        return render_template('seo.html', data1=temp1, data2=temp2, data3=temp3, data4=temp4)

    else:

        return render_template('login.html')


@app.route('/deletemetatag/<int:id>')
def deletemetatag(id):

    delete1 = None

    if 'username' in session:
        conn = sqlite3.connect('news.db')

        conn.execute("delete from metatags where id=?", (id,))

        conn.commit()

        delete1 = 'Deleted Successfully'

        temp1=conn.execute("select * from metatags")

        conn.commit()

        temp2=conn.execute("select * from metadescription")

        temp3=conn.execute("select * from header")

        temp4=conn.execute("select * from footer")

        return render_template('seo.html', delete1=delete1, data1=temp1, data2=temp2, data3=temp3, data4=temp4)

    else:

        return render_template('login.html')


@app.route('/deletemetadescription/<int:id>')
def deletemetadescription(id):

    delete2 = None

    if 'username' in session:
        conn = sqlite3.connect('news.db')

        conn.execute("delete from metadescription where id=?", (id,))

        conn.commit()

        delete2 = 'Deleted Successfully'

        temp1=conn.execute("select * from metatags")

        temp2=conn.execute("select * from metadescription")

        temp3=conn.execute("select * from header")

        temp4=conn.execute("select * from footer")

        return render_template('seo.html', delete2=delete2, data1=temp1, data2=temp2, data3=temp3, data4=temp4)

    else:

        return render_template('login.html')


@app.route('/addmetatag', methods=['POST', 'GET'])
def addmetatag():

    add1 = None

    if 'username' in session:

        if request.method == 'POST':
            tag = request.form['mtg']

            conn = sqlite3.connect('news.db')

            conn.execute("insert into metatags(tagname)values(?)", (tag,))

            conn.commit()

            add1 = 'Added Successfully'

            temp1=conn.execute("select * from metatags")

            temp2=conn.execute("select * from metadescription")

            temp3=conn.execute("select * from header")

            temp4=conn.execute("select * from footer")

            return render_template('seo.html', add1=add1, data1=temp1, data2=temp2, data3=temp3, data4=temp4)

        else:

            return render_template('seo.html')

    else:

        return render_template('login.html')


@app.route('/addmetadescription', methods=['POST', 'GET'])
def addmetadescription():
    if 'username' in session:

        add2 = None

        if request.method == 'POST':
            tag = request.form['mds']

            conn = sqlite3.connect('news.db')

            conn.execute("insert into metadescription(tagdescription)values(?)", (tag,))

            conn.commit()

            add2 = 'Added Successfully'

            temp1=conn.execute("select * from metatags")

            temp2=conn.execute("select * from metadescription")

            temp3=conn.execute("select * from header")

            temp4=conn.execute("select * from footer")

            return render_template('seo.html', add2=add2, data1=temp1, data2=temp2, data3=temp3, data4=temp4)

        else:

            return render_template('seo.html')

    else:

        return render_template('login.html')


@app.route('/editmetatag/<int:id>')
def editmetatag(id):
    if 'username' in session:

        conn = sqlite3.connect('news.db')

        temp = conn.execute("select * from metatags where id=?", (id,))

        temp1 = conn.execute("select * from header")

        temp2 = conn.execute("select * from footer")

        return render_template('editmetatag.html', data=temp, data1=temp1, data2=temp2)

    else:

        return render_template('login.html')


@app.route('/updatemetatag/<int:id>', methods=['POST', 'GET'])
def updatemetetag(id):
    if 'username' in session:

        update1 = None

        if request.method == 'POST':
            tag = request.form['mtg']

            conn = sqlite3.connect('news.db')

            change = "update metatags set tagname=? where Id=?"
            data = (tag, id)

            conn.execute(change, data)

            conn.commit()

            update1 = 'Updated Successfully'

            temp1=conn.execute("select * from metatags")

            temp2=conn.execute("select * from metadescription")

            temp3=conn.execute("select * from header")

            temp4=conn.execute("select * from footer")

            return render_template('seo.html', update1=update1, data1=temp1, data2=temp2, data3=temp3, data4=temp4)

    else:

        return render_template('login.html')


@app.route('/editmetadescription/<int:id>')
def editmetadescription(id):
    if 'username' in session:

        conn = sqlite3.connect('news.db')

        temp = conn.execute("select * from metadescription where id=?", (id,))

        temp1 = conn.execute("select * from header")

        temp2 = conn.execute("select * from footer")

        return render_template('editmetadescription.html', data=temp, data1=temp1, data2=temp2)

    else:

        return render_template('login.html')


@app.route('/updatemetadescription/<int:id>', methods=['POST', 'GET'])
def updatemetadescription(id):
    if 'username' in session:

        update2 = None

        if request.method == 'POST':
            tag = request.form['mds']

            conn = sqlite3.connect('news.db')

            change = "update metadescription set tagdescription=? where Id=?"
            data = (tag, id)

            conn.execute(change, data)

            conn.commit()

            update2 = 'Updated Successfully'

            temp1=conn.execute("select * from metatags")

            temp2=conn.execute("select * from metadescription")

            temp3=conn.execute("select * from header")

            temp4=conn.execute("select * from footer")

            return render_template('seo.html', update2=update2, data1=temp1, data2=temp2, data3=temp3, data4=temp4)

    else:

        return render_template('login.html')


@app.route('/changelogin')
def changelogin():
    if 'username' in session:

        conn = sqlite3.connect('news.db')

        temp = conn.execute("select * from login")
        
        temp1=conn.execute("select * from header")

        temp2=conn.execute("select * from footer")

        return render_template('changelogin.html', data=temp, data1=temp1, data2=temp2)

    else:

        return render_template('/login.html')


@app.route('/editlogin/<int:id>')
def editlogin(id):
    if 'username' in session:

        conn = sqlite3.connect('news.db')

        temp = conn.execute("select * from login where id=?", (id,))

        temp1 = conn.execute("select * from header")

        temp2 = conn.execute("select * from footer")

        return render_template('editlogin.html', data=temp, data1=temp1, data2=temp2)

    else:

        return render_template('login.html')


@app.route('/updatelogin/<int:id>', methods=['POST', 'GET'])
def updatelogin(id):
    if 'username' in session:

        if request.method == 'POST':
            username = request.form['un']

            password = request.form['pd']

            conn = sqlite3.connect('news.db')

            change = "update login set username=?, password=? where id=?"

            data = (username, password, id)

            conn.execute(change, data)

            conn.commit()

            flash('Updated successfully')

            return redirect('/changelogin')

    else:

        return render_template('/login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)

    flash('Logged out successfully!')

    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)
