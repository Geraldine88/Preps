"""
    A product is a single purchasable item.

    It will;
        - Provide price
        - Provide product information

    Note that quantity does not belong to product

"""


class Product:
    def __init__(self, productId, productName, productPrice):
        self.productId = productId
        self.productName = productName
        self.productPrice = productPrice
        self.productCategory = []


    def getPrice(self):
        return self.productPrice


    # def getQuantity(self):
    #     return self.productQuantity


    # def addProduct(self, productId):
    #     return self.productQuantity.append(productId)

    # def removeProduct(self, productId):
    #     if not self.productQuantity:
    #         return "There are no products."

    #     return self.productQuantity.remove(productId)

    # This is where we display the metadata of product
    def getCategory(self, productId):
        return self.productCategory[productId]
