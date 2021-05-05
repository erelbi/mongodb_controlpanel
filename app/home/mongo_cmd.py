from app  import mongo_client
from bson.objectid import ObjectId

class MongoClient:
    db_name='admin'
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

    @staticmethod
    def mongo_get_users(db_name):
        try:
            func = getattr(mongo_client, db_name)
            return func.command("usersInfo")
        except Exception as err:
            print(err)
            return err
        finally:
            mongo_client.close()
    @staticmethod
    def mongo_create_user(db_name,user,passwd,role):
        try:
            func = getattr(mongo_client,db_name)
            return func.command('createUser',user,pwd=passwd,roles=[role])
        except Exception as err:
            print(err)
            return  err
        finally:
            mongo_client.close()

    @staticmethod
    def mongo_stat(db_name):
        status=dict()
        try:
            func = getattr(mongo_client, db_name)
            mongostat = func.command('serverStatus')
            status['mem'] = mongostat['mem']
            status['network'] = mongostat['network']
            status['opcounters'] = mongostat['opcounters']
            status['globalLock'] = mongostat['globalLock']
            return  status
        except Exception as err:
            print(err)
            return err
        finally:
            mongo_client.close()

    @staticmethod
    def delete_document(db_name,collection,_id):
        try:
            cursor = mongo_client[db_name]
            document = getattr(cursor, collection)
            document.delete_one({'_id': ObjectId(_id)})
            return {'delete':'ok'}
        except Exception as err:
            print(err)
            return err
        finally:
            mongo_client.close()

    @staticmethod
    def mongo_log(db_name,type):
        try:
            func = getattr(mongo_client, db_name)
            return func.command({'getLog':type})
        except Exception as err:
            print(err)
            return err
        finally:
            mongo_client.close()







