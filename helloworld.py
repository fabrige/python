import webapp2
import cgi
import string

def escape_html(s):
    return cgi.escape(s, quote = True)

form = """
<form method="post">
    Enter some text ?
    <br>
<textarea rows="4" cols="50" name="textToEncrypt">%(textToEncrypt)s</textarea>
 
    <div style="color: red">%(error)s</div>
    <br><br>
    <input type="submit">
</form>
"""

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                        'September', 'October', 'November', 'December']
intab="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
outab="nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"

def valid_day(day):
        if(day and day.isdigit()):
                day = int(day)
        if(day < 32 and day > 0):
                return day

def valid_month(month):
        if(month):
                month = month.capitalize()
        if(month in months):
                return month

def valid_year(year):
        if(year and year.isdigit()):
                year = int(year)
        if(year < 2020 and year > 1880):
                return year

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="",textToEncrypt=""):
        self.response.out.write(form %{"error": error,"textToEncrypt":textToEncrypt})

    def get(self):
        self.write_form()

    def post(self):
        textToEncrypt = self.request.get('textToEncrypt')
        textToEncrypt=textToEncrypt.encode('ascii')
        trantab = string.maketrans(intab, outab)
        encryptedText=textToEncrypt.translate(trantab)
  

                
        self.write_form("",encryptedText)


app = webapp2.WSGIApplication([('/', MainPage)],
                             debug=True)
