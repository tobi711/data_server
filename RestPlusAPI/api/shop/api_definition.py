from flask_restplus import fields 
from RestPlusAPI.api.myapi import api 


product = api.model('Product',{
    'id': fields.Integer(readOnly = True, description = 'The Product identifier'),
    'name' : fields.String (required = True, description = 'Product Name'),
})

category = api.model('Product category', {
    'id' : fields.Integer(readOnly=True, description='The identifier of the categroy'),
    'name' : fields.String(required = True, description = 'Category Name'),
})

pagination = api.model('One Page of products',{
    'page' : fields.Integer(description = 'current page'),
    'pages' : fields.Integer(description = 'Total pages'),
    'items_per_page' : fields.Integer(description = 'Items per page'),
    'total_items' : fields.Integer(description = 'Total amount of Items')
})

page_with_products = api.inherit('Page with Products', pagination, {
    'items' : fields.List(fields.Nested(product))
})

