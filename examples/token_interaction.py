from kanvas.token import TokenHandler

# Initialize the token handler
token_handler = TokenHandler()

# Check available token balance
balance = token_handler.check_balance("user_address")
print(f"Token Balance: {balance} KANVA")

# Spend tokens to access a premium feature
token_handler.spend_tokens("user_address", 10)  # Spend 10 KANVA tokens
print("Tokens spent for premium access.")
