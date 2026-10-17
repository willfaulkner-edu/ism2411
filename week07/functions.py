def calculate_tax(subtotal, tax_rate=0.07):
    """Calculates the sales tax based on the subtotal and tax rate."""
    return subtotal * tax_rate

def apply_discount(subtotal, discount_percent=0.10):
    """Calculates the discount amount based on the subtotal and discount percentage."""
    return subtotal * discount_percent

def final_price(subtotal, tax_rate=0.07, discount_percent=0.10):
    """Calculates the final price after applying discounts and adding tax."""
    discount = apply_discount(subtotal, discount_percent)
    discounted_total = subtotal - discount
    tax = calculate_tax(discounted_total, tax_rate)
    return round(discounted_total + tax, 2)