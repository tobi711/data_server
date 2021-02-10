from flask_restplus import Api


api = Api(version='0.1', title='MyDemo API', description='Please use this APi')

@api.errorhandler
def std_handler(e): 
    return {'message': 'An unexpected Error occured'}, 500 

    