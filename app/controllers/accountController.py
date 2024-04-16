from app.models.model import Account, TransactionType
from app.repositories.accountRepo import AccountRepository


class AccountController:
    def __init__(self, account_repo: AccountRepository):
        self.account_repo = account_repo

    def create_account(
        self, customer_id: int, name: str, email: str, phone_number: str
    ) -> Account:
        account_id = len(self.account_repo.accounts) + 1
        account_number = f"ACCT-{account_id}"
        new_account = Account(
            account_id=account_id,
            customer_id=customer_id,
            account_number=account_number,
            balance=0.0,
        )
        self.account_repo.save_account(new_account)
        return new_account

    def make_transaction(
        self, account_id: int, amount: float, transaction_type: TransactionType
    ) -> None:
        account = self.account_repo.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found")

        if transaction_type == TransactionType.deposit:
            account.deposit(amount)
        elif transaction_type == TransactionType.withdraw:
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type")