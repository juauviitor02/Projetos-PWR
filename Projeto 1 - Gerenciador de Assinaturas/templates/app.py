import __init__
from views.view import SubscriptionService
from models.database import engine
from datetime import datetime
from decimal import Decimal
from models.model import Subscription

class Ui:
    def __init__(self):
        self.subscription_service = SubscriptionService(engine)

    def start(self):
        while True:
            print("Bem vindo ao sistema de assinaturas!")
            print("""
            [1] -> Adicionar assinatura
            [2] -> Remover assinatura
            [3] -> Pagar assinatura
            [4] -> Remover pagamento
            [5] -> Valor total
            [6] -> Gastos últimos 12 meses
            [7] -> Sair
            """)

            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                self.add_subscription()
            elif choice == 2:
                self.delete_subscription()
            elif choice == 3:
                self.pay_subscription()
            elif choice == 4:
                self.delete_payment()
            elif choice == 5:
                self.total_value()
            elif choice == 6:
                self.subscription_service.get_chart()
            else:
                break
    
    def add_subscription(self):
        empresa = input("Informe o nome da empresa: ")
        site = input("Informe o site da empresa: ")
        data_assinatura = datetime.strptime(input("Informe a data da assinatura (dd/mm/YYYY):"), "%d/%m/%Y")
        valor = Decimal(input("Informe o valor da assinatura: "))

        subscription = Subscription(empresa=empresa, site=site, data_assinatura=data_assinatura, valor=valor)
        self.subscription_service.create(subscription)
        print("Assinatura cadastrada com sucesso!")

    def delete_subscription(self):
        assinaturas = self.subscription_service.list_all_subscriptions()
        print("Assinaturas cadastradas:")
        for n, i in enumerate(assinaturas):
            print(f"[{n}] - {i.id} - {i.empresa}")
        choice = int(input("Informe o id da assinatura que deseja remover: "))
        self.subscription_service.delete_subscription(choice)
        question = input("Deseja remover também o pagamento dessa assinatura? Y ou N: ")
        if question.upper() == "Y":
            self.subscription_service.delete_payment(choice)
        else:
            print("Pagamento não removido!")

    def total_value(self):
        print(f"O valor total das assinaturas esse mês é de R${self.subscription_service.total_value()}")

    def pay_subscription(self):
        assinaturas = self.subscription_service.list_all_subscriptions()
        print("Assinaturas cadastradas:")
        for i, s in enumerate(assinaturas):
            print(f"[{i}] - {s.empresa}")
        print(self.subscription_service.pay(assinaturas[int(input("Digite o número que corresponde a empresa que deseja pagar: "))]))
    
    def delete_payment(self):
        assinaturas = self.subscription_service.list_all_payments()
        print("Pagamentos cadastrados:")
        for n, i in enumerate(assinaturas):
            print(f"[{n}] - {i.subscription_id} - {i.empresa}")
        print(self.subscription_service.delete_payment(int(input("Informe o id da assinatura: "))))
    
Ui().start()
