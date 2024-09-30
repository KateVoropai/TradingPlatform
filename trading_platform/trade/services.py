from offer.models import Offer
from trade.models import Trade
from inventory.models import Inventory


def find_matching_offers():
    buy_offers = Offer.objects.filter(type='buy').order_by('-price')
    sell_offers = Offer.objects.filter(type='sell').order_by('price')
    
    for buy_offer in buy_offers:
        for sell_offer in sell_offers:
            if buy_offer.price >= sell_offer.price and buy_offer.quantity <= sell_offer.quantity:
                execute_trade(buy_offer, sell_offer)


def execute_trade(buy_offer, sell_offer):
    quantity = min(buy_offer.quantity, sell_offer.quantity)
    price = sell_offer.price

    # Создание сделки
    trade = Trade.objects.create(
        buyer=buy_offer.user, seller=sell_offer.user, item=buy_offer.item, 
        price=price, quantity=quantity
    )

    # Обновление инвентаря
    buyer_inventory, _ = Inventory.objects.get_or_create(user=buy_offer.user, item=buy_offer.item)
    buyer_inventory.quantity += quantity
    buyer_inventory.save()

    seller_inventory = Inventory.objects.get(user=sell_offer.user, item=sell_offer.item)
    seller_inventory.quantity -= quantity
    seller_inventory.save()

    # Обновление офферов
    buy_offer.quantity -= quantity
    sell_offer.quantity -= quantity

    if buy_offer.quantity == 0:
        buy_offer.delete()
    else:
        buy_offer.save()

    if sell_offer.quantity == 0:
        sell_offer.delete()
    else:
        sell_offer.save()