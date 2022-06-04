# import json
# import uuid
# from datetime import datetime
# from typing import List
#
# batch_no = 0
# now = datetime.utcnow()
#
#
# class Product:
#     def __init__(self, name):
#         self.id = uuid.uuid4().hex
#         self.name = name
#
#
# class Demand:
#     def __init__(self, products: List[Product]):
#         global batch_no, now
#         batch_no += 1
#         self.batch_no = batch_no
#         self.id = uuid.uuid4().hex
#         self.demand_date = now
#         self.products = products
#         print(self.batch_no)
#
#     def to_json(self):
#         return {
#             "batch_no": self.batch_no,
#             "demand_date": str(f"{self.demand_date.day}, {self.demand_date.month} {self.demand_date.year}, "
#                                f"{self.demand_date.hour}:{self.demand_date.minute}:{self.demand_date.second}"),
#             "products": [product.name for product in self.products]
#         }
#
#
# products = [
#     Product('despririe'),
#     Product('sar dard gulai'),
#     Product('tokhe golai'),
# ]
#
# batch_1 = Demand(products=products)
# print(json.dumps(batch_1.to_json(), indent=4))
#
# batch_2 = Demand(products=products)
# print(json.dumps(batch_2.to_json(), indent=4))
#
# batch_3 = Demand(products=products)
# print(json.dumps(batch_3.to_json(), indent=4))
#
# batch_4 = Demand(products=products)
# print(json.dumps(batch_4.to_json(), indent=4))
