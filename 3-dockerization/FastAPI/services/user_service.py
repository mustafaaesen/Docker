#kurallar ve kararlar buradadır backendin beynidir
#routesta öağırılan fonksiyonlar ve çıktıları yer alır

from services.activity_service import log_activity
#activity sevsinin import edilemsi yapılanalarda aktivite kaydı için
#ör kullanıcı kayıt tarihi yapılma tarihi etkisinin kadı gibi



_users_db = []

def create_user(user):
    if len(user.username)<3:

        raise ValueError("Username must be at least 3 characters")
    
    new_user={
        "id":len(_users_db)+1,
        "username":user.username,
        "email":user.email
    }

    _users_db.append(new_user)

    log_activity(new_user["id"],"user_created")#aktivitenin kaydedilmesi paralel olarak


    return new_user

#kuallnıcı ooluşturmak için routes ta çapğırlır şartkarı sağlarsa yeni kullanıcı sağlamazsa hata mesajını döner

def list_users():
    return _users_db  #routes ta tüm listeleme route ında çağırlır tüm kayıtları döner

def get_user_by_id(user_id: int):

    for user in _users_db:
        if user["id"] == user_id:
            return user
        
    return None #kullanıcı bulursa user bulamazsa none döner routes ta id ye göre bulmada çağırılır

def delete_user(user_id : int):

    for user in _users_db:
        if user["id"]==user_id:
            _users_db.remove(user)

            log_activity(user_id,"user_deleted")#kullanıcı silinmesi

            return True
    return False                   #id ye göre ara bulursa sile bulamazsa flase döner routesta çağırılır