from database import DAO
class Model:

    def get_anni(self):
        return DAO.DAO.get_anni()

    def get_brands(self):
        return DAO.DAO.get_brands()

    def get_retailers(self):
        return DAO.DAO.get_retailers()

    def top_vendite(self, anno, brand, retailer):
        return DAO.DAO.top_vendite(anno, brand, retailer)