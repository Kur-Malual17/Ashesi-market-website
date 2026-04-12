# Table Names Updated with `market_` Prefix

## All Tables Now Have Prefix

To avoid conflicts with your other apps in the shared PostgreSQL database, all tables now have the `market_` prefix:

### Updated Table Names:

| Old Name | New Name |
|----------|----------|
| `users` | `market_users` |
| `categories` | `market_categories` |
| `products` | `market_products` |
| `product_images` | `market_product_images` |
| `cart` | `market_cart` |
| `cart_items` | `market_cart_items` |
| `orders` | `market_orders` |
| `order_items` | `market_order_items` |
| `reviews` | `market_reviews` |

### Django Auth Tables (Automatic):

Django will also create these tables (with default names):
- `auth_group`
- `auth_group_permissions`
- `auth_permission`
- `django_admin_log`
- `django_content_type`
- `django_migrations`
- `django_session`

These are standard Django tables and won't conflict with other Django apps.

## Deploy Steps

### 1. Add DATABASE_URL to Railway

Go to your Django service → Variables → Add:
```
DATABASE_URL=postgresql://postgres:rbPzVpKUvmepOKVlIIGZrvDcBbfRzkDN@postgres-h30n.railway.internal:5432/railway
```

### 2. Deploy Code

```bash
cd ashesi_market_django
git add .
git commit -m "Add market_ prefix to all tables and configure PostgreSQL"
git push
```

### 3. Verify in Railway Logs

After deployment, check logs for:
```
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
  Applying marketplace.0001_initial... OK
```

### 4. Check Database

In Railway PostgreSQL → Data tab, you should see:
- `market_users`
- `market_products`
- `market_categories`
- `market_cart`
- `market_orders`
- etc.

All with the `market_` prefix! ✅

## Benefits

✅ **No conflicts** with other apps in the same database
✅ **Easy to identify** which tables belong to Ashesi Market
✅ **Clean separation** even in shared database
✅ **Easy to backup/restore** just the market tables
✅ **Easy to delete** if needed (just drop market_* tables)

## Testing After Deployment

1. **Register a user** - creates row in `market_users`
2. **Create a product** - creates row in `market_products`
3. **Add to cart** - creates rows in `market_cart` and `market_cart_items`
4. **Place order** - creates rows in `market_orders` and `market_order_items`

All data will persist across deployments! 🎉

## If You Need to Reset

To start fresh (delete all market data):

```sql
DROP TABLE IF EXISTS market_reviews CASCADE;
DROP TABLE IF EXISTS market_order_items CASCADE;
DROP TABLE IF EXISTS market_orders CASCADE;
DROP TABLE IF EXISTS market_cart_items CASCADE;
DROP TABLE IF EXISTS market_cart CASCADE;
DROP TABLE IF EXISTS market_product_images CASCADE;
DROP TABLE IF EXISTS market_products CASCADE;
DROP TABLE IF EXISTS market_categories CASCADE;
DROP TABLE IF EXISTS market_users CASCADE;
```

Then redeploy to recreate tables.

## Summary

✅ All tables prefixed with `market_`
✅ No conflicts with other apps
✅ Ready to deploy with PostgreSQL
✅ Data will persist forever

Deploy now! 🚀
