def transform_orders(raw_orders):
    """Modtag rå ordredata og omdan dem til et format klar til database."""
    transformed_orders = []

    for order in raw_orders:
        transformed_order = {
            "order_id": int(order["order_id"]),
            "customer_id": int(order["customer_id"]),
            "order_status": int(order["order_status"]),
            "order_date": order["order_date"],
            "required_date": order["required_date"],
            "shipped_date": None if order["shipped_date"] in [None, "NULL", ""] else order["shipped_date"],
            "store": order["store"].strip(),
            "staff_name": order["staff_name"].strip()
        }
        transformed_orders.append(transformed_order)

    return transformed_orders
