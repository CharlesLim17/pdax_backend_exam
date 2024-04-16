from app.models.model import Account
from typing import List, Optional


class AccountRepository:
    def __init__(self):
        self.accounts: List[Account] = []

    def save_account(self, account: Account) -> None:
        self.accounts.append(account)

    def find_account_by_id(self, account_id: int) -> Optional[Account]:
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        return None

    def find_accounts_by_customer_id(self, customer_id: int) -> List[Account]:
        return [account for account in self.accounts if account.customer_id == customer_id]