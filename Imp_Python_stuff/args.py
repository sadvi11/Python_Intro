def fruit_basket(*args, **kwargs):
    print("Fruits:", args)
    print("Details:", kwargs)

fruit_basket("apple", "banana", quantity=5, fresh=True)
