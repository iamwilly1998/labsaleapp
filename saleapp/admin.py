from saleapp import app, db
from flask_admin import Admin, BaseView
from flask_admin.contrib.sqla import ModelView
from saleapp.models import Category, Product


admin = Admin(app=app, name="Quản trị viên", template_mode="bootstrap4")

class ProductView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    column_filters = ['name', 'price']
    column_searchable_list = ['name', 'description', 'price', 'category_id']
    column_exclude_list = ['image']
    column_labels = {
        "name": "Tên sản phẩm",
        "description": "Mô tả",
        "price": "Giá bán",
        "category": "Danh mục",
        "id": "Mã sản phẩm"
    }
    column_sortable_list = ['id', 'name', 'price']
    column_list = ['id', 'name', 'description', 'price', 'category']


admin.add_view(ModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
