# User Case Testing Documentation

## Overview

User case testing (also called integration testing or end-to-end testing) validates complete user workflows from start to finish. Unlike unit tests that test individual components, user case tests ensure that multiple components work together correctly to achieve real-world user goals.

---

## What is User Case Testing?

**User Case Testing** simulates real user scenarios by:
- Testing complete workflows (not just individual endpoints)
- Validating data flow between multiple components
- Ensuring business logic works end-to-end
- Verifying user stories are implemented correctly

**Example**: Instead of just testing "add to cart" endpoint, we test the entire purchase flow: browse → add to cart → checkout → confirm → complete → review.

---

## Implemented User Case Tests

### 1. Complete Purchase Flow ✅

**File**: `marketplace/tests.py` → `UserCaseTest_CompletePurchaseFlow`

**User Story**: 
> As a buyer, I want to browse products, add items to my cart, checkout, and leave a review after receiving the item.

**Workflow Tested**:
```
1. Browse products (unauthenticated) ✓
2. View product details ✓
3. Register new account ✓
4. Login ✓
5. Add multiple products to cart ✓
6. View cart with totals ✓
7. Checkout and create order ✓
8. Seller views incoming orders ✓
9. Seller confirms order ✓
10. Seller marks order as completed ✓
11. Buyer leaves 5-star review ✓
12. Review appears on product page ✓
```

**Run Test**:
```bash
python manage.py test marketplace.tests.UserCaseTest_CompletePurchaseFlow.test_complete_purchase_flow
```

**Expected Result**: All 12 steps pass, order created, review submitted

---

### 2. Seller Listing Flow ✅

**File**: `marketplace/tests.py` → `UserCaseTest_SellerListingFlow`

**User Story**: 
> As a seller, I want to create a product listing, edit it, receive orders, and manage sales.

**Workflow Tested**:
```
1. Seller creates product listing ✓
2. Seller views their listings ✓
3. Seller edits product (title, price) ✓
4. Buyer purchases the product ✓
5. Seller confirms order ✓
6. Seller completes order ✓
7. Product quantity decreases correctly ✓
```

**Run Test**:
```bash
python manage.py test marketplace.tests.UserCaseTest_SellerListingFlow.test_seller_listing_flow
```

**Expected Result**: Product created, edited, sold, quantity updated

---

### 3. Order Cancellation Flow ✅

**File**: `marketplace/tests.py` → `UserCaseTest_OrderCancellation`

**User Story**: 
> As a buyer, I want to cancel my order before the seller confirms it, and get my product quantity restored.

**Workflows Tested**:

#### Scenario A: Cancel Pending Order
```
1. Buyer places order (quantity: 2) ✓
2. Product quantity decreases (5 → 3) ✓
3. Buyer cancels pending order ✓
4. Product quantity restored (3 → 5) ✓
```

#### Scenario B: Cannot Cancel Confirmed Order
```
1. Buyer places order ✓
2. Seller confirms order ✓
3. Buyer tries to cancel ✗
4. Order remains confirmed ✓
```

**Run Tests**:
```bash
python manage.py test marketplace.tests.UserCaseTest_OrderCancellation.test_buyer_cancels_pending_order
python manage.py test marketplace.tests.UserCaseTest_OrderCancellation.test_buyer_cannot_cancel_confirmed_order
```

**Expected Result**: Pending orders can be cancelled, confirmed orders cannot

---

### 4. Review System Flow ✅

**File**: `marketplace/tests.py` → `UserCaseTest_ReviewSystem`

**User Story**: 
> As a buyer, I want to leave reviews only for products I've purchased, and see accurate ratings.

**Workflows Tested**:

#### Scenario A: Review Completed Orders
```
1. Create completed order ✓
2. Buyer leaves review ✓
3. Review appears on product ✓
```

#### Scenario B: Cannot Review Twice
```
1. Buyer leaves first review ✓
2. Buyer tries to leave second review ✗
3. System prevents duplicate review ✓
```

#### Scenario C: Rating Calculation
```
1. Initial rating: 0.0 (no reviews) ✓
2. Buyer 1 leaves 5-star review ✓
3. Buyer 2 leaves 4-star review ✓
4. Buyer 3 leaves 3-star review ✓
5. Average rating: 4.0 ✓
6. Review count: 3 ✓
```

**Run Tests**:
```bash
python manage.py test marketplace.tests.UserCaseTest_ReviewSystem.test_buyer_can_only_review_completed_orders
python manage.py test marketplace.tests.UserCaseTest_ReviewSystem.test_buyer_cannot_review_twice
python manage.py test marketplace.tests.UserCaseTest_ReviewSystem.test_product_rating_updates_with_reviews
```

**Expected Result**: Reviews work correctly, ratings calculated accurately

---

### 5. Multiple Roles Flow ✅

**File**: `marketplace/tests.py` → `UserCaseTest_MultipleRoles`

**User Story**: 
> As a user with 'both' role, I want to both buy and sell products on the platform.

**Workflows Tested**:

#### Scenario A: User Can Sell and Buy
```
1. User creates product listing (as seller) ✓
2. User purchases from another seller (as buyer) ✓
3. User has both purchases and sales ✓
```

#### Scenario B: Cannot Buy Own Product
```
1. User creates product ✓
2. User tries to add own product to cart ✗
3. System prevents self-purchase ✓
```

**Run Tests**:
```bash
python manage.py test marketplace.tests.UserCaseTest_MultipleRoles.test_user_can_sell_and_buy
python manage.py test marketplace.tests.UserCaseTest_MultipleRoles.test_user_cannot_buy_own_product
```

**Expected Result**: Users with 'both' role can buy and sell, but not buy own products

---

## Running All User Case Tests

### Run All User Case Tests
```bash
python manage.py test marketplace.tests.UserCaseTest
```

### Run with Verbose Output
```bash
python manage.py test marketplace.tests.UserCaseTest --verbosity=2
```

### Expected Output
```
test_buyer_cancels_pending_order (marketplace.tests.UserCaseTest_OrderCancellation) ... ok
test_buyer_cannot_cancel_confirmed_order (marketplace.tests.UserCaseTest_OrderCancellation) ... ok
test_buyer_can_only_review_completed_orders (marketplace.tests.UserCaseTest_ReviewSystem) ... ok
test_buyer_cannot_review_twice (marketplace.tests.UserCaseTest_ReviewSystem) ... ok
test_product_rating_updates_with_reviews (marketplace.tests.UserCaseTest_ReviewSystem) ... ok
test_complete_purchase_flow (marketplace.tests.UserCaseTest_CompletePurchaseFlow) ... ok
test_seller_listing_flow (marketplace.tests.UserCaseTest_SellerListingFlow) ... ok
test_user_can_sell_and_buy (marketplace.tests.UserCaseTest_MultipleRoles) ... ok
test_user_cannot_buy_own_product (marketplace.tests.UserCaseTest_MultipleRoles) ... ok

----------------------------------------------------------------------
Ran 9 tests in X.XXXs

OK
```

---

## Test Coverage Summary

### User Workflows Covered

| Workflow | Test Class | Status |
|----------|-----------|--------|
| Complete Purchase (Browse → Review) | UserCaseTest_CompletePurchaseFlow | ✅ |
| Seller Listing (Create → Sale) | UserCaseTest_SellerListingFlow | ✅ |
| Order Cancellation | UserCaseTest_OrderCancellation | ✅ |
| Review System | UserCaseTest_ReviewSystem | ✅ |
| Multiple Roles | UserCaseTest_MultipleRoles | ✅ |

### User Stories Validated

- ✅ Buyer can browse, purchase, and review products
- ✅ Seller can list, edit, and manage sales
- ✅ Buyer can cancel pending orders
- ✅ Review system prevents duplicates and calculates ratings
- ✅ Users with 'both' role can buy and sell
- ✅ Users cannot purchase their own products
- ✅ Product quantities update correctly
- ✅ Order status transitions work properly

---

## Benefits of User Case Testing

### 1. **Validates Real User Scenarios**
- Tests actual user workflows, not just individual functions
- Ensures features work together as intended

### 2. **Catches Integration Issues**
- Identifies problems that unit tests miss
- Validates data flow between components

### 3. **Documents User Stories**
- Tests serve as executable documentation
- Shows how features are supposed to work

### 4. **Prevents Regressions**
- Ensures new changes don't break existing workflows
- Provides confidence when refactoring

### 5. **Business Logic Validation**
- Verifies business rules are enforced
- Tests edge cases in real scenarios

---

## Writing New User Case Tests

### Template

```python
class UserCaseTest_MyWorkflow(APITestCase):
    """
    Test Case: My Workflow Description
    User Story: As a [role], I want to [goal], so that [benefit].
    """
    
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        
        # Create users
        self.user = User.objects.create_user(
            username='testuser',
            email='test@ashesi.edu.gh',
            password='pass123'
        )
        
        # Create other test data
        # ...
    
    def test_my_workflow(self):
        """Test complete workflow from start to finish"""
        
        # Step 1: User does something
        response = self.client.post('/api/endpoint/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Step 2: User does next thing
        response = self.client.get('/api/endpoint/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Step 3: Verify final state
        # ...
```

### Best Practices

1. **Name tests clearly**: Use descriptive names that explain the workflow
2. **Document user stories**: Include user story in docstring
3. **Test complete flows**: Don't stop halfway through a workflow
4. **Verify state changes**: Check that data is updated correctly
5. **Test both success and failure**: Include negative test cases
6. **Use realistic data**: Create data that resembles production
7. **Keep tests independent**: Each test should work in isolation

---

## Comparison: Unit Tests vs User Case Tests

### Unit Tests
- Test individual components
- Fast execution
- Isolated functionality
- Example: "Can user add item to cart?"

### User Case Tests
- Test complete workflows
- Slower execution
- Integrated functionality
- Example: "Can user browse, add to cart, checkout, and review?"

### Both Are Important!
- **Unit tests**: Catch bugs early, fast feedback
- **User case tests**: Ensure features work together, validate business logic

---

## Continuous Integration

### GitHub Actions Example

```yaml
name: User Case Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run User Case Tests
      run: |
        python manage.py test marketplace.tests.UserCaseTest --verbosity=2
```

---

## Future User Case Tests

### Planned Workflows

1. **Password Reset Flow**
   - Request reset → Receive email → Reset password → Login

2. **Wishlist Flow**
   - Add to wishlist → View wishlist → Purchase from wishlist

3. **Seller Analytics Flow**
   - View sales dashboard → Filter by date → Export report

4. **Admin Moderation Flow**
   - Report product → Admin reviews → Admin takes action

5. **Payment Integration Flow**
   - Add to cart → Checkout → Pay via Mobile Money → Confirm

---

## Troubleshooting

### Test Fails: "Order not found"
**Cause**: Order ID not captured correctly
**Fix**: Ensure you save `order_id = response.data['id']` after checkout

### Test Fails: "Permission denied"
**Cause**: User not authenticated
**Fix**: Use `self.client.force_authenticate(user=self.user)` before API calls

### Test Fails: "Product quantity not updated"
**Cause**: Need to refresh from database
**Fix**: Use `self.product.refresh_from_db()` before checking quantity

### Tests Are Slow
**Cause**: Database operations are slow
**Fix**: Use in-memory SQLite: `python manage.py test --keepdb`

---

## Resources

- [Django Testing Documentation](https://docs.djangoproject.com/en/4.2/topics/testing/)
- [DRF Testing Guide](https://www.django-rest-framework.org/api-guide/testing/)
- [Integration Testing Best Practices](https://martinfowler.com/bliki/IntegrationTest.html)

---

**Last Updated**: April 30, 2026
**Total User Case Tests**: 9 scenarios across 5 test classes
**Status**: ✅ All tests passing
