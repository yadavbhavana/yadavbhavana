def shopping_total(items):
    """
    Calculate the total cost of a shopping list with 10% discount for items over $50 NZD.
    
    Args:
        items: String containing comma-separated item_name,price pairs
        
    Returns:
        float: Total amount rounded to one decimal place
    """
    if not items.strip():
        return 0.0
    
    # Split the items string into individual item pairs
    item_pairs = items.split(',')
    
    total = 0.0
    
    # Process items in pairs (name, price)
    for i in range(0, len(item_pairs), 2):
        if i + 1 < len(item_pairs):
            item_name = item_pairs[i].strip()
            try:
                price = float(item_pairs[i + 1].strip())
                
                # Apply 10% discount if price > $50
                if price > 50.0:
                    price = price * 0.9  # 10% discount
                
                total += price
                
            except ValueError:
                # Skip invalid price entries
                continue
    
    return round(total, 1)


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