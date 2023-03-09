from app.models.database.order import Order

order_data = [
    {
        "code": "1505",
        "value": "500",
        "cpf": "12345678900",
        "date": "2022-04-13 18:14:31.972000",
    },
    {
        "code": "22890",
        "value": "1400",
        "cpf": "98765432122",
        "date": "2022-04-13 18:14:31.972000",
    },
    {
        "code": "546",
        "value": "1800",
        "cpf": "15350946056",
        "status": "approved",
        "date": "2022-04-13 18:14:31.972000",
    },
]


def load_orders_db_data():
    for order in order_data:
        Order(**order).save_safe()
