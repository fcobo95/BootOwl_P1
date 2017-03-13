#User Manual

#Introduction

This manual is focused on explaining the core functionalities that Boot Owl can perform.

#Methods

#Instance Initialization

app = Flask(\_\_name\_\_)

#Mongo Data Base Connection

The following lines of code allow us to connect to our MongoDB located in mlab, which extends from Amazon Web Services. This method is wrapped in between a try-except, in case the DB is down.

uri = "mongodb://:@ds153609.mlab.com:53609/bootowl" client = MongoClient(uri) data_base = client.get_default_database() data_base_test = client.test This allows the API to connect to the data base, in order to provide the user with the core functionalities that the RESTful API can offer.
client = MongoClient(uri)
data_base = client.get_default_database()

#Learn Method app.route('/learn/') INSERT (C)

Allows Boot Owl to learn new actions. This method received to arguments in POSTMAN parameters, these two are: "action_code" and "name. One is the code or action code that Boot Owl will learn, and creates a new document in the MongoDB "Boot Owl Activity Log" collection with the name it was assigned as a parameter.

#State Method app.route('/log/') GET (R)

Prints out to screen in JSON format a log of all the action performed by Boot Owl.

#Memory app.route('/state/')

Prints in JSON format, all the possible states that Boot Owl could be in. 

#Update Method app.route('/update/\<doc_id>/') UPDATE (U)

Allows Boot Owl to update an action he previously learned. This function takes a parameter in the url which is "doc_id". With this id, we will be able to update a certain action. The way you rename the doc_id you have chosen is by sending it parameters through POSTMAN, this parameter in arguments is called "new_name". This will be the updated name of the previous doc_id name. 

#Forget Method app.route('/forget/\<name>') DELETE (D)

Allows Boot Owl to forget an action he previously learned. This function takes a parameter in the url which is "name". With this name, we will be able to forget a certain action. This deletes the collection document that contains that name.

###The previous methods comply with the CRUD standards. 

#Execute Action app.route('execute-action/\<name>'')

This method is dangerous, I've read throughout the internet, that the use of the exec and eval functions are dangerous, but for purposes of learning, I have extended this ability for Boot Owl to be able to perform an action that a client desiers it to do.

#Default Route Method app.route('/')

This is just a rendered html file which greets the user. This is known as the default home page for Boot Owl.
