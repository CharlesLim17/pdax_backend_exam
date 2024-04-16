from app.models.model import TransactionType
from app.controllers.accountController import AccountController
from app.controllers.statementController import StatementController
from app.repositories.accountRepo import AccountRepository


if __name__ == "__main__":
    account_repo = AccountRepository()
    account_controller = AccountController(account_repo)
    statement_controller = StatementController(account_repo)

    # Create a new account
    new_account = account_controller.create_account(
        customer_id=1, name="Charles Lim", email="choylim06@gmail.com", phone_number="+639056601728"
    )
    print("\nNew Account:", new_account)

    # Make Deposit
    account_controller.make_transaction(
        account_id=new_account.account_id, amount=100.0, transaction_type=TransactionType.deposit
    )

    # Make Withdrawal
    account_controller.make_transaction(
        account_id=new_account.account_id, amount=50.0, transaction_type=TransactionType.withdraw
    )

    # Generate account statement
    statement = statement_controller.generate_account_statement(account_id=new_account.account_id)
    print("\n"+statement)
