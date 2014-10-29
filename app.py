import falcon
import index
import images
import readjson
import parsejson
from mysql_libs import findall
from mysql_libs import findbyphone


app = falcon.API()

index = index.Index()
images = images.Resource()
readjson = readjson.ReadJson()
findall = findall.FindAll()
findbyphone = findbyphone.FindByPhone()
parsejson = parsejson.ParseJson()

app.add_route('/', index)
app.add_route('/images', images)
app.add_route('/readjson', readjson)
app.add_route('/find', findall)
app.add_route('/find/{user_phone}', findbyphone)
app.add_route('/parse', parsejson)
