"""
Dependency Inversion Principle (DIP)
High level modules should not depend on low level modules. Both should depend on abstractions.
Abstractions should not depend on details. Details should depend on abstractions.
High level and low level module definitions are relative and not absolute.
Ps: Dependency Inversion and Dependency Injection are different concepts.
"""
# Dont do it
class MySqlProductRepository:
    def get_all_product_names(self):
        return ["phone", "laptop", "tablet"]


class ProductCatalog:
    def get_all_products_list(self):
        product_manager = MySQLProductRepository()
        product_manager.get_all_product_names()

"""
In this example, ProductCatalog is a high level module and ProductManager is a low level module
and ProductCatalog depends on ProductManager.
"""

# Do it
class ProductRepository:
    def get_all_product_names(self) -> [str]:
        raise NotImplementedError()


class MysqlProductRepository(ProductRepository):
    def get_all_product_names(self):
        return ["phone", "laptop", "tablet"]


class MongoProductRepository(ProductRepository):
    def get_all_product_names(self):
        return ["book", "pen", "eraser"]


class ProductFactory:
    @staticmethod
    def create() -> ProductRepository:
        #return MongoProductRepository()
        return MysqlProductRepository()


class ProductCatalog:
    def get_all_products_list(self):
        product_manager = ProductFactory.create()
        print(product_manager.get_all_product_names())


product_catalog = ProductCatalog()
product_catalog.get_all_products_list()

""" Now ProductCatalog(high level) class not depended with MysqlProductRepository(low level) class
they both depends on ProductRepository(abstraction) class. In the future if MongoRepository inherited ProductRepository
only change ProductFactory create method and it will run
"""

# A little dependency injection sample
"""
if you create a class has named ListingApp between ProductCatalog and ProductFactory
when ProductCatalogs objects create, it gets a MysqlProductRepository object
ProductCatalog object is free to use the ProductRepository object
we are injecting the dependency into ProductCatalog object, instead of ProductCatalog
"""
class ProductRepository:
    def get_all_product_names(self) -> [str]:
        raise NotImplementedError()


class MysqlProductRepository(ProductRepository):
    def get_all_product_names(self):
        return ["phone", "laptop", "tablet"]


class MongoProductRepository(ProductRepository):
    def get_all_product_names(self):
        return ["book", "pen", "eraser"]


class ProductFactory:
    @staticmethod
    def create() -> ProductRepository:
        #return MongoProductRepository()
        return MysqlProductRepository()


class ProductCatalog:
    def __init__(self, product_manager: ProductRepository):
        self.product_manager = product_manager

    def get_all_products_list(self):
        return self.product_manager.get_all_product_names()


class ListingApp:
    def list_products(self):
        product_manager = ProductFactory.create()
        product_catalog = ProductCatalog(product_manager)
        print(product_catalog.get_all_products_list())


listing_app = ListingApp()
listing_app.list_products()
