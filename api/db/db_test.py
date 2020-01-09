from db.db_managers import *


class ProManagerTester:
    def __init__(self,  db_name, hall_name):
        self.pro_manager = ProManager(db_name, hall_name)

    def run_api(self, api, *args):
        self.pro_manager.api(*args)




def test_MysqlManager():
    mysql = MysqlManager()
    mysql.create_db('test2')
    print(
        mysql.read_db_list()
    )


def test_HallManager():
    hall_manager = HallManager('test2', 'test_hall2')
    hall_manager.delete_hall()
    print(
        hall_manager.read_hall_names()
    )


def test_Promanager():
    pro_manager = ProManager('test2', 'test_hall1')
    pro_manager.delete_pro_by_date(20190201, 20190301)
    r = pro_manager.select_pro_by_date(20190201, 20190301)
    for row in r:
        print(row)


if __name__ == '__main__':
    test_HallManager()

