from app  import mongo_client

class MongoClient:

    @staticmethod
    def usersInfo(db_name):
        try:
            func = getattr(mongo_client,db_name)
            return func.command("usersInfo")
        except Exception as err:
            return err
        finally:
            mongo_client.close()

    @staticmethod
    def list_databases():
        try:
            return mongo_client.list_databases()
        except Exception as err:
            return err
        finally:
            mongo_client.close()

    @staticmethod
    def serverStatus(db_name):
        try:
            func = getattr(mongo_client, db_name)
            return func.command("serverStatus")
        except Exception as err:
            return err
        finally:
            mongo_client.close()

    @staticmethod
    def connection_users(db_name):
        conn_info = []
        user = {}
        try:
            func = getattr(mongo_client, db_name)
            with func.aggregate([{"$currentOp": {"allUsers": True}}]) as cursor:
                for operation in cursor:
                    if 'client' in operation.keys():
                        user['host'] = operation['client']
                        user['id'] = operation['connectionId']
                        user['time'] = operation['currentOpTime']
                        conn_info.append(user)
            return conn_info
        except Exception as err:
            return err
        finally:
            mongo_client.close()

    @staticmethod
    def collection_get(db_name):
        try:
            return mongo_client[db_name].list_collection_names()
        except Exception as err:
            return err
        finally:
            mongo_client.close()

    @staticmethod
    def documents_get(db_name,collection):
        try:
            cursor = mongo_client[db_name]
            document = getattr(cursor,collection)
            return document.find({})
        except Exception as err:
            return err
        finally:
            mongo_client.close()






