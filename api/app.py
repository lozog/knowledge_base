from flask import Flask

import routes

app = Flask(__name__)

app.register_blueprint(routes.blueprint)

print(
    """
 __   ___  _______   
|/"| /  ")|   _  "\  
(: |/   / (. |_)  :) 
|    __/  |:     \/  
(// _  \  (|  _  \\  
|: | \  \ |: |_)  :) 
(__|  \__)(_______/  
"""
)
APP_HOST="localhost"
APP_DEBUG=True

# Start the show...
if __name__ == "__main__":
    app.run(host=APP_HOST, debug=APP_DEBUG)
