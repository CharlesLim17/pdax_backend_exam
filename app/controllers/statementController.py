from app.repositories.accountRepo import AccountRepository


class StatementController:
    def __init__(self, account_repo: AccountRepository):
        self.account_repo = account_repo

    def generate_account_statement(self, account_id: int) -> str:
        account = self.account_repo.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found")

        statement = f"Account Statement for Account ID: {account_id}\n"
        statement += f"Current Balance: {account.get_balance()}\n"
        return statement
