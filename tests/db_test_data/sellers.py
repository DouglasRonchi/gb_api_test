from app.models.database.seller import Seller

seller_data = [
    {
        "name": "Fulano Santos",
        "cpf": "98765432122",
        "email": "test@test.com.br",
        "password": "1234@1234",
    },
    {
        "name": "Ciclano da Silva",
        "cpf": "15350946056",
        "email": "test1@test.com.ko",
        "password": "1234@1234",
    },
]


def load_sellers_db_data():
    for seller in seller_data:
        Seller(**seller).save_safe()
