# Shopping total calculation using lambda functions

# Lambda to apply 10% discount if price > $50
apply_discount = lambda price: price * 0.9 if price > 50.0 else price

# Helper function to safely parse float (wrapped in lambda style)
def safe_float_parse(s):
    try:
        return float(s.strip())
    except (ValueError, AttributeError):
        return 0.0

# Lambda to process price string and apply discount
process_price = lambda price_str: apply_discount(safe_float_parse(price_str))

# Main shopping total function using lambda and functional programming
shopping_total = lambda items: round(
    sum(map(process_price, 
        [items.split(',')[i] for i in range(1, len(items.split(',')), 2)]
    )), 1
) if items.strip() else 0.0


# Test function with the provided examples
def test_shopping_total():
    # Example 1: Apple, 2.5, banana, 1.8, Orange, 3.2, Mango, 55.0
    # Expected: 2.5 + 1.8 + 3.2 + (55.0 * 0.9) = 2.5 + 1.8 + 3.2 + 49.5 = 57.0
    test1 = "Apple, 2.5, banana, 1.8, Orange, 3.2, Mango, 55.0"
    result1 = shopping_total(test1)
    print(f"Test 1: {result1} (expected 57.0)")
    
    # Example 2: Kiwi, 15, strawberry, 22, avocado, 60, guava, 25, pineapple, 70, pumpkin, 45
    # Expected: 15 + 22 + (60 * 0.9) + 25 + (70 * 0.9) + 45 = 15 + 22 + 54 + 25 + 63 + 45 = 224.0
    test2 = "Kiwi, 15, strawberry, 22, avocado, 60, guava, 25, pineapple, 70, pumpkin, 45"
    result2 = shopping_total(test2)
    print(f"Test 2: {result2} (expected 224.0)")


if __name__ == "__main__":
    test_shopping_total()